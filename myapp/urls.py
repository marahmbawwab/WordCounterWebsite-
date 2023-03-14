from django import views
from django.urls import path
from . import views

"""
     list of urls, path to configure each url 
     empty path '' mean main website with /marah means websitepath/marah
     views in views.py file
"""
urlpatterns = [
    # name id for this path, we go to views file and find index function or class and execute, render what exist inside it
    path('', views.index, name='index'),
    path('counter', views.countword, name='counter')
]
