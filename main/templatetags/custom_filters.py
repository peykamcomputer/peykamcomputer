from atexit import register
from django import template
from django.conf import settings
import webcolors


register = template.Library()

@register.filter
def to_rgb(value):
    value = tuple(webcolors.name_to_rgb(value)) + (0.1,)
    return value

@register.filter
def split(value):
    return value.split('.')