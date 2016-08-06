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
        return Ticket.objects.order_by('pub_date')


# This class view shows the details of a pre-existing ticket in an editable
# format.
class DetailsView(generic.DetailView):
    """
    Used for overview of the ticket status.
    """
    model = Ticket
    template_name = "tickets/details.html"


# This function is supposed to save changes to a ticket from the Details
# view. I changed the function name to keep for debugging against methods 
# called save().
def keep(request, ticket_id):
    print(request)
    print(ticket_id)
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    #try:
    updated_info = ticket.objects.get(pk=request.POST["document_number"])
    #except(KeyError, ticket.DoesNotExist):
        # Redisplay the details page if there is an error
        #return render(request, 'tickets/details.html', {
            #'ticket':ticket,
            #'error_message': "Something didn't work",
            #})
    #else:
    updated_info.save()
    return HttpResponseRedirect(reverse(
                                    "tickets:index", args=(ticket.id,)))



def get_name(request, ticket_id=None):
    # If this is a POST  request, we need to process the form data.
    print(request)
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        # Check if it's valid.
        #if ticket.is_valid():
            # Um... They said something about form.cleaned_data as required
            # I don't know what that means.
            # Redirect to new URL
        return HttpResponseRedirect(reverse("tickets:index"))
        # If GET or other method, present blank form
        #else:
            #ticket = DetailsView()

        #return render(request, "details.html", {"ticket":ticket})
