from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Document (models.Model):
    """
    This model is for a document that will be held in the file system. The
    model needs to hold the path to the file and some data about it.
    """
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
