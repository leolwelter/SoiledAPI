from django.urls import path
from django.conf.urls import re_path
from rest_framework.routers import DefaultRouter
from Sensors import views

urlpatterns = [
    path('', views.api_root, name='root'),
    path('plants', views.ListPlants.as_view(), name='plant-list'),
    path(r'users/', views.ListUsers.as_view(), name='user-list'),
    path(r'sensors/', views.ListSensors.as_view(), name='sensor-list'),
    path(r'readings/', views.ListReadings.as_view(), name='reading-list'),
    path(r'users/<int:pk>', views.RetrieveUser.as_view(), name='user-detail'),
    path(r'plants/<int:pk>', views.RetrievePlant.as_view(), name='plant-detail'),
    path(r'sensors/<int:pk>', views.RetrieveSensor.as_view(), name='sensor-detail'),
    path(r'readings/<int:pk>', views.RetrieveReading.as_view(), name='reading-detail'),
]
