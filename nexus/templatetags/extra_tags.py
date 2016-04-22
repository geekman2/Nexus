from django import template

register = template.Library()

@register.inclusion_tag('tab.html')
def weather(tab):
    return {'tab': tab}