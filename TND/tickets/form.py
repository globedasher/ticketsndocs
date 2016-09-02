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
from django.forms import ModelForm, Textarea, SelectDateWidget

from .models import Ticket


# Create your forms here.

# This class is used to display a new ticket form, but only fields for
# reporting an issue and not other fields used for corrective action.
class NewForm(ModelForm):
    # TODO: Add requried fields for all fo the fields on a new ticket.
    class Meta:
        model = Ticket
        fields = ['pub_date', 
                  'document_number', 
                  'comments_for_revision',
                  'reported_by', 
                  'reported_by_email', 
                  'url_of_issue',
                  'pic_of_issue',
                  'revision', 
                  ]
        # The following section defines the widgets used for fields on the
        # form.
        widgets = {
                'pub_date': SelectDateWidget(),
                'comments_for_revision': 
                      Textarea(attrs={'cols':50, 'rows':10}),
                  }

# This class is used to display all available fields for the open ticket to
# allow a representative to perform corrective action and document it in the
# tickets system.
class DetailForm(ModelForm):

    # TODO: Insert errors when a single field is chosen for the close date and
    # no other fields are selected. 
    class Meta:
        model = Ticket
        fields = ['eng', 
                  'eng_email', 
                  'eng_comments',
                  'confirmed',
                  'close_date',
                  ]
        # The following section defines the widgets used for fields on the
        # form.
        widgets = {
                'eng_comments':
                    Textarea(attrs={'cols':50, 'rows':10}),
                'close_date': SelectDateWidget(),
                  }
