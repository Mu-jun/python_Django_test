from tkinter import ALL
from .base import *
import os

ALLOWED_HOSTS = ['13.209.74.184']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []
DEBUG = False