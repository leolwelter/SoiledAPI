from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.reverse import reverse

from Sensors.models import Plant, User, Sensor, Reading
from Sensors.serializers import PlantSerializer, UserSerializer, SensorSerializer, ReadingSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'sensors': reverse('sensor-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'plants': reverse('plant-list', request=request, format=format),
        'readings': reverse('reading-list', request=request, format=format)
    })


class RetrieveUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrievePlant(RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class RetrieveSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveReading(RetrieveAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class ListPlants(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class ListUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ListReadings(ListAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
