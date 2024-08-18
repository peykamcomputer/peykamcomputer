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

@register.filter
def is_translate(value):
    msg1 = "erjime"
    msg2 = "еревод"
    if msg1 or msg2 in value:
        return True
    else:
        return False