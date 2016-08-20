"""
This is the views.py file for Tickets 'n Docs.

By Richard Morley
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Ticket
from .form import DetailForm


# Create your views here.


# This class view shows all the tickets that are currently open and provides
# a portal to create more tickets.
class TicketIndex(generic.ListView):
    template_name = "tickets/index.html"
    context_object_name = "open_ticket_list"

    def get_queryset(self):
        """
        Return all the tickets.
        """
        return Ticket.objects.order_by('id') 


# This class view shows the details of a pre-existing ticket in an editable
# format.
class DetailsView(generic.DetailView):
    """
    Used for overview of the ticket status.
    """
    model = Ticket
    template_name = "tickets/details.html"


def create_ticket(request):
    # This function is used to display a blank form for data input and to
    # accept post data from the blank form.
    # If a POST reqest, we need to process the form data
    if request.method == 'POST':
        # Create a new form instance and populate it with data from the request
        form = DetailForm(request.POST)
        # Check if the data is valid
        if form.is_valid():
            # Process the cleaned data and place it in the ticket elements then
            # save it to the database. 
            tick = Ticket(form.cleaned_data['pub_date'], 
                          form.cleaned_data['document_number'],
                          form.cleaned_data['comments_for_revision'],
                          form.cleaned_data['writer'], 
                          form.cleaned_data['writer_email'],
                          form.cleaned_data['editor'],
                          form.cleaned_data['editor_email'],
                          form.cleaned_data['major_revision'],
                          form.cleaned_data['minor_revision'],
                          )
            print(tick.pk)
            tick.save()
            print(tick.pk)
            # Redirect to a new URL
            return HttpResponseRedirect('/tickets/thanks/')

    # If GET or any other method, present a blank form.
    else:
        form = DetailForm()

    return render(request, 'tickets/newForm.html', {'form':form})

def open_ticket(request, pk):
    # This function is used to render a bound form with existing data.
    if request.method == 'POST':
        # Create a new form instance and populate it with data from the request
        form = DetailForm(request.POST)
        # Check if the data is valid
        if form.is_valid():
            tick = Ticket(form.cleaned_data['pub_date'], 
                          form.cleaned_data['document_number'],
                          form.cleaned_data['comments_for_revision'],
                          form.cleaned_data['writer'], 
                          form.cleaned_data['writer_email'],
                          form.cleaned_data['editor'],
                          form.cleaned_data['editor_email'],
                          form.cleaned_data['major_revision'],
                          form.cleaned_data['minor_revision'],
                          )
            print(tick)
            tick.save()
            # Process the data in form.clean_data
            #
            # Redirect to a new URL
            return HttpResponseRedirect('/tickets/thanks/')

    # If GET or any other method, present a blank form.
    else:
        ticket = Ticket.objects.get(pk=pk)
        form = DetailForm(instance=ticket)

    return render(request, 'tickets/form.html', {'form':form})

def thanks(request):
    """
    Used to thank the user for inputting a ticket.
    """
    return render(request, 'tickets/thanks.html')
