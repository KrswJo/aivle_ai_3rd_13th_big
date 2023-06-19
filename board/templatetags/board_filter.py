#board index 정렬
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import linebreaksbr

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def custom_linebreaksbr(value, arg):
    new_value = ""
    count = 0
    for char in value:
        new_value += char
        count += 1
        if count % arg == 0:
            new_value += "\n"
    return mark_safe(linebreaksbr(new_value))