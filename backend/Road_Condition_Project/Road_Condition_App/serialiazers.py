#Third-party modules
from rest_framework import serializers
from django.contrib.gis.geos import Point

from .models import RoadInternationalRoughnesIndex

class PointFieldSerializer(serializers.Field):
   def to_representation(self, value):
        # Convert the Point object to a dictionary with coordinates
        return {
            'longitude': value.x,
            'latitude': value.y
        }
   def to_internal_value(self, data):
        # Convert separate longitude and latitude to a Point object
        try:
            longitude = data['longitude']
            latitude = data['latitude']
            return Point(longitude, latitude)
        except KeyError:
            raise serializers.ValidationError("Longitude and latitude are required fields.")
        
class AddRoadInternationRoughnessIndexSerializer(serializers.ModelSerializer):
    speed = serializers.FloatField(required = False)
    vertical_displacement= serializers.FloatField(required = False)
    travel_distance = serializers.FloatField(required = False)
    road_condition = serializers.CharField(required = False)
    time = serializers.FloatField(required = False)
    longitude = serializers.FloatField(required = False)
    latitude = serializers.FloatField(required = False)
    geom = PointFieldSerializer(required=False)
    
    class Meta:
        model = RoadInternationalRoughnesIndex
        fields = [
            'id', 
            'speed', 
            'vertical_displacement', 
            'travel_distance',
            'road_condition',
            'time',
            'longitude',
            'latitude',
            'geom'
            ] 