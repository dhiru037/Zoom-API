from django import template

register = template.Library()

@register.filter
def endswith_section_c(value):
    return value.endswith("Section C")

