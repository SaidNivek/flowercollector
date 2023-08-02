from django.db import models

# Create your models here.
class Flower(models.Model):
    name: models.CharField(max_length=100)
    plantType: models.CharField(max_length=100)
    bloom: models.TextField(max_length=250)
    height: models.IntegerField()
    spacing: models.IntegerField()
    pinch: models.CharField(max_length=100)   
    deerResistant: models.BooleanField()
    image: models.CharField(max_length=100)