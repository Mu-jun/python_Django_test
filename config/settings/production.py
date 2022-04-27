from tkinter import ALL
from .base import *
import os

ALLOWED_HOSTS = ['13.209.74.184']
'''
# WSGI 서버(Gunicorn) 사용시

STATIC_ROOT = [
    os.path.join(BASE_DIR, 'static')
    
]
STATICFILES_DIRS = []
'''
DEBUG = False