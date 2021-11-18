from django import template
register = template.Library()

@register.filter(name='dot')
def dot(value):
    return str(value).replace(',','.')
 
