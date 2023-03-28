from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .elevator_logic import ElevatorController
from .models import Building, Elevator, ElevatorRequest
from .serializer import *
from .utils import get_floor_distance
from .redis_utils import RedisUtils
from .constants import RunningStatus
elevators = {}

class BuildingView(viewsets.ModelViewSet):
    '''
    Crud for Building
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


class ElevatorView(viewsets.ModelViewSet):
    '''
    Crud for Elevator
    '''
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class ElevatorOutsideRequestView(APIView):

    serializer_class = ElevatorRequestOutsideSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_utils = RedisUtils()

    def post(self, request):
        '''
        function used when the user request for the Elevator from outside 
        we calculated the elevator which is minimum distance from this floor
        '''
        serializer = ElevatorRequestOutsideSerializer(data=request.data)
        if serializer.is_valid():
            building_id = serializer.validated_data['building_id']
            user_destination_floor = serializer.validated_data['destination_floor']
            try:
                building_obj = Building.objects.get(id=building_id)
            except Building.DoesNotExist:
                return Response("Building not found", status=status.HTTP_404_NOT_FOUND)

            if user_destination_floor > building_obj.max_floor: # check for maximum floor reached by the elevator
                return Response("Destination floor should be less than max floor", status=status.HTTP_400_BAD_REQUEST)

            if user_destination_floor < building_obj.min_floor: # check for minimum floor reached by the elevator
                return Response("Destination floor should be less than min floor", status=status.HTTP_400_BAD_REQUEST)

            elevator =  Elevator.objects.filter(
                building_id=building_id).exclude(running_status=RunningStatus.NOT_WORKING.value)
            
            user_elevator = -1
            min_elevator_current_position = -1
            min_distance = 1000 # consider the max floor is less then 1000
            for obj in elevator:
                lift_status = self.redis_utils.get_all_fields_value_from_map(obj.id)
                if not lift_status:
                    # If the status doesn't exist in cache, retrieve it from the database
                    current_floor = obj.current_floor
                else:
                    current_floor = lift_status['current_floor']
                current_lift_distance = get_floor_distance(user_destination_floor,int(current_floor))
                if current_lift_distance < min_distance:
                    user_elevator = obj.id
                    min_distance = current_lift_distance
                    min_elevator_current_position=current_floor

            if  user_elevator !=- 1 :#elevator_obj:
                elevator = elevators.get(user_elevator, None)
                if not elevator:
                    elevator = ElevatorController(
                        elevator_id=user_elevator, initial_floor=int(min_elevator_current_position), building_id=building_id, min=building_obj.min_floor, max=building_obj.max_floor)
                    elevators[user_elevator] = elevator

                request = ElevatorRequest(destination_floor=user_destination_floor)
                request.save()
                elevator.add_request(request)

                if not elevator.is_alive():# run the thread for ElevatorController if not running
                    elevator.start()

                return Response("Request sent successfully", status=status.HTTP_200_OK)
            else:
                return Response("No elevator found", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElevatorInsideRequestView(APIView):

    serializer_class = ElevatorRequestSerializer
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):
        '''
        function used when the user request for the Elevator to reach on the destination from inside the Elevator 
        '''
        serializer = ElevatorRequestSerializer(data=request.data)
        if serializer.is_valid():
            building_id = serializer.validated_data['building_id']
            destination_floor = serializer.validated_data['destination_floor']
            elevator_id = serializer.validated_data['elevator_id']
            try:
                building_obj = Building.objects.get(id=building_id)
            except Building.DoesNotExist:
                return Response("Building not found", status=404)
            if destination_floor > building_obj.max_floor: # check for maximum floor reached by the elevator
                return Response("Destination floor should be less than max floor", status=status.HTTP_400_BAD_REQUEST)

            if destination_floor < building_obj.min_floor: # check for minimum floor reached by the elevator
                return Response("Destination floor should be less than min floor", status=status.HTTP_400_BAD_REQUEST)
            try:
                elevator_obj = Elevator.objects.get(id=elevator_id)
            except Elevator.DoesNotExist:
                return Response("Elevator not found", status=404)
            if elevator_obj:
                # calling the ElevatorController
                if elevator_obj.id not in elevators:
                    elevators[elevator_obj.id] = ElevatorController(
                        elevator_id=elevator_obj.id, initial_floor=elevator_obj.current_floor, building_id=building_id, min=building_obj.min_floor, max=building_obj.max_floor)
                elevator = elevators[elevator_obj.id]
                request = ElevatorRequest(destination_floor=destination_floor)
                request.save()
                elevator.add_request(request)
                
                if not elevator.is_alive():# run the thread for ElevatorController if not running
                    elevator.start()
                return Response("Request sent successfully", status=200)
            
            else:
                return Response("No elevator found", status=400)
        
        else:
            return Response(serializer.errors, status=400)


class ElevatorStatus(APIView):

    serializer_class = ElevatorStatusSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_utils = RedisUtils()

    def post(self, request):
        serializer = ElevatorStatusSerializer(data=request.data)
        if serializer.is_valid():
            elevator_id = serializer.validated_data['elevator_id']
            try:
                elevator_obj = Elevator.objects.get(id=elevator_id)
            except Elevator.DoesNotExist:
                return Response("Elevator not found", status=404)

            # Retrieve the elevator status from Redis cache
            status = self.redis_utils.get_all_fields_value_from_map(
                elevator_id)
            is_busy = False
            if not status:
                # If the status doesn't exist in cache, retrieve it from the database
                current_floor = elevator_obj.current_floor
                is_door_open = elevator_obj.is_door_open
                running_status = elevator_obj.running_status
                is_busy = elevator_obj.is_busy
                print("is_busy",is_busy)
                elevator_status = {
                    "current_floor": int(current_floor),
                    "is_door_open": int(is_door_open),
                    "running_status": running_status
                }
                # Save the status in Redis cache for future requests
                self.redis_utils.add_to_hash_map_set(
                    str(elevator_id), elevator_status)

            else:
                current_floor = status['current_floor']
                is_door_open = status['is_door_open']
                running_status = status['running_status']
                if running_status == RunningStatus.GOING_DOWN.value or running_status == RunningStatus.GOING_UP.value: 
                    is_busy = True # this is just for the edge case of redis because we have not sotred print is_busy in redis, we have saved in db
            message = "data fectch successfully"
            data = {
                "current_floor": current_floor,
                "is_door_open": is_door_open,
                "running_status": running_status,
                "is_busy": is_busy
            }
            result = {
                'data': data,
                "message": message
            }
            return Response(result, status=200)
        else:
            return Response(serializer.errors, status=400)


