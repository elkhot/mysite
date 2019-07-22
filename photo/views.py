from django.shortcuts import render



def photo(request):
    return render(request, 'mysite_photos.html')