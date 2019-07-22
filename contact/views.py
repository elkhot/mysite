from django.shortcuts import render


def contact(request):
    return render(request, 'mysite_contact.html')