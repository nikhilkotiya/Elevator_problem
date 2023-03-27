from rest_framework import serializers
from .models import Building, Elevator, ElevatorRequest


class BuildingSerializer(serializers.ModelSerializer):
    '''
    Model serializer for model Building
    '''
    class Meta:
        model = Building
        fields = '__all__'


class ElevatorSerializer(serializers.ModelSerializer):
    '''
    Model serializer for model Elevator
    '''

    class Meta:
        model = Elevator
        fields = '__all__'


class ElevatorRequestSerializer(serializers.ModelSerializer):
    '''
    Model serializer for ElevatorRequest, used for 
    POST request that Takes only two arguments 
    '''
    class Meta:
        model = ElevatorRequest
        fields = (
            'requested_floor',
            'destination_floor',
        )


class ElevatorRequestSerializerAll(serializers.ModelSerializer):
    '''
    Model serializer for ElevatorRequest, used for 
    GET request that returns all the fields
    '''
    class Meta:
        model = ElevatorRequest
        fields = '__all__'


class ElevatorRequestSerializer(serializers.Serializer):
    '''
    serializer for people inside Elevator, used for 
    validate the request 
    '''
    elevator_id = serializers.IntegerField(required=True)
    building_id = serializers.CharField(max_length=20, required=True)
    destination_floor = serializers.IntegerField(required=True)


class ElevatorRequestOutsideSerializer(serializers.Serializer):
    '''
    serializer for people outside Elevator, used for 
    validate the request 
    '''
    building_id = serializers.CharField(max_length=20, required=True)
    destination_floor = serializers.IntegerField(required=True)


class ElevatorStatusSerializer(serializers.Serializer):
    '''
    serializer for Status of Elevator, used for 
    validate the request 
    '''
    elevator_id = serializers.CharField(max_length=20, required=True)