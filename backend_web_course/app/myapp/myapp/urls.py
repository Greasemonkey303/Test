from django import views
from django.urls import URLPattern, path
from . import views

URLPattern = [
    path('', views.index, name= 'index')
]