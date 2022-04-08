from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # form의 입력값을 개별적으로 얻고 싶을 때는 .cleanded_data.get('키값')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 사용자 인증
            user = authenticate(username=username, password=raw_password)
            # 로그인
            login(request, user)
            
            return redirect('index')
    else:
        form = UserForm()
    
    context = {'form': form }    
    return render(request, 'common/signup.html', context)
    
            