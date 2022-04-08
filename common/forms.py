from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    '''
UserCreationForm 속성

username	사용자이름
password1	비밀번호1
password2	비밀번호2 (비밀번호1을 제대로 입력했는지 대조하기 위한 값)
    '''
    email = forms.EmailField(label="이메일")
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")