import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Ticket

# Create your tests here.

class TicketMethodTests(TestCase):

    def test_was_published_recently_with_future_ticket(self):
        """
        This test ensures any tickets published with a future date are not 
        added to the system.
        """
        
