from django.db import models
import os
from django_resized import ResizedImageField
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    dateAdded = models.DateTimeField(auto_now=True)
    img = ResizedImageField( size=[200,200], upload_to='', quality=100, blank=True, null=True)
    description = models.CharField(max_length=500,blank=True)