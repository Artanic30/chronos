from django.contrib import admin
from django.contrib.auth.models import User
from .models import Event, Place, Weather
# Register your models here.
admin.site.register(Event)
admin.site.register(Place)
admin.site.register(Weather)

