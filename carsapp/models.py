from django.db import models

# Create your models here.
class cars(models.Model):
    company = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    fueltype = models.CharField(max_length=200)
    year_of_realease = models.IntegerField()
    seat_capacity = models.IntegerField()