"""tickets app urls.py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.conf.urls import url, include

from . import views

# The following app_name provides a name to reference in the namespace...
# or something. I'm still learning Django.
app_name = "docs"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'upload_center/$', views.upload_center, name='upload_center'),
    url(r'upload/$', views.upload, name='upload'),
    url(r'records/$', views.records, name='records'),
]
