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
    # URL for the index of existing tickets
    url(r'^$', views.TicketIndex.as_view(), name='index'),

    # URL for the index of closed tickets
    url(r'closed/$', views.ClosedTicketIndex.as_view(), 
        name='closed'),

    # URL for a blank form for a new ticket
    url(r'newForm/$', views.create_ticket, name='newForm'),

    # Post the new ticket to the database 
    url(r'create_ticket/', views.create_ticket, name='create_ticket'),

    # Display the details of an existing ticket with bound data
    url(r'^(?P<pk>[0-9]+)/form/$', views.open_ticket, name='form'),

    # Post updated data from an existing ticket
    url(r'^(?P<pk>[0-9]+)/update/$', views.open_ticket, name='update'),

    # This URL will redirect users to a thank you page after submitting a
    # ticket or updating a ticket
    url(r'thanks/$', views.thanks, name='thanks'),

            ]
