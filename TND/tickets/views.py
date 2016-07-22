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


# Create your views here.


class TicketIndex(generic.ListView):
    template_name = "tickets/index.html"
    context_object_name = "open_ticket_list"

    def get_queryset(self):
        """
        Return all the tickets.
        """
        return Ticket.objects.order_by('pub_date')


class DetailsView(generic.DetailView):
    """
    Used for overview of the ticket status.
    """
    model = Ticket
    template_name = "tickets/details.html"


# This class view is intended to be used with the create_ticket function.
class InitialForm(generic.TemplateView):
    """
    Used to create the ticket and provide preliminiary information
    """
    model = Ticket
    context_object_name = "open_ticket_list"
    template_name = "tickets/initial.html"


def create_ticket(request, Ticket):
    """
    This method is used to create a ticket then display the details 
    page for the associated ticket.
   
    """
    model = Ticket
    Ticket.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("tickets:details", args=(ticket.id,)))
