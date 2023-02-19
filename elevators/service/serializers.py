from .models import Building, Elevator , ElevatorOperations
from rest_framework import serializers



class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['id','floors', 'elevators']


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['id', 'building', 'created_at', 'created_by', 'is_active']


class ElevatorOperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorOperations
        fields = ['id', 'elevator', 'current_floor', 'current_status', 'button_pressed', 'requests']