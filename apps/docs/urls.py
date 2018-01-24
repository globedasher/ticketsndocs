"""tickets app urls.py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.urls import include, path

from . import views

# The following app_name provides a name to reference in the namespace...
# or something. I'm still learning Django.
app_name = "docs"
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'upload_center/', views.upload_center, name='upload_center'),
    path(r'upload/', views.upload, name='upload'),
    path(r'records/', views.records, name='records'),
    path(r'details/<int:item_id>', views.details, name='details'),
]
