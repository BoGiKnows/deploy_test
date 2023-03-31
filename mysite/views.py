from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm


# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f'<div><p>{item.title}</p><p>{item.content}</p></div><hr>'
#     return HttpResponse(res)


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'mysite/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': 'Список новостей',
        'category': category,
    }
    return render(request, 'mysite/category.html', context=context)


def view_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)  # News.objects.get(pk=news_id)
    return render(request, 'mysite/view_news.html', {'news_item': news})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data) # Для форм не связанных с моделями
            news = form.save() # Для форм, связанных с моделями
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'mysite/add_news.html', {'form': form})