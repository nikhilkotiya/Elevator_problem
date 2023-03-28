def get_floor_distance(user_floor,current_floor):
    if current_floor >= user_floor:
        return current_floor - user_floor
    else:
        return user_floor - current_floor
