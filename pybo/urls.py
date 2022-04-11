from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo' # 다른 앱에서 같은 url 별칭사용시 충돌방지

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    
    # question_views    
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    
    # answer_views
    path('answer/create/<int:question_id>/',answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
