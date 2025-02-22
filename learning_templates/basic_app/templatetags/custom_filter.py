from django import template

register=template.Library()
@register.filter('cutit')
def cutit(value,arg=3):
    return str(value).center(0)
# register.filter('cutit',cutit)