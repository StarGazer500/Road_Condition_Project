from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.
class RoadInternationalRoughnesIndex(models.Model):
    speed = models.FloatField(max_length=100,verbose_name="Speed",null=True,blank=True)
    vertical_displacement = models.FloatField(max_length=100,verbose_name="Vertical Displacement", null=True,blank=True)
    travel_distance = models.FloatField(max_length=100, verbose_name="Travel Distance", null=True, blank=True)
    longitude = models.FloatField(max_length=100, verbose_name="Longitude",null=True, blank=True)
    latitude = models.FloatField(max_length=100, verbose_name="Latitude",null=True, blank=True)
    time = models.FloatField(max_length=100,verbose_name="Time", null=True, blank=True)
    road_condition = models.CharField(max_length=100, verbose_name="Road Condition",null=True,blank=True)
    geom = models.PointField(default=Point(0.0,0.0),srid=4326)


class Meta:
        indexes = [
            models.Index(fields=['geom'], name='geom_gist_idx_roads', opclasses=['gist'])
        ]