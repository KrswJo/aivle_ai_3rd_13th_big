#board index 정렬
from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg