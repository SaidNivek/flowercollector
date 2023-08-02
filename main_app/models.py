from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    plantType = models.CharField(max_length=100)
    bloom = models.TextField(max_length=250)
    height = models.CharField(max_length=100)
    spacing = models.CharField(max_length=100)
    hardiness = models.CharField(max_length=100)
    pinch = models.CharField(max_length=100)   
    deerResistant = models.BooleanField()
    image = models.TextField(max_length=1000)

    def __str__(self):
        return f"This flower is called {self.name} and is in the family of {self.plantType}."