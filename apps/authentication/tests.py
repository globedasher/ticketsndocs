from django.test import TestCase

from . import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your tests here.

class MyTestCase(TestCase):
    def setUp(self):
        self.aldo = "Team test!"
        user = User.objects.create_user(
                   "testname",
                   "test@email.com",
                   "Password1!",
               )
        user.save()

    def test_this(self):
        """Identify stuff just created."""
        print("Test This")
        print(views.users(req))
        self.assertEqual(self.aldo, "Team test!")

