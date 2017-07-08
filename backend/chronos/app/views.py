from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from jpspapp.models import Weather, Region, Token, Event
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate
import random

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


class Token:
    def __init__(self, username, token=""):
        self.username = username
        self.token = token
        self.message = ""

    def generate(self):
        for i in range(length):
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
                "message": "User Authenticated",
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
        token_object = Token(username=username)
        token = token_object.generate()
        return JsonResponse({
            "token": token,
            "message": "Success",
            "Access-Control-Allow-Origin": '*'
        })
    except:
        return JsonResponse({
            "message": "Error",
            "Access-Control-Allow-Origin": '*',
        })


@require_http_methods(['POST'])
def logout(request):
    try:
        body = json.loads(request.body)
        username = body['Username']
        token = body['Token']
        token_object = Token.objects.get(username=username)
        token_object.delete()
        return JsonResponse({
            'message': 'Success',
            "Access-Control-Allow-Origin": '*',
        })
    except:
        return JsonResponse({
            'message': 'Error',
            "Access-Control-Allow-Origin": '*',
        })

@require_http_methods(['POST'])
def addEvent(request):
    try:
        body = json.loads(request.body)
        type = body['Type']
        place = body['Place']
        content = body['Content']
        start_datetime = body['StartDatetime']
        end_datetime = body['EndDatetime']
        emotion = body['Emotion']
        # weather uses api!
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
def removeEvent(request):
    try:
        body = json.loads(request.body)
        id = body['Id']
        event_object = Event.objects.filter(pk=id)
        event_object.delete()
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
def predictEvent(request):
    pass
