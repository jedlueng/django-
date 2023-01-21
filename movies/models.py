from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model): 
    #attribute for name str 
    name = models.CharField(max_length=255)


class Movie(models.Model): 
    # INT FLOAT
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField() 
    #IF delete delete all objects 
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    date_created = models.DateTimeField(default= timezone.now) 