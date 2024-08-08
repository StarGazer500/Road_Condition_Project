#Third Party Modules
from import_export import resources
from import_export.fields import Field

#Django Modules
from django.contrib.gis.geos import Point

from .models import RoadInternationalRoughnesIndex

class RoadInternationalRoughnessIndexxResource(resources.ModelResource):

    speed = Field(attribute='speed', column_name='Speed')
    vertical_displacement = Field(attribute='vertical_displacement', column_name='Vert_Displacement')
    travel_distance  = Field(attribute='travel_distance', column_name='Travel_Distance')
    longitude = Field(attribute='longitude', column_name='longitude')
    latitude = Field(attribute='latitude', column_name='latitude')
    time = Field(attribute='time', column_name='time')
    road_condition = Field(attribute='road_condition', column_name='Road Condition')

    class Meta:
        model = RoadInternationalRoughnesIndex  # or 'core.Book'
        fields = (
         "id",
         'speed', 
         'vertical_displacement', 
         'travel_distance',
         'longitude',
         'latitude',
         'time',
         'road_condition',
         'geom'
         )
        
    def before_import_row(self, row, **kwargs):
        """
        Override this method to create a Point object from latitude and longitude.
        """
        latitude = row.get('latitude')
        longitude = row.get('longitude')
        if latitude is not None and longitude is not None:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
                row['geom'] = Point(longitude, latitude)
            except ValueError:
                row['geom'] = None
        else:
                row['geom'] = None