from django.urls import path

from . import views

app_name = 'pybo' # 다른 앱에서 같은 url 별칭사용시 충돌방지

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
]
