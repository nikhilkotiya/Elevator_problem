from .constants import RunningStatus
def get_floor_distance(user_floor,current_floor,running_status,array_of_floor):
    if array_of_floor:
        max_floor = 0 
        min_floor = -1000
        lenght = len(array_of_floor)
        for floor in range(lenght):
            if array_of_floor[floor] == 1:
                max_floor = floor
            if array_of_floor[floor] == 1 and min_floor == -1000:
                min_floor = floor
        if running_status ==  RunningStatus.GOING_UP and user_floor>=current_floor:
            return user_floor - current_floor 
        elif running_status ==  RunningStatus.GOING_UP:
            return 2*(max_floor-current_floor) + user_floor
        
        elif running_status ==  RunningStatus.STANDING_STILL:
            return abs(user_floor - current_floor)
        
        elif current_floor>=user_floor:
            return current_floor - user_floor
        else:
            return 2*(current_floor -max_floor) + user_floor

    else:
        return abs(user_floor - current_floor)