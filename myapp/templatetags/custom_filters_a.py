from django import template

register = template.Library()

@register.filter
def endswith_section_a(value):
    return value.endswith("Section A")


