import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Ticket

# Create your tests here.

class TicketMethodTests(TestCase):

    def test_was_published_recently_with_future_ticket(self):
        """
        This test ensures any tickets published with a future date return a 
        False statement for was_published_recently()
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_ticket = Ticket(pub_date=time)
        self.assertEqual(future_ticket.was_published_recently(),False)
