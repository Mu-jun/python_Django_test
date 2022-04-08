'''
장고에서 사용하는 속성의 타입
https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

filter에 대한 자세한 사용법
https://docs.djangoproject.com/en/3.0/topics/db/queries/
'''
'''
makemigrations 명령은 장고가 테이블 작업을 수행하기 위한 작업 파일(예: 0001_initial.py)을 생성하는 명령어다. 실제 테이블 작업은 migrate 명령을 통해서만 가능하다.
'''
'''
author 속성에 null 허용하기

author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

null=True 속성을 부여하면 migrate시 데이터베이스에 null 허용 컬럼으로 생성된다.
'''

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # null=True : 데이터베이스에서 null을 허용한다는 뜻.
    # blank=True : form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 뜻.
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey( # 기존 모델과 연결
        Question,
        on_delete=models.CASCADE # 연결된 모델이 삭제될 경우 같이 삭제함.
        )
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)