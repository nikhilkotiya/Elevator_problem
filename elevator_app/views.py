from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .elevator_logic import ElevatorController 
from .models import Building,Elevator,ElevatorRequest
from .serializer import *
from .constants import RunningStatus

class ElevatorSystemList(viewsets.ModelViewSet):
  '''
  Fetch all the listed elevator systems.
  '''
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.building = Building()
  queryset = Building.objects.all()
  serializer_class = BuildingSerializer
  
  def perform_create(self, serializer):
        serializer.save()
        self.building.create_elevators(
        number_of_elevators=serializer.data['number_of_elevators'],
        building_id=serializer.data['id']
        )


class Elevator_(viewsets.ModelViewSet):
  queryset = Elevator.objects.all()
  serializer_class = ElevatorSerializer

elevators = {}


class ElevatorRequestView(APIView):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):
      serializer = ElevatorRequestSerializer(data=request.data)
      if serializer.is_valid():
        building_id = serializer.validated_data['building_id']
        destination_floor = serializer.validated_data['destination_floor']
        source_floor = serializer.validated_data['source_floor']
        try:
          building_obj = Building.objects.get(id=building_id)
        except Building.DoesNotExist:
          return Response("Building not found", status=404)
        if destination_floor > building_obj.max_floor:
          return Response("Destination floor should be less than max floor", status=400)
        
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
            return Response("Request sent successfully", status=200)
        else:
           return Response("No elevator found", status=400)
      else:
        return Response(serializer.errors, status=400)