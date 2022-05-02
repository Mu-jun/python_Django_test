from tkinter import ALL
from .base import *
import os

ALLOWED_HOSTS = ['13.209.74.184']

# WSGI 서버(Gunicorn) 사용시

STATIC_ROOT = [BASE_DIR/'static']
STATICFILES_DIRS = []

DEBUG = False # False면 static&media파일 제공안함
# static파일을 제공받으려면 python manage.py runserver --insecure