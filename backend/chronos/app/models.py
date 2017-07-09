from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user_object = models.OneToOneField(User)
    Nickname = models.CharField(max_length=50, default=None)
    Age = models.IntegerField()
    Job = models.CharField(max_length=50, default=None)


# class Place(models.Model):
#     Region = models.TextField(default=None)
#     SundayVisitedTimes = models.IntegerField()
#     SaturdayVisitedTimes = models.IntegerField()
#     MondayVisitedTimes = models.IntegerField()
#     TuesdayVisitedTimes = models.IntegerField()
#     WednesdayVisitedTimes = models.IntegerField()
#     ThursdayVisitedTimes = models.IntegerField()
#     FridayVisitedTimes = models.IntegerField()
#
#     def __unicode__(self):
#         return self.Region


# class Weather(models.Model):
#     temperature = models.DecimalField(decimal_places=2, max_digits=5)
#     skycon = models.CharField(max_length=10, default=None)
#     wind_direction = models.CharField(max_length=5, default=None)
#     wind_speed = models.DecimalField(decimal_places=2, max_digits=5)
#     humidity = models.DecimalField(decimal_places=2, max_digits=5)
#     rain_intensity = models.DecimalField(decimal_places=2, max_digits=6)
#     datetime = models.DateTimeField(default=None)
#
#     def __unicode__(self):
#         return self.datetime
#

class Token(models.Model):
    token = models.CharField(max_length=30, default=None)
    userprofile = models.OneToOneField(UserProfile)
    username = models.CharField(max_length=100, default=None)


class Event(models.Model):
    type_choices = (
        ('f', 'future'),
        ('p', 'past')
    )
    Type = models.CharField(max_length=6, choices=type_choices, default=None)
    Content = models.TextField(default=None)
    # Region = models.OneToOneField(Place, default=None)
    # Weather = models.OneToOneField(Weather)
    StartDatetime = models.DateTimeField()
    EndDatetime = models.DateTimeField()
    Emotion = models.DecimalField(decimal_places=2, max_digits=5)
