from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_registered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID:{self.id} {self.username}'


class Plant(models.Model):
    """
    Represents a single plant for a single user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO semantically normalize this in views
    species = models.CharField(max_length=64, default='')
    last_watered = models.DateTimeField(default='', blank=True, null=True)

    def __str__(self):
        return f'ID:{self.id} (User:{self.user.username}, {self.species})'


class Sensor(models.Model):
    OKAY = 'OK'
    NO_CONTACT = 'NC'
    IGNORED = 'IG'
    OFFLINE = 'OL'
    SENSOR_STATUSES = [
        (OKAY, 'Healthy'),
        (NO_CONTACT, 'No Contact'),
        (IGNORED, 'Ignored'),
        (OFFLINE, 'Confirmed Offline')
    ]
    uuid = models.CharField(primary_key=True, max_length=64)
    status = models.CharField(choices=SENSOR_STATUSES, max_length=2, default='OK')
    location = models.CharField(default='', max_length=128, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'ID:{self.uuid[0:8]}... ({self.location}, P:{self.plant_id})'


class Reading(models.Model):
    """
    Represents a sensor reading: has a many-to-one relation with a sensor, and with a plant

    If the sensor is deleted, we keep the readings.
    """
    sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=False)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField()  # generated on the sensor
    status = models.IntegerField()

    def __str__(self):
        return f'[{self.timestamp}] (S{self.sensor_id}, P{self.plant_id})'
