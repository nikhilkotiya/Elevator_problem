import time
import threading
from .models import Elevator
import time
from queue import Queue
from .constants import RunningStatus
from .redis_utils import RedisUtils


class ElevatorController(threading.Thread):
    '''
    Elevator thread class. Each elevator is represented as a separate thread
    '''

    def __init__(self, elevator_id, initial_floor, building_id, min, max):
        '''
        Constructor function for the Elevator class. Initializes the Elevator with a given id
        and starting floor, and also creates a queue to store pending requests.
        '''
        super().__init__()
        self.elevator_id = elevator_id
        self.current_floor = initial_floor
        self.building_id = building_id
        self.queue = Queue()
        self.is_running = False
        self.is_door_open = False
        self.min = min
        self.redis_utils = RedisUtils()
        self.arr = [0] * (max-min)

    def update_running_staus(self, elevator_status,):
        elevator_status["running_status"] = self.running_status
        self.redis_utils.add_to_hash_map_set(self.elevator_id, elevator_status)

    def update_door(self, elevator_status,):
        elevator_status["is_door_open"] = int(self.is_door_open)
        self.redis_utils.add_to_hash_map_set(self.elevator_id, elevator_status)

    def update_current_floor(self, elevator_status,):
        elevator_status["current_floor"] = self.current_floor
        self.redis_utils.add_to_hash_map_set(self.elevator_id, elevator_status)

    def run(self):
        '''
        Run function for the Elevator thread. This function keeps the elevator moving between floors
        until the queue is empty.

        Not removing comments so that we can see what is happening in elevator thread

        first check wheather we have value in a queue or not. if have then we check we passed this floor in the 
        middle of the journy after requested. If yes then we remove that request.
        '''
        self.is_running = True
        while self.is_running:
            # Check if there are any pending requests in the queue
            if not self.queue.empty():
                request = self.queue.get()
                if self.arr[request.destination_floor - self.min] == 0:
                    #removing the request becuase it is aleady reached in between the journy.
                    request.delete()
                    continue

                if request.destination_floor > self.current_floor:
                    self.running_status = RunningStatus.GOING_UP.value
                else:
                    self.running_status = RunningStatus.GOING_DOWN.value

                elevator_status = {
                    "current_floor": self.current_floor,
                    "is_door_open": int(self.is_door_open),
                    "running_status": self.running_status
                }
                # Save the current status of the elevator in Redis
                self.redis_utils.add_to_hash_map_set(
                    self.elevator_id, elevator_status)

                elevator = Elevator.objects.get(id=self.elevator_id)
                elevator.is_busy = True
                elevator.running_status = self.running_status
                elevator.save()
                self.update_running_staus(elevator_status)
                elevator = Elevator.objects.get(id=self.elevator_id)
                elevator.running_status = self.running_status
                elevator.save()
                while self.current_floor != request.destination_floor:
                    # Check when this request is in the queue if yes the we take it as a stop and mark arr[index]=0
                    if self.arr[self.current_floor - self.min] == 1:
                        print("door open")
                        self.is_door_open = True
                        self.update_door(elevator_status)
                        time.sleep(2)
                        # Close the elevator doors
                        self.is_door_open = False
                        self.update_door(elevator_status)
                        self.arr[self.current_floor - self.min] = 0
                        print("door close")
                    # taking time for 2 seconds to move to next floor
                    time.sleep(2)
                    self.current_floor += 1 if self.running_status == RunningStatus.GOING_UP.value else -1
                    print(
                        f"Elevator {self.elevator_id} is at floor {self.current_floor} and destination {request.destination_floor} .")
                    self.update_current_floor(elevator_status)

                self.arr[self.current_floor - self.min] = 0
                self.running_status = RunningStatus.STANDING_STILL.value
                self.update_running_staus(elevator_status)
                # Open the elevator doors
                print("door open")
                self.is_door_open = True
                self.update_door(elevator_status)
                # Wait for some time to simulate the elevator doors being open
                time.sleep(2)
                # Close the elevator doors
                self.is_door_open = False
                self.update_door(elevator_status)
                print("door close")
                elevator.current_floor = self.current_floor
                elevator.running_status = self.running_status
                elevator.is_busy = False
                elevator.save()
                # Mark the request as completed in the database
                request.delete()
            else:
                # wait for 1 second before checking the queue again
                time.sleep(2)

    def add_request(self, request):
        '''
        Function to add a new request to the elevator's queue Also using an array for optimising
        marking the arr[index] = 1 and - self.min is used because of underground floor of Elevator
        '''
        index = request.destination_floor - self.min
        self.arr[index] = 1
        self.queue.put(request)
        print(f"Request added to Elevator {self.elevator_id} queue: {request}")
