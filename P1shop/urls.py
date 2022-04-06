from django.urls import path
from . import views

app_name = 'P1shop'

urlpatterns = [
    path('', views.index, name='index' )
]
