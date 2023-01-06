from django.db import models

# Create your models here.

class Contact(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.EmailField()
    Phone=models.CharField(max_length=10)
