from django import template
from django.db.models import Count

# from mainblog.sql_query import count_themes
from mainblog.models import BlogPost, ThemePost

# from mainblog.views import tags

register = template.Library()


@register.simple_tag()
def get_interesting():
    interesting = BlogPost.objects.filter()[:3]
    return {'interesting': interesting}


@register.simple_tag()
def get_themes():
    count_themes = ThemePost.objects.filter(themes__in=BlogPost.objects.all()).annotate(
        count=Count("*"))
    return {'count_themes': count_themes}
