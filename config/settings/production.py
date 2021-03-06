from .base import *
import os

ALLOWED_HOSTS = ['3.39.240.39', '.mujunkim.shop']

# WSGI 서버(Gunicorn) 사용시

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []

DEBUG = False # False면 static&media파일 제공안함
# static파일을 제공받으려면 python manage.py runserver --insecure
