from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=200)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/', null=True)

class Director(models.Model):
    name=models.CharField(max_length=200)    