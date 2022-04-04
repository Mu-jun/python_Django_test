# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question,Answer
from .forms import QuestionForm


# Create your views here.
def index(request):
    # return HttpResponse('안녕하세요 pybo에 오신것을 환영합니다.')
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date') # order_by 는 조회 결과를 정렬하는 함수
    # -create_date : 작성일 역순으로
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    # question = Question.objects.get(id=question_id) # id가 없을 때 500오류 보냄.
    question = get_object_or_404(Question, pk=question_id) # id가 없을 때 404오류 보내기
    context = {'question':question}
    return render(request, 'pybo/question_detail.html',context)

def answer_create(request, question_id):
    '''
    pybo 답변등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    # 방법1
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 방법2
    '''
    Answer모델을 사용하여 만들기
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    '''
    return redirect('pybo:detail', question_id=question_id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장(commit=False)하여 question 객체를 리턴받는다.
            # QuestionForm 객체에는 현재 create_date 데이터가 없기 때문에 임시저장하여 값을 넣고나서 저장해야 한다.
            question.create_date = timezone.now()
            # create_date는 저장시점에 생성해야 하는 값이므로 저장할 때 생성하여 넣어준다.
            question.save()
            return redirect('pybo:index')        
    else :
        form = QuestionForm()
        
    return render(request, 'pybo/question_form.html', {'form':form})