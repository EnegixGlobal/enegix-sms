from django import template

register = template.Library()

@register.filter
def get_item(data, key):
    return data.get(key)