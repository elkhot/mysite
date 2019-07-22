from django.shortcuts import render
from .models import Blog


def blog(request):
    blog = Blog.objects.all().order_by('date')
    return render(request, 'mysite_blog.html', {'blog': blog})


def blog_details(request, slug):
    article= Blog.objects.get(slug=slug)
    return render(request, 'mysite_blog_article.html', {'article': article})

