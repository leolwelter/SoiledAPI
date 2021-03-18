from django.contrib import admin
from .models import Sensor, User, Reading, Plant
# Register your models here.
models = (User, Sensor, Reading, Plant)
admin.site.register(models)
