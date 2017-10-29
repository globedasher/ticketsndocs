from django.test import TestCase

# Create your tests here.

class MyTestCase(TestCase):
    def setUp(self):
        self.aldo = "Team test!"

    def test_this(self):
        """Identify stuff just created."""
        self.assertEqual(self.aldo, "Team test!")

