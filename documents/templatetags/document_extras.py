from django import template

register = template.Library()

@register.filter
def highlight(value, query):
    index = value.index(query)

    summary_start = index-20 if index-20 >= 0 else 0
    summary = value[summary_start:index+20]

    start = summary.index(query)
    end = start + len(query)
    
    return '...' + summary[:start] + '<mark>' + query + '</mark>' + summary[end:] + '...'
