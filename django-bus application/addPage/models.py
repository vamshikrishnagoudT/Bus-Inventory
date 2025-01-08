from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_number = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100)
    no_of_seats = models.PositiveIntegerField()
    trip = models.CharField(max_length=200)
    trip_duration = models.DurationField()
    conductor = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bus_number} - {self.trip}"