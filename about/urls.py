from django.urls import path
from . import views

app_name = 'about'


urlpatterns =[
    path('', views.aboutme, name= 'about'),
    path('<slug>', views.about_details, name='detail'),
    ]