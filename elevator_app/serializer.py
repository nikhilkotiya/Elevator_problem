from rest_framework import serializers


# Local imports
from .models import Building,Elevator,ElevatorRequest


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
    building_id = serializers.CharField(max_length = 20,required = True)
    destination_floor = serializers.IntegerField(required = True)
    source_floor = serializers.IntegerField(required = True)