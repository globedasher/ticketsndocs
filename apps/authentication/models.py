from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}')

# Create your models here.
