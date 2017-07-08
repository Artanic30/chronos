from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from .models import Weather, Place, Token, Event, UserProfile
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate
import random

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

class Token:
    def __init__(self,username,token=""):
        self.username = username
        self.token = token
        self.message = ""

    def generate(self):
        for i in range(0,30):
            self.token += alphabet[random.randint(0, len(alphabet) - 1)]
        try:
            Token.objects.create(
                Token=self.token,
                User=User.objects.get(Username=self.username),
                UserType=self.usertype
                # start_time=datetime.datetime.now(),
                # TODO:  datetime in python and SQL ??
                # end_time =datetime.datetime.now(),
            )
            self.message = 'Success'
            return self.token
        except:
            self.message = 'error'

    def remove(self):
        try:
            token = Token.objects.get(Username=self.username)
            if token:
                token.delete()
                self.message = 'Success'
                return self.message
        except:
            self.message = 'Error'
            return self.message

    def authenticate(self):
        token = Token.objects.get(Username=self.username).Token
        if token != None:
            if self.token == token:
                self.message = 'Success'
                return self.message
            else:
                self.message = 'Error'
                return self.message

@require_http_methods(['POST'])
def login(request):
    try:
        body = json.loads(request.body)
        username = body['Username']
        password = body['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token_object = Token(username=username)
            # TODO : token
            return JsonResponse({
                "UserName": username,
                "message": 'User Authenticated',
                "Token": token_object.generate(),
                "Access-Control-Allow-Origin": '*'
            })
    except:
        return JsonResponse({
            "message": "User Not Authenticated",
            "Access-Control-Allow-Origin": '*',
        })

@require_http_methods(['POST'])
def register(request):
    try:
        body = json.loads(request.body)
        username = body['Username']
        password = body['password']
        token_object = Token(username=username)
        return JsonResponse({
            "message": "Success",
            "Token": token_object.generate(),
            "Access-Control-Allow-Origin": '*'
        })
    except:
        return JsonResponse({
            "message": "Error",
            "Access-Control-Allow-Origin": '*',
        })

@require_http_methods(['POST'])
def logout(request):
    pass

@require_http_methods(['POST'])
def getPlaces(request):
    try:
        body = json.loads(request)
        token = body['Token']
        place = body['Place']
        day = body['day']
        queryset = []
        queryset_object = Place.objects.filter(Region=place)
        for data in queryset_object:
            queryset.append({
                'Region': data.Region,
                'SundayVisitedTimes': data.SundayVisitedTimes,
                'SaturdayVisitedTimes': data.SaturdayVisitedTimes,
                'MondayVisitedTimes' : data.MondayVisitedTimes,
                'TuesdayVisitedTimes': data.TuesdayVisitedTimes,
                'WednesdayVisitedTimes': data.WednesdayVisitedTimes,
                'ThursdayVisitedTimes': data.ThursdayVisitedTimes,
                'FridayVisitedTimes': data.FridayVisitedTimes
            })
        return JsonResponse({
            "message": "Success",
            "Access-Control-Allow-Origin": '*',
            "data": json.dumps(queryset)
        },safe=False)
    except:
        return JsonResponse({
            "message": "Error",
            "Access-Control-Allow-Origin": '*'
        })


@require_http_methods(['POST'])
def addEvent(request):
    try:
        body = json.loads(request.body)
        name = body['Name']
        type = body['Type']
        place = body['Place']
        content = body['Content']
        start_datetime = body['StartDatetime']
        end_datetime = body['EndDatetime']
        emotion = body['Emotion']
        # weather uses api!
        # todo: place one to one field
        Event.objects.create(Name=name,Type=type,Place=place,Content=content,StartDatetime=start_datetime,EndDatetime=end_datetime,Emotion=emotion)
        return JsonResponse({
            "message":"Success",
            "Access-Control-Allow-Origin": '*'
        })
    except:
        return JsonResponse({
            "message":"Error",
            "Access-Control-Allow-Origin": '*'
        })

@require_http_methods(['POST'])
def removeEvent(request):
    try:
        body = json.loads(request.body)
        id = body['Id']
        event_object = Event.objects.filter(pk=id)
        event_object.delete()
        return JsonResponse({
            "message":"Success",
            "Access-Control-Allow-Origin": '*'
        })
    except:
        return JsonResponse({
            "message":"Error",
            "Access-Control-Allow-Origin": '*'
        })


@require_http_methods(['POST'])
def updateEvent(request):


@require_http_methods(['POST'])
def predictEvent(request):
    pass


@require_http_methods(['POST'])
def profileGet(request):
    try:
        body = json.loads(request.body)
        username = body['Username']
        userprofile_object = UserProfile.objects.get(username=username)
        return JsonResponse({
            "message": "Success",
            "Access-Control-Allow-Origin": '*',
            'data':{
                'Nickname': userprofile_object.Nickname
                'Id': userprofile_object.pk
            }
        })
    except:
        return JsonResponse({
            "message": "Error",
            "Access-Control-Allow-Origin": '*'
        })


@require_http_methods(['POST'])
def profileEdit(request):
    try:
        body = json.loads(request.body)
        pk = body['Id']
        nickname = body['Nickname']
        userprofile_object = UserProfile.objects.get(pk=pk)
        userprofile_object.Nickname = nickname
        userprofile_object.save()
        return JsonResponse({
            "message": "Success",
            "Access-Control-Allow-Origin": '*'
        })
    except:
        return JsonResponse({
            "message": "Error",
            "Access-Control-Allow-Origin": '*'
        })


@require_http_methods(['POST'])
def getEvent(request):
    try:
        body = json.loads(request.body)
        month = body['Month']
        day = body['Day']
        year = body['Year']
        # todo: event_object
        event_object = Event.objects.get(StartDatetime=datetime.datetime(year,month,day))
        data = {
            'pk': event_object.pk,
            'Name': event_object.Name,
            'Type': event_object.Type,
            'Place': event_object.Place,
            'Content': event_object.Content,
            'Weather': event_object.Weather,
            'StartDatetime': event_object.StartDatetime,
            'EndDatetime': event_object.EndDatetime,
            'Emotion': event_object
        }
        return JsonResponse({
            "message": 'Success',
            "Access-Control-Allow-Origin": '*',
            "data": json.dumps(data)
        },safe=False)
    except:
        return JsonResponse({
            "message": "Error",
            "Access-Control-Allow-Origin": '*'
        })
