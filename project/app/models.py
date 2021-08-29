import email
import re
from django.db import models

# Create your models here.

class Vendors(models.Model):
    name=models.CharField(
        max_length=50,
        blank=False,
        unique=True,
    )
    email=models.EmailField()
    website=models.URLField()

class Recipes(models.Model):
    name=models.CharField(max_length=50)
    ingrdients=models.CharField(default=any, max_length=50)
    submitted_by=models.ManyToManyField(Vendors, related_name='Vendors')



    
