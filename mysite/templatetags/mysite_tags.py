from django import template

from mysite.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('mysite/list_categories.html')
def show_categories(cat=None):
    categories = Category.objects.all()
    return {'categories': categories, 'category': cat}