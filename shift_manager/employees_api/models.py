from django.db import models
# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    age = models.IntegerField()
    title = models.CharField(max_length=32)
    pay = models.IntegerField()

class Posts(models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=300)

