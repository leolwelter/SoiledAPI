from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Sensors import views

# provides autowired root and ViewSet view links for each registered ViewSet
router = DefaultRouter()
router.register('sensors', views.SensorViewset, 'sensor')
router.register('plants', views.PlantViewset, 'plant')
router.register('users', views.UserViewset, 'user')
router.register('readings', views.ReadingViewset, 'reading')
urlpatterns = [
    path('', include(router.urls))
]
