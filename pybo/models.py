from django.db import models

# Create your models here.
# 장고에서 사용하는 속성의 타입
# https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    question = models.ForeignKey( # 기존 모델과 연결
        Question,
        on_delete=models.CASCADE # 연결된 모델이 삭제될 경우 같이 삭제함.
        )
    content = models.TextField()
    create_date = models.DateTimeField()