from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ElevatorManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)