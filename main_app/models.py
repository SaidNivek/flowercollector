from django.db import models
from django.urls import reverse

WATER_TIMES = (
    (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening')
    )
)

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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'flower_id': self.id})
    
class Watering(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=WATER_TIMES,
        default=WATER_TIMES[0][0]
    )

    cat = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} watering on {self.date}."