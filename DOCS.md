Elevator System
Elevator system Model. Equivalent to a building containing a number of elevators Also contains the default ID parameter assigned by django as a primary key. Used to make the project compatible with multiple elevator systems. Minimum floor is assumed as 0 but dynamic minimum floor can be implemented easily.

GET /buildings: Returns a list of all buildings in the system.
POST /buildings: Creates a new building with the specified parameters.
GET /buildings/:id: Returns the details of a specific building, where :id is the ID of the building.
PUT /buildings/:id: Updates the details of a specific building, where :id is the ID of the building.
DELETE /buildings/:id: Deletes a specific building, where :id is the ID of the building.

API Documentation - Elevator System

This is an API documentation for an elevator system model, which consists of buildings and elevators. The API allows creating, updating, deleting buildings and elevators, and sending requests for elevators from outside and inside the elevator.

Base URL: http://127.0.0.1:8000/

Building API Endpoints:

GET /buildings: Returns a list of all buildings in the system.

Response Example:
Status Code: 200 OK
Response Body:
[
    {
        "id": 10,
        "name": "My Building",
        "max_floor": 10,
        "min_floor": 0,
        "number_of_elevators": 2
    }
]

POST /buildings: Creates a new building with the specified parameters.

Payload Example:
{
  "name": "string",
  "max_floor": 0,
  "min_floor": 0,
  "number_of_elevators": 0
}

Response Example:
Status Code: 201 Created
Response Body:
{
    "id": 11,
    "name": "My New Building",
    "max_floor": 20,
    "min_floor": 0,
    "number_of_elevators": 3
}
GET /buildings/:id: Returns the details of a specific building, where :id is the ID of the building.

Response Example:
Status Code: 200 OK
Response Body:
{
    "id": 10,
    "name": "My Building",
    "max_floor": 10,
    "min_floor": 0,
    "number_of_elevators": 2
}

PUT /buildings/:id: Updates the details of a specific building, where :id is the ID of the building.

Payload Example:
{
    "id": 10,
    "name": "My Updated Building",
    "max_floor": 15,
    "min_floor": 0,
    "number_of_elevators": 2
}
Response Example:
Status Code: 200 OK
Response Body:

{
    "id": 10,
    "name": "My Updated Building",
    "max_floor": 15,
    "min_floor": 0,
    "number_of_elevators": 2
}

DELETE /buildings/:id: Deletes a specific building, where :id is the ID of the building.

Response Example:
Status Code: 200 OK





GET /elevator: Returns a list of all elevator in the system.
POST /elevator: Creates a new building with the specified parameters.
GET /elevator/:id: Returns the details of a specific elevator, where :id is the ID of the building.
PUT /elevator/:id: Updates the details of a specific elevator, where :id is the ID of the building.
DELETE /elevator/:id: Deletes a specific elevator, where :id is the ID of the building

GET http://127.0.0.1:8000/elevator/
View all the elevator in a buiding(system)

Response Example
200
[
    {
        "id": 7,
        "number": 1,
        "current_floor": 9,
        "is_busy": false,
        "is_operational": true,
        "is_door_open": false,
        "running_status": "standing_still",
        "building": 10
    }
]
POST http://127.0.0.1:8000/elevator/
201
Create a new Elevator 
payload
{
    "number": 1,
    "current_floor": 9,
    "is_busy": false,
    "is_operational": true,
    "is_door_open": false,
    "running_status": "standing_still",
    "building": 10
}

GET http://127.0.0.1:8000/elevator/7/
Response Example
200
{
    "id": 7,
    "number": 1,
    "current_floor": 9,
    "is_busy": false,
    "is_operational": true,
    "is_door_open": false,
    "running_status": "standing_still",
    "building": 10
},

update Building
200
PUT http://127.0.0.1:8000/elevator/7/
Request 
{
    "id": 7,
    "number": 1,
    "current_floor": 9,
    "is_busy": false,
    "is_operational": true,
    "is_door_open": false,
    "running_status": "standing_still",
    "building": 10
}
Response
{
    "id": 7,
    "number": 1,
    "current_floor": 9,
    "is_busy": false,
    "is_operational": true,
    "is_door_open": false,
    "running_status": "standing_still",
    "building": 10
}


Delete Building
200
DELETE http://127.0.0.1:8000/elevator/10/





request of a elevator from outside the elevator
POST 
http://127.0.0.1:8000/elevator/request_outside_elivator/
request
{
    "destination_floor" : 9,
    "building_id" : 10
}
Response => "Request sent successfully"




request of a elevator from insdide the elevator
POST 
http://127.0.0.1:8000/elevator/request_inside_elivator/
{
    "destination_floor" : 0,
    "building_id" : 10,
    "elevator_id":7
}
Response => "Request sent successfully"