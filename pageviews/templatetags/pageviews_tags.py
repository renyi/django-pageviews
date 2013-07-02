from django import template
from ..models import HitCount


register = template.Library()


@register.simple_tag(takes_context=True)
def pageviews(context):
    """
    Displays pageviews of the current page.
    """
    try:
        request = context['request']
        hit = HitCount.objects.get(url=request.path)
        return hit.hits
    except HitCount.DoesNotExist:
        return 0


@register.simple_tag
def pageviews_url(path):
    """
    Displays pageviews by url. Useful for list views.
    """
    try:
        hit = HitCount.objects.get(url=path)
        return hit.hits
    except HitCount.DoesNotExist:
        return 0
