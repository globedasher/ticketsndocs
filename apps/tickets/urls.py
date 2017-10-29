"""tickets app urls.py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

# The following app_name provides a name to reference in the namespace...
# or something. I'm still learning Django.
app_name = "tickets"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'closed/$', views.ClosedTicketIndex.as_view(), name='closed'),
    url(r'newForm/$', views.create_ticket, name='newForm'),
    url(r'create_ticket/', views.create_ticket, name='create_ticket'),
    url(r'^(?P<pk>[0-9]+)/form/$', views.open_ticket, name='form'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.open_ticket, name='update'),
    url(r'thanks/$', views.thanks, name='thanks'),
]
