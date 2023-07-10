from django import template

register = template.Library()

@register.filter
def add_commas(value):
    if value is not None:
        try:
            value = int(value)
            return "{:,}".format(value)
        except (TypeError, ValueError):
            pass
    return value
