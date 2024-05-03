from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    section = models.CharField(max_length=20 ,null=True)
    salary = models.IntegerField()
    password = models.CharField(max_length=10)
class Employee(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    section = models.CharField(max_length=20,null=True)
    phone = models.IntegerField()
    salary = models.IntegerField()
    password = models.CharField(max_length=10)
class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(max_length=20,null=True)
    password = models.CharField(max_length=10,null=True)
class Order(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date = models.DateField()
    quantity = models.IntegerField()
    details = models.CharField(max_length=20) 
    # status = models.CharField(max_length=20)
    # progress = models.CharField(max_length=20 ,null=True)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    message = models.CharField(max_length=20)

