from django.db import models
import datetime as dt
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    location_name=models.CharField(max_length=30,unique=True)
    
    def __str__(self):
        return self.location_name
   
    def save_location(self):
        self.save()
       
class Category(models.Model):
    category_name = models.CharField(max_length=40,unique=True)
   
def __str__(self):
    return self.category_name
   
def save_category(self):
    self.save()
       
