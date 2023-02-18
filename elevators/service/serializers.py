from .models import Building, Elevator
from rest_framework import serializers



class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['id','floors', 'elevators']


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['id', 'building', 'current_floor', 'is_moving', 'is_door_open', 'is_active', 'is_reached_top', 'is_reached_bottom', 'requests']