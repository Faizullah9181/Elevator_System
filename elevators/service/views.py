from django.shortcuts import render
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from .models import Building, Elevator, ElevatorManager
from .serializers import BuildingSerializer, ElevatorSerializer, UserSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_elevators(request):
    elevators = Elevator.objects.all()
    serializer = ElevatorSerializer(elevators, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_elevator(request):
    data = request.data
    elevator = Elevator.objects.create(
        building_id=data['building'],
        current_floor=data['current_floor'],
        is_moving=data['is_moving'],
        is_door_open=data['is_door_open'],
        is_active=data['is_active'],
        is_reached_top=data['is_reached_top'],
        is_reached_bottom=data['is_reached_bottom'],
    )
    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)