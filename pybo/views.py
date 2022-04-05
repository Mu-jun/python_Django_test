from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question,Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    # return HttpResponse('안녕하세요 pybo에 오신것을 환영합니다.')
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date') # order_by 는 조회 결과를 정렬하는 함수
    # -create_date : 작성일 역순으로
    '''
    Paginator를 이용한 페이징
    '''
    page = request.GET.get('page','1') # 페이지 default: 1
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) # 장고 내부적으로 페이지의 데이터만 조회하도록 쿼리변경
    context = {
        'question_list': page_obj # 게시물 전체 데이터 question_list
        }
    return render(request, 'pybo/question_list.html',context)
'''
page_obj 속성

paginator.count	전체 게시물 개수
paginator.per_page	페이지당 보여줄 게시물 개수
paginator.page_range	페이지 범위
number	현재 페이지 번호
previous_page_number	이전 페이지 번호
next_page_number	다음 페이지 번호
has_previous	이전 페이지 유무
has_next	다음 페이지 유무
start_index	현재 페이지 시작 인덱스(1부터 시작)
end_index	현재 페이지의 끝 인덱스(1부터 시작)
paginator.num_pages 마지막 페이지 번호
'''

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    # question = Question.objects.get(id=question_id) # id가 없을 때 500오류 보냄.
    question = get_object_or_404(Question, pk=question_id) # id가 없을 때 404오류 보내기
    context = {'question':question}
    return render(request, 'pybo/question_detail.html',context)

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
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)