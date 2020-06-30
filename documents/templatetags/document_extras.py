from django import template

register = template.Library()

@register.filter
def highlight(value, query):
    index = value.index(query)
    summary = value[index-20:index+20]
    start = summary.index(query)
    end = start + len(query)
    return '...' + summary[:start] + '<mark>' + query + '</mark>' + summary[end:] + '...'
