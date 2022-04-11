from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Answer, Question



@login_required(login_url='common:login')
def answer_create(request, question_id):
    '''
    pybo 답변등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    
    '''
    폼을 이용하지 않고 만들기
    
    # 방법1
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 방법2
    Answer모델을 사용하여 만들기
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()

    return redirect('pybo:detail', question_id=question_id)
    '''
    
    '''
    폼을 이용해서 HTML만들기
    '''
    
    if request.method=='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url="commom:login")
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method=="POST":
        form = AnswerForm(request.POST, instance=answer )
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer':answer, 'form':form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url="common:login")
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect('pybo:detail', question_id=answer.question.id)
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)