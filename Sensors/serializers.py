from rest_framework import serializers

from .models import Sensor, User, Reading, Plant


# serializers for Django Rest Framework

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
        fields = ['url', 'id', 'sensor', 'plant', 'temperature', 'humidity', 'timestamp']
    sensor = serializers.HyperlinkedRelatedField(view_name='sensor-detail', read_only=True)
    plant = serializers.HyperlinkedRelatedField(view_name='plant-detail', read_only=True)
