"""
This is the models.py file for Tickets n' Docs. This is great! Get it on!
"""
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Ticket(models.Model):

    """
    This class builds a ticket for documentation update or a new document.
    The ticket will be assigned to an agent of the team to complete. Once the
    ticket has been addressed by the writer, an editor will be assigned to
    review the documentation. The editor will markup changes and pass it back
    to the writer until they agree it can be released.
    """
    # TODO: Improve Ticet model to reflect more functions for support teams.
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(max_length=100, default=timezone.now)
    document_number = models.CharField(max_length=30)
    comments_for_revision = models.CharField(max_length=500)
    url_of_issue = models.CharField(max_length=200, blank=True)
    pic_of_issue = models.FileField(blank=True)
    # major_revision will only be incremented when a release is posted. It will
    # remain a zero until that point. (0.1, 0.2,... 1.0)
    revision = models.CharField(max_length=4, blank=True)
    confirmed = models.BooleanField(default=False, blank=True)
    close_date = models.DateField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        When requested, return the document_number.
        """
        return self.document_number

    def was_published_recently(self):
        """
        This function will determine if a ticket has been published in the last
        day.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Note(models.Model):
    """
    This class is used to create notes for each ticket. This will be a many
    (notes) to one (ticket).
    """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    eng = models.ForeignKey(User, on_delete=models.CASCADE)
    eng_comments = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
