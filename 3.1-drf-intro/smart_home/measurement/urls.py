from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('sensors/', SensorAPIList.as_view()),
    path('sensors/<int:pk>/', SensorAPIUpdate.as_view()),
    path('sensor_details/<int:pk>/', SensorDetailAPIView.as_view()),
    path('мeasurement/', MeasurementAPIList.as_view()),
    path('мeasurement/<int:pk>/', MeasurementAPIUpdate.as_view())
]
