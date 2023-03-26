from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .elevator_logic import ElevatorController 
from .models import Building,Elevator,ElevatorRequest
from .serializer import BuildingSerializer,ElevatorSerializer,ElevatorRequestSerializer,ElevatorRequestSerializerAll


class ElevatorSystemList(viewsets.ModelViewSet):
  '''
  Fetch all the listed elevator systems.
  '''
  queryset = Building.objects.all()
  serializer_class = BuildingSerializer
  
  def perform_create(self, serializer):
        serializer.save()

        # Creating elevators needed for the system. For more details check create_elevators.py
        Building().create_elevators(
        number_of_elevators=serializer.data['number_of_elevators'],
        building_id=serializer.data['id']
        )


class Elevator_(viewsets.ModelViewSet):
  queryset = Elevator.objects.all()
  serializer_class = ElevatorSerializer

from enum import Enum
class RunningStatus(Enum):
    '''
    Choices for running status of the elevator system
    '''
    GOING_UP = 'going_up'
    STANDING_STILL = 'standing_still'
    GOING_DOWN = 'going_down'


elevators = {}


class ElevatorRequestView(APIView):

    def post(self, request):
        building_id = int(request.data.get('building_id'))
        destination_floor = int(request.data.get('destination_floor'))
        source_floor = int(request.data.get('source_floor'))
        try:
          building_obj = Building.objects.get(id=building_id)
        except Building.DoesNotExist:
          return Response("Given Elevator not found....")
        if destination_floor > building_obj.max_floor:
          return Response("destination_floor should be less then max_floor",status=400)
        
        elevator_obj = Elevator.objects.filter(building_id=building_id,running_status = RunningStatus.STANDING_STILL.value)
        if not elevator_obj:
           elevator_obj = Elevator.objects.filter(building_id=building_id)[0:1]
        
        if elevator_obj:
          elevator_obj = elevator_obj[0]
          if elevator_obj.id not in elevators:
            elevators[elevator_obj.id] = ElevatorController(elevator_id=elevator_obj.id, initial_floor=elevator_obj.current_floor, building_id=building_id)
          elevator = elevators[elevator_obj.id]
          request = ElevatorRequest(source_floor=source_floor, destination_floor=destination_floor)
          request.save()
          elevator.add_request(request)
          if not elevator.is_alive():
            elevator.start()
        else:
           return Response("no elivator found")    
        return Response("done")