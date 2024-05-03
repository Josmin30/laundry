from django.test import TestCase
from ewebApp.models import Customer
# Create your tests here.
class CustomerTest(TestCase):
    def setup(self):
        Customer.objects.Create(name="Jerry",phone=9809865421,email="jerry@gmail.com",password="jerry@1234")
    def test_Customer_password(self):
        Jerry = Customer.objects.get(name='Jerry')
        self.assertEqual(Jerry.password,'jerry@1234')