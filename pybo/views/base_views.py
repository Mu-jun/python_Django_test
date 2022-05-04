from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

import logging
logger = logging.getLogger("pybo")

def index(request):
    logger.info('pybo접속')
    # return HttpResponse('안녕하세요 pybo에 오신것을 환영합니다.')
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date') # order_by 는 조회 결과를 정렬하는 함수
    # -create_date : 작성일 역순으로
    '''
    검색기능 추가
    '''
    kw =  request.GET.get('kw','')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__content__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    
    '''
    Paginator를 이용한 페이징
    '''
    page = request.GET.get('page','1') # 페이지 default: 1
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) # 장고 내부적으로 페이지의 데이터만 조회하도록 쿼리변경
    
    context = {
        'question_list': page_obj, # 게시물 전체 데이터 question_list
        'page': page,
        'kw': kw,
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