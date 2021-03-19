from rest_framework import serializers

from .models import Sensor, User, Reading, Plant

"""
Serializers for Django Rest Framework
NOTE, for HyperlinkedModelSerializer fields, read_only must be True, or queryset must be set
In order to change relation fields (like above), read_only MUST BE FALSE 
"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'date_registered']


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ['url', 'id', 'species', 'last_watered', 'user']

    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['url', 'uuid', 'status', 'location', 'user', 'plant']

    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    plant = serializers.HyperlinkedRelatedField(view_name='plant-detail', read_only=True)


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ['url', 'id', 'sensor', 'plant', 'temperature', 'humidity', 'timestamp', 'status']

    sensor = serializers.HyperlinkedRelatedField(view_name='sensor-detail', queryset=Sensor.objects.all())
    plant = serializers.HyperlinkedRelatedField(view_name='plant-detail', queryset=Plant.objects.all())
