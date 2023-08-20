from django import template

register = template.Library()

@register.filter
def endswith_section_b(value):
    return value.endswith("Section B")



