from django.test import TestCase
from .models import Product
class ProductTest(TestCase):
    def test_create(self):
        p = Product.objects.create(name='Lapto1p', price=5000)
        self.assertEqual(p.name, 'Laptop')
