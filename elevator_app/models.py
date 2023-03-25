from django.db import models

class Elevator(models.Model):
    id = models.IntegerField(primary_key=True)
    floor = models.IntegerField(default=0)
    direction = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    is_working = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

class Request(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    direction = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
