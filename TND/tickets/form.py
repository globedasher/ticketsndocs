"""
This is the form.py file for Tickets 'n Docs.

By Richard Morley
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django import forms

from .models import Ticket


# Create your forms here.


# This class view shows all the tickets that are currently open and provides
# a portal to create more tickets.
class DetailForm(forms.Form):
    your_name = forms.CharField(label="Your name:", max_length=100)
