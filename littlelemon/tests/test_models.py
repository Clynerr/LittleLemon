from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest (TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="Truffles", price=15, inventory=7)
        self.assertEqual(item, "Truffles : 15")

