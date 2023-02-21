from django.db import models
from .choese import ch,classes,gender,cast

# Create your models here.
class MoviesModel(models.Model):
    name = models.CharField(max_length=100)
    choiese = models.CharField(max_length=20,choices=ch,default="ch")
    date = models.DateField()
    classes = models.CharField(max_length=20,choices=classes)
    rating = models.DecimalField(decimal_places=2,max_digits=4)
    gender = models.CharField(max_length=20,choices=gender)
    storyline = models.TextField()
    cast_on = models.CharField(max_length=50,choices=cast)