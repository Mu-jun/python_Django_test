from atexit import register
from django import template

import markdown
from django.utils.safestring import mark_safe
'''
마크다운 확장 기능 문서
https://python-markdown.github.io/extensions/
'''

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mul(value, arg):
    return value * arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))