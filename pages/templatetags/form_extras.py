# pages/templatetags/form_extras.py
from django import template
register = template.Library()

@register.filter
def as_widget(field, css):
    attrs = {}
    for part in css.split(","):
        k, v = part.split("=")
        attrs[k] = v
    return field.as_widget(attrs=attrs)
