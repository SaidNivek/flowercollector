from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

YES_NO = (
    (
        ('Y', 'Yes'),
        ('N', 'No')
    )
)

WATER_TIMES = (
    (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening')
    )
)

# Create your models here.
class Garden(models.Model):
    name = models.CharField(max_length=50)
    length = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return f'{self.name} is {self.width} feet wide and {self.length} feet long.'
    
    def get_absolute_url(self):
        return reverse ('gardens_detail', kwargs={'pk': self.id})

class Flower(models.Model):
    name = models.CharField(max_length=100)
    plantType = models.CharField(max_length=100)
    bloom = models.TextField(max_length=250)
    height = models.CharField(max_length=100)
    spacing = models.CharField(max_length=100)
    hardiness = models.CharField(max_length=100)
    pinch = models.CharField(max_length=100)   
    deerResistant = models.CharField(
        'Deer Resistant', max_length=1,
        choices=YES_NO,
        default=YES_NO[0][0]
    )
    gardens = models.ManyToManyField(Garden)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"This flower is called {self.name} and is in the family of {self.plantType}."
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'flower_id': self.id})
    
    def watered_today(self):
        return self.watering_set.filter(date=date.today()).count() >= 1
    
class Watering(models.Model):
    date = models.DateField('watering date')
    time = models.CharField(
        max_length=1,
        choices=WATER_TIMES,
        default=WATER_TIMES[0][0]
    )

    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} watering on {self.date}."
    
    # Change the default sort, most recent dates at the top
    class Meta:
        ordering=['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"

