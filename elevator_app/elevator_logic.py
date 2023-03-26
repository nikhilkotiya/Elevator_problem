import time
import threading
from .models import Elevator
import time
from queue import Queue
from .constants import RunningStatus

class ElevatorController(threading.Thread):
    '''
    Elevator thread class. Each elevator is represented as a separate thread
    '''

    def __init__(self, elevator_id, initial_floor, building_id):
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


    # def validate()
    def run(self):
        '''
        Run function for the Elevator thread. This function keeps the elevator moving between floors
        until the queue is empty.
        '''
        self.is_running = True
        while self.is_running:
            # Check if there are any pending requests in the queue
            if not self.queue.empty():
                request = self.queue.get()
                if request.source_floor == self.current_floor:
                  pass
                elif request.source_floor > self.current_floor:
                    self.running_status = RunningStatus.GOING_UP.value
                else:
                    self.running_status = RunningStatus.GOING_DOWN.value
                elevator = Elevator.objects.get(id = self.elevator_id)
                elevator.running_status = self.running_status
                elevator.save()
                # Move the elevator to the requested floor
                while self.current_floor != request.source_floor:
                    time.sleep(2)  # wait for 2 seconds to move to next floor
                    self.current_floor += 1 if self.running_status == RunningStatus.GOING_UP.value else -1
                    print(f"Elevator {self.elevator_id} is at floor {self.current_floor}. and source {request.source_floor}")
                # Open the elevator doors
                print("door open")
                self.is_door_open = True
                # Wait for some time to simulate the elevator doors being open
                time.sleep(2)
                # Close the elevator doors
                self.is_door_open = False
                print("door close")
                # Move the elevator to the destination floor
                if request.destination_floor > self.current_floor:
                    self.running_status = RunningStatus.GOING_UP.value
                else:
                    self.running_status = RunningStatus.GOING_DOWN.value
                
                elevator = Elevator.objects.get(id = self.elevator_id)
                elevator.running_status = self.running_status
                elevator.save()
                while self.current_floor != request.destination_floor:
                    time.sleep(2)  # taking time for 2 seconds to move to next floor
                    self.current_floor += 1 if self.running_status == RunningStatus.GOING_UP.value else -1
                    print(f"Elevator {self.elevator_id} is at floor {self.current_floor} and destination {request.destination_floor} .")
                # Open the elevator doors
                print("door open")
                self.is_door_open = True
                # Wait for some time to simulate the elevator doors being open
                time.sleep(2)
                # Close the elevator doors
                self.is_door_open = False
                print("door close")
                # Mark the request as completed in the database
                request.delete()
            else:
                # If there are no pending requests, set the elevator's running status to standing still
                self.running_status = RunningStatus.STANDING_STILL.value
                elevator = Elevator.objects.get(id = self.elevator_id)
                elevator.running_status = RunningStatus.STANDING_STILL.value
                elevator.is_door_open = False
                elevator.current_floor = self.current_floor
                elevator.save()
                time.sleep(2)  # wait for 1 second before checking the queue again

    def add_request(self, request):
        '''
        Function to add a new request to the elevator's queue
        '''
        self.queue.put(request)
        print(f"Request added to Elevator {self.elevator_id} queue: {request}")
