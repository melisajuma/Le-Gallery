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
       
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_path = models.ImageField(upload_to = 'images/', default="")
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    mygalary_image = models.ImageField(upload_to = 'media/')
    date_posted = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.image_name
   
@classmethod
def get_all_images(cls):
        images = Image.objects.all()
        return images

