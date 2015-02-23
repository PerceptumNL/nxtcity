from django import template
from landing.models import Partner

register = template.Library()

@register.inclusion_tag('landing/tags/partners.html', takes_context=True)
def partners(context):
    return {
        'partners': Partner.objects.all(),
        'request': context['request']}

