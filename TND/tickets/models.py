"""
This is the models.py file for Tickets n' Docs. This is great! Get it on!
"""
import datetime


from django.db import models
from django.utils import timezone


# Create your models here.


class Ticket(models.Model):
    
    """ 
    This class builds a ticket for documentation update or a new document.
    The ticket will be assigned to an agent of the team to complete. Once the
    ticket has been addressed by the writer, an editor will be assigned to
    review the documentation. The editor will markup changes and pass it back
    to the writer until they agree it can be released.  
    """
    pub_date = models.DateTimeField("Date published")
    document_number = models.CharField(max_length=8)
    comments_for_revision = models.CharField(max_length=400)
    writer = models.CharField(max_length=50)
    writer_email = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)
    editor_email = models.CharField(max_length=50)
    close_date = models.DateTimeField("Date closed")
    # major_revision will only be incremented when a release is posted. It will
    # remain a zero until that point. (0.1, 0.2,... 1.0)
    major_revision = models.CharField(max_length=2)
    # minor_revision will be incremented with each file commit.
    minor_revision = models.CharField(max_length=2)

    def __str__(self):
        """ 
        When requested, return the ticket number.
        """
        return self.document_number
