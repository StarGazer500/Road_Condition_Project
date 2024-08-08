from django.contrib import admin
#Third Party Modules
from leaflet.admin import LeafletGeoAdmin
from import_export.admin import ImportExportModelAdmin

from .models import RoadInternationalRoughnesIndex
from .serialiazers import AddRoadInternationRoughnessIndexSerializer
from .import_resources import RoadInternationalRoughnessIndexxResource

leaflet_config = {
    'DEFAULT_CENTER': (20, 0),  # Adjust this based on your map's center (latitude, longitude)
    #'DEFAULT_ZOOM': 2,
    'TILES': [
         ('Satellite', 'http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {'subdomains': ['mt0', 'mt1', 'mt2', 'mt3']}),
        ('OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {}),
    ],
   'LAYERS_CONTROL': True,  # Add layer controls
}

# Register your models here.

#Fire Road International Roughness Index Admin
class RoadInternationalRoughnessIndexAdmin(LeafletGeoAdmin,ImportExportModelAdmin):
   
    serializer_class = AddRoadInternationRoughnessIndexSerializer
    resource_classes = [RoadInternationalRoughnessIndexxResource]
    leaflet_config = leaflet_config
   
admin.site.register(RoadInternationalRoughnesIndex, RoadInternationalRoughnessIndexAdmin)

