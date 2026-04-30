from django.test import TestCase
from .models import Product
class ProductTest(TestCase):
    def test_create(self):
        p = Product.objects.create(name='Laptop', prices=50000)
        self.assertEqual(p.name, 'Laptop')
