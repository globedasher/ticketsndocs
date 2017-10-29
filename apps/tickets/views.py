"""
This is the views.py file for Tickets 'n Docs.

By Richard Morley
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Ticket


# Create your views here.

def index(request):
    print(request.user)
    print(request.user.id)
    print(request.user.first_name)
    open_tickets = Ticket.objects.select_related().filter(close_date__isnull=True)
    context = {"open_ticket_list": open_tickets}
    return render(request, "tickets/index.html", context)



# This class view shows all the tickets that are closed
class ClosedTicketIndex(generic.ListView):
    template_name = "tickets/closed.html"
    context_object_name = "closed_ticket_list"

    def get_queryset(self):
        """
        Return all the tickets.
        """
        # The following get the ticket objects from the database that exist but
        # do not have a close date to populate the currently open ticket list.
        # This list is then ordered by id number.
        closed_tickets = Ticket.objects.filter(close_date__isnull=False)
        context = closed_tickets.order_by('id')
        return context


def create_ticket(req):
    # This function is used to display a blank form for data input and to
    # accept post data from the blank form.
    # If a POST reqest, we need to process the form data
    if req.method == 'POST':
        print(req.POST['pic_of_issue'])
        print(req.user)
        tick = Ticket(document_number = req.POST['document_number'],
                  reported_by = req.user,
                  comments_for_revision = req.POST['comments_for_revision'],
                  url_of_issue = req.POST['url_of_issue'],
                  pic_of_issue = req.POST['pic_of_issue'],
                  revision = req.POST['revision'],
               )
        tick.save()
        # Redirect to a new URL
        return HttpResponseRedirect('/tickets/thanks/')

    # If GET or any other method, present the blank form.
    else:
        return render(req, 'tickets/newForm.html')

def open_ticket(request, pk):
    # This function is used to render a bound form with existing data to update
    # an existing ticket. 
    if request.method == 'POST':
        # The following code will save altered data to an existing ticket.
        form = DetailForm(request.POST)
        # Check if the data is valid
        if form.is_valid():
            # Process the data from the form
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
        context = {'ticket':ticket}
        # The following renders the form with the above contextual data.
        return render(request, 'tickets/form.html', context)

# The folling definition displays a thank you page
def thanks(request):
    """
    Used to thank the user for inputting a ticket.
    """
    return render(request, 'tickets/thanks.html')
