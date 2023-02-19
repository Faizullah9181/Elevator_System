from django.contrib import admin
from .models import Building, Elevator , ElevatorOperations

# Register your models here.

admin.site.register(Building)
admin.site.register(Elevator)
admin.site.register(ElevatorOperations)
