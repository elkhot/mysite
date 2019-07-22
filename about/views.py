from django.shortcuts import render
from .models import About


def aboutme(request):
    about = About.objects.all().order_by('date')
    return render(request, 'mysite_about.html', {'about': about})


def about_details(request, slug):
    article= About.objects.get(slug=slug)
    return render(request, 'mysite_about_article.html', {'article': article})




