from enum import Enum
class RunningStatus(Enum):
    '''
    Choices for running status of the elevator 
    '''
    GOING_UP = 'going_up'
    STANDING_STILL = 'standing_still'
    GOING_DOWN = 'going_down'
    NOT_WORKING = 'not_working'