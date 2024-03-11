from django.test import TestCase
from restaurant.views import MenuItemView, BookingViewSet, SingleMenuItemView
from restaurant.models import Menu, Booking

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Food1", price=10.00, inventory=15)
        Menu.objects.create(title="Food2", price=5, inventory=150)
    

    
