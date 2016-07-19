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
    model = Ticket
    template_name = "tickets/details.html"

# This class view is intended to be used with the create_ticket function.
class CreateTicket(generic.TemplateView):
    model = Ticket
    model_name = "ticket"
    template_name = "tickets/create.html"
