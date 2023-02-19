from django.db import models
from django.contrib.auth.models import User



class Building(models.Model):
    floors = models.IntegerField(default=3)
    elevators = models.IntegerField(default=1)


class Elevator(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)



class ElevatorOperations(models.Model):

    class PRESS_BUTTON(models.TextChoices):
        TOP = 'TOP'
        BOTTOM = 'BOTTOM'
        FLOOR = 'FLOOR'
    class status(models.TextChoices):
        REACHED = 'REACHED'
        MOVING = 'MOVING'
        IDLE = 'IDLE'

        

    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    current_floor = models.IntegerField(default=1)
    current_status = models.CharField(max_length=20, choices=status.choices, default=status.IDLE)
    button_pressed = models.CharField(max_length=20, choices=PRESS_BUTTON.choices, default=PRESS_BUTTON.BOTTOM)
    requests = models.ManyToManyField(User, related_name='requests')