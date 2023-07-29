from django.db import models
from .constants import RunningStatus


class Building(models.Model):
    '''
    Building Model. Equivalent to a building containing a number of elevators
    Also contains the default ID parameter assigned by django as a primary key.
    Used to make the project compatible with multiple elevator systems.
    Minimum floor is assumed as 0 but dynamic minimum floor can be implemented easily.
    '''
    name = models.CharField(max_length=20)
    max_floor = models.IntegerField()
    min_floor = models.IntegerField(default=0)
    number_of_elevators = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return_str = str(self.name) + " Building No " + str(self.id)
        return return_str

    def create_elevators(self, building_id, number_of_elevators):
        '''
        Function to automatically create elevators inside an Bilding
        Given the Building id and number of elevators. This function is ran once
        an elevator is created
        '''

        for i in range(number_of_elevators):
            elevator_object = Elevator.objects.create(
                building_id=building_id,
                number=i+1,
            )

            elevator_object.save()


class Elevator(models.Model):
    '''
    Elevator object model. Represents a single elevator that can move up and down. It
    is always a part of an entire elevator system. So elevator system is assigned as foreignkey.

    '''

    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    number = models.IntegerField()
    current_floor = models.IntegerField(default=0)
    is_busy = models.BooleanField(default=False)
    # is_operational = models.BooleanField(default=True)
    is_door_open = models.BooleanField(default=False)
    running_status = models.CharField(max_length=20, choices=[(status.value, status.name.title(
    )) for status in RunningStatus], default=RunningStatus.STANDING_STILL.value)

    def __str__(self) -> str:
        return_str = "Elevator Number " + str(self.number)
        return return_str


class ElevatorRequest(models.Model):
    '''
    User request targeted to a specific elevator. This can be improved further using model managers 
    to clean the invalid requests like request elevator in negative floor/greater than maximum floor
    request an elevator that doesn't exist.
    '''
    destination_floor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
