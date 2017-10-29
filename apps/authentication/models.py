from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}')

# Create your models here.

class UserManager(models.Manager):

    def login(self, email, password):
        errors = []

        # password validations
        if not password:
            errors.append("Please enter a password.")

        if not errors:
            # Get the user object and check the password (hashed through
            # bcrypt)
            try:
                user = User.objects.get(email=email)
                encoded_hash = user.pw_hash.encode('utf-8')
                encoded_pw = password.encode('utf-8')
                if bcrypt.hashpw(encoded_pw, encoded_hash) == encoded_hash:
                    return (True, user)
                else:
                    errors.append("Password incorrect.")
                    return (False, errors)
            except:
                errors.append("Please register this email address.")
                return(False, errors)
        else:
            return (False, errors)


    def register(self, *args):
        first_name = args[0]['first_name']
        last_name = args[0]['last_name']
        password = args[0]['password']
        password2 = args[0]['password2']
        email = args[0]['email']

        errors = []
        # Build validations here

        # first_name validations
        if not first_name:
            errors.append("First name must exist.")
        elif not first_name.isalpha():
            errors.append("First name must contain letters only.")
        elif len(first_name) < 2:
            errors.append("First name must be longer than two characters.")

        # last_name validations
        if not last_name:
            errors.append("Last name must exist.")
        elif not last_name.isalpha():
            errors.append("Last name must contain letters only.")
        elif len(last_name) < 2:
            errors.append("Last name must be longer than two characters.")

        # email validations
        if not email:
            errors.append("Please enter an email address.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid email address.")

        # password validations
        if not password or not password2:
            errors.append("Please enter a password and confirmation.")
        if not password == password2:
            errors.append("Passwords do not match.")
        elif not PASSWORD_REGEX.match(password):
            errors.append("Password must include one capital, one number and eight characters")
        if not errors:
            encoded_pw = password.encode('utf-8')
            pw_hash = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
            user = User(first_name=first_name
                    ,last_name=last_name
                    ,pw_hash=pw_hash
                    ,email=email) 
            user.save()
            return (True, user)
        else:
            return (False, errors)


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    pw_hash = models.CharField(max_length=256)
    objects = UserManager()
