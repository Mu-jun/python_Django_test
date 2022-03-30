'''
장고 관리자 기능
https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
'''

from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)