from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Region(models.Model):
    Region =  models.TextField(default=None)
    SundayVisitedTimes = models.IntegerField()
    SaturdayVisitedTimes = models.IntegerField()
    MondayVisitedTimes = models.IntegerField()
    TuesdayVisitedTimes = models.IntegerField()
    WednesdayVisitedTimes = models.IntegerField()
    ThursdayVisitedTimes = models.IntegerField()
    FridayVisitedTimes = models.IntegerField()

    def __unicode__(self):
        return self.region


class Weather(models.Model):
    temperature = models.DecimalField()
    skycorn = models.CharField(max_length=10,default=None)
    pm2point5 = models.DecimalField()
    wind_direction = models.CharField(max_length=5,default=None)
    wind_speed = models.DecimalField()
    humidity = models.DecimalField()
    rain_intensity = models.DecimalField()



class Event(models.Model):
    type_choices= (
        ('f','future'),
        ('p','past')
    )
    Type = models.CharField(max_length=6, choices=type_choices, default=None)
    Content = models.TextField(default=None)
    Region = models.OneToOneField(Region)
    Weather = models.OneToOne(Weather)
    StartDatetime = models.DatetimeField()
    EndDatetime =  models.DatetimeField()
    Emotion = models.DecimalField()

class UserProfile(models.Model):
    user_object = models.OneToOneField(User)
    
