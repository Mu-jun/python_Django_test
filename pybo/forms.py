from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question모델의 속성
        '''
        폼 위젯
        자동으로 생성되는 HTML에 부트스트랩 적용하기
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'rows': 10}),
        }
        '''
        '''
        폼 레이블
        자동으로 생성되는 HTML에 Subject, Content 한글로 표시하기
        '''
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }