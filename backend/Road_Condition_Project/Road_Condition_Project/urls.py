
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api-auth/', include('rest_framework.urls')),
     path('fire-outbreakpi/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    
     #Road_Condition_App Mapping
    # path('road_condition/', include('Road_Condition_App.urls')),
]
