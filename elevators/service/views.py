from django.shortcuts import render
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from .models import Building, Elevator,ElevatorOperations
from .serializers import BuildingSerializer, ElevatorSerializer , ElevatorOperationsSerializer
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
    user = request.user
    building_id = request.data['building_id']
    building = Building.objects.get(id=building_id)
    elevator = Elevator.objects.create(
        building=building,
        created_by=user,
        created_at=datetime.now()
    )

    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_elevator(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    serializer = ElevatorSerializer(elevator, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_elevator(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    elevators_operations = ElevatorOperations.objects.filter(elevator=elevator)
    if elevators_operations:
        elevator_operations = elevators_operations[0]
        elevator_operations.requests.add(request.user)
        elevator_operations.save()
        serializer = ElevatorOperationsSerializer(elevator_operations, many=False)
        return Response(serializer.data)
    else:
        elevator_operations = ElevatorOperations.objects.create(
            elevator=elevator,
            current_floor=1,
            current_status='IDLE',
            button_pressed='BOTTOM'
        )
        elevator_operations.requests.add(request.user)
        elevator_operations.save()
        serializer = ElevatorOperationsSerializer(elevator_operations, many=False)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def press_button(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    elevators_operations = ElevatorOperations.objects.filter(elevator=elevator)
    if elevators_operations:
        elevator_operations = elevators_operations[0]
        if elevator_operations.current_status == 'IDLE':
            elevator_operations.button_pressed = request.data['button_pressed']
            elevator_operations.save()
            serializer = ElevatorOperationsSerializer(elevator_operations, many=False)
            return Response(serializer.data)
        else:
            return Response('Elevator is busy')
    else:
        return Response('Elevator is busy')
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_status(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    elevator_operations = ElevatorOperations.objects.get(elevator=elevator)
    serializer = ElevatorOperationsSerializer(elevator_operations, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_requests(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    elevator_operations = ElevatorOperations.objects.get(elevator=elevator)
    serializer = UserSerializer(elevator_operations.requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_elevator_manager(request):
    elevator_id = request.data['elevator_id']
    elevator = Elevator.objects.get(id=elevator_id)
    created_by = elevator.created_by
    serializer = UserSerializer(created_by, many=False)
    return Response(serializer.data)
