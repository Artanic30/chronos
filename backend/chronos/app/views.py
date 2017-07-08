from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from jpsp.shortcut import JPSPToken, JPSPTime
from jpspapp.models import Weather, Region,
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate

# Create your views here.

@require_http_methods(['POST'])
def login(request):
    try:
        body = json.loads(request.body)
        username = body['Username']
        password = body['Password']
        if user is not None:
            token_object = Token(username=userid, usertype=usertype)
            # TODO : token
            return JsonResponse({
                "UserName":
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
        password = body['password']
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
def predictEvent(request):
    pass
