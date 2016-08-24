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
from .form import NewForm
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
        form = NewForm(request.POST)
        # Check if the data is valid
        if form.is_valid():
            # Process the cleaned data and place it in the ticket elements then
            # save it to the database. In this instance, the cleaned_data is a
            # dictionary from the form object. Each key presents the data
            # obtained from the form.
            tick = Ticket(pub_date = form.cleaned_data['pub_date'], 
                          document_number = form.cleaned_data['document_number'],
                          comments_for_revision = form.cleaned_data['comments_for_revision'],
                          reported_by = form.cleaned_data['reported_by'], 
                          reported_by_email = form.cleaned_data['reported_by_email'],
                          major_revision = form.cleaned_data['major_revision'],
                          minor_revision = form.cleaned_data['minor_revision'],
                          )
            tick.save()
            # Redirect to a new URL
            return HttpResponseRedirect('/tickets/thanks/')

    # If GET or any other method, present the blank form.
    else:
        form = NewForm()

    return render(request, 'tickets/newForm.html', {'form':form})

def open_ticket(request, pk):
    # This function is used to render a bound form with existing data to update
    # an existing ticket. 
    if request.method == 'POST':
        # The following code will save altered data to an existing ticket.
        form = DetailForm(request.POST)
        # Check if the data is valid
        if form.is_valid():
            # Process the data in form.clean_data
            target = Ticket.objects.get(pk=pk)
            tick = DetailForm(request.POST, instance=target)
            tick.save()
            # Redirect to a 'thanks' URL to inform the user the input has been
            # received.
            return HttpResponseRedirect('/tickets/thanks/')

    # If GET or any other method, present a form with data from an exiting
    # ticket. 
    else:
        ticket = Ticket.objects.get(pk=pk)
        form = DetailForm(instance=ticket)
    
    # TODO: Get the ticket.id to be passed to the template when it is rendered.
    # The lack of this number being passed to the template is preventing the
    # POST functions above from saving the updated data back to the datbase.
    return render(request, 'tickets/form.html', {'form':form})

def thanks(request):
    """
    Used to thank the user for inputting a ticket.
    """
    return render(request, 'tickets/thanks.html')
