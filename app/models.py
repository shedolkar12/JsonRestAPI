from django.db import models
from django.contrib import admin

class Provider(models.Model):
    provider_id=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    currency=models.CharField(max_length=50)
    def __str__(self):
        return self.email

# Create your models here.
