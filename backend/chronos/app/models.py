from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Place(models.Model):
    Region = models.TextField(default=None)
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
    skycorn = models.CharField(max_length=10, default=None)
    pm2point5 = models.DecimalField()
    wind_direction = models.CharField(max_length=5, default=None)
    wind_speed = models.DecimalField()
    humidity = models.DecimalField()
    rain_intensity = models.DecimalField()


class Token(models.Model):
    token = models.CharField(max_length=30, default=None)
    userprofile = models.OneToOneField(UserProfile)
    username = models.CharField(max_length=100, default=None)


class Event(models.Model):
    type_choices = (
        ('f', 'future'),
        ('p', 'past')
    )
    Name = models.CharField(max_lengt=30,defualt=None)
    Type = models.CharField(max_length=6, choices=type_choices, default=None)
    Content = models.TextField(default=None)
    Region = models.OneToOneField(Place)
    Weather = models.OneToOne(Weather)
    StartDatetime = models.DatetimeField()
    EndDatetime = models.DatetimeField()
    Emotion = models.DecimalField()


class UserProfile(models.Model):
    user_object = models.OneToOneField(User)
    Age = models.IntegerField()
    Job = models.CharField(max_length=50, default=None)
