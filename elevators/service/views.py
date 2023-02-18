from django.shortcuts import render
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from .models import Building, Elevator
from .serializers import BuildingSerializer, ElevatorSerializer
from rest_framework.response import Response
from user.models import ElevatorManager
from user.serializers import UserSerializer
from datetime import datetime

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_building(request):
    data = request.data
    building = Building.objects.create(
        floors=data['floors'],
        elevators=data['elevators']
    )
    serializer = BuildingSerializer(building, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_elevator(request):
    data = request.data
    building_id = request.data['building_id']
    building = Building.objects.get(id=building_id)
    elevator = Elevator.objects.create(
        building=building,
        created_by=request.user,
        created_at=datetime.now()
    )

    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_elevator(request, pk):
    elevator = Elevator.objects.get(id=pk)
    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_elevator(request, pk):
    elevator = Elevator.objects.get(id=pk)
    elevator.requests.add(request.user)
    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def press_button(request, pk):
    elevator = Elevator.objects.get(id=pk)
    elevator.button_pressed = request.data['button_pressed']
    elevator.save()
    elevator.requests.add(request.user)
    elevator.save()
    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_status(request, pk):
    elevator = Elevator.objects.get(id=pk)
    if elevator.button_pressed == 'TOP':
        elevator.current_status = 'REACHED'
        elevator.save()
    elif elevator.button_pressed == 'BOTTOM':
        elevator.current_status = 'REACHED'
        elevator.save()
    elif elevator.button_pressed == 'FLOOR':
        elevator.current_status = 'REACHED'
        elevator.save()
    else:
        elevator.current_status = 'NO REQUEST'
        elevator.save()



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_requests(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    requests = elevator.requests.all()
    serializer = UserSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_elevator_manager(request):
    elevator_managers = ElevatorManager.objects.all()
    serializer = UserSerializer(elevator_managers, many=True)
    return Response(serializer.data)
