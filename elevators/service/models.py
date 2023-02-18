from django.db import models
from django.contrib.auth.models import User


class Building(models.Model):
    floors = models.IntegerField(default=10)
    elevators = models.IntegerField(default=1)


class Elevator(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    current_floor = models.IntegerField(default=1)
    is_moving = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_reached_top = models.BooleanField(default=False)
    is_reached_bottom = models.BooleanField(default=False)
    requests = models.ManyToManyField(User , related_name='requests', blank=True)
