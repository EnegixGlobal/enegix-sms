from django import template
register = template.Library()
@register.filter
def get_item(dictobj, key):
    return dictobj.get(key)




