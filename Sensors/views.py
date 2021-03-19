from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from Sensors.models import Plant, User, Sensor, Reading
from Sensors.serializers import PlantSerializer, UserSerializer, SensorSerializer, ReadingSerializer
import logging

logger = logging.getLogger(__name__)

"""
ViewSets just use a variety of mixin classes to define all the behavior they implement
and are used as a shortcut to not need to define a ton of urls and views for essentially boilerplate operations
At the same time, they offer a lot of customization and control over how the CRUD operations actually proceed
"""


class UserViewset(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class PlantViewset(ModelViewSet):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer


class SensorViewset(ModelViewSet):
    queryset = Sensor.objects.all().order_by('uuid')
    serializer_class = SensorSerializer


class ReadingViewset(ModelViewSet):
    queryset = Reading.objects.all().order_by('sensor_id')
    serializer_class = ReadingSerializer

    def create(self, request, *args, **kwargs):
        """ ensure Plant is set based on the Sensor uuid passed in request """
        # TODO this should be done on the model level, probably
        try:
            sensor = Sensor.objects.get(uuid__exact=request.data.get('sensor'))
        except ObjectDoesNotExist:
            return Response(data=f'Sensor with UUID{request.data.get("sensor")} not found',
                            status=status.HTTP_404_NOT_FOUND)
        try:
            plant = Plant.objects.get(id__exact=sensor.plant_id)
        except ObjectDoesNotExist:
            return Response(data=f'Plant with ID{sensor.plant_id} not found', status=status.HTTP_404_NOT_FOUND)
        request.data['plant'] = reverse('plant-detail', args=[plant.id])
        request.data['sensor'] = reverse('sensor-detail', args=[sensor.uuid])
        Reading.objects.filter(sensor__isnull=True)
        return super().create(request, *args, **kwargs)
