from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
     path("", views.default , name = 'defalt'),
    path("home/", views.home , name = 'home'),
    path("about/", views.about , name = 'about'),
]
   