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
from django.forms import ModelForm, Textarea

from .models import Ticket


# Create your forms here.

# This class is used to display a new ticket form, but only fields for
# reporting an issue and not other fields used for corrective action.
class NewForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['pub_date', 
                  'document_number', 
                  'comments_for_revision',
                  'reported_by', 
                  'reported_by_email', 
                  'major_revision', 
                  'minor_revision'
                  ]
        # The following section defines the widgets used for fields on the
        # form.
        widgets = {
                  'comments_for_revision': 
                      Textarea(attrs={'cols':50, 'rows':10}),
                  }

# This class is used to display all available fields for the open ticket to
# allow a representative to perform corrective action and document it in the
# tickets system.
class DetailForm(ModelForm):

    #confirmed = forms.BooleanField(required=False)
    #close_date = forms.DateField(required=False)

    class Meta:
        model = Ticket
        fields = ['pub_date', 
                  'document_number', 
                  'comments_for_revision',
                  'reported_by', 
                  'reported_by_email', 
                  'editor', 
                  'editor_email', 
                  'major_revision', 
                  'minor_revision',
                  'confirmed',
                  'close_date',
                  ]
        # The following section defines the widgets used for fields on the
        # form.
        widgets = {
                  'comments_for_revision': 
                      Textarea(attrs={'cols':50, 'rows':10}),
                  }
