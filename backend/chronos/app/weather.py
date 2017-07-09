from app.models import Weather
import json
import urllib.request
import datetime
import time
import ssl
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")  # project_name 项目名称
django.setup()
ssl._create_default_https_context = ssl._create_unverified_context
weather_url_forecast = 'https://free-api.heweather.com/v5/now?city=CN101020600&key=b1887d6fc0bc4f279f00e8627a3f292f'
weather_url_now = 'https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/121.6544,25.1552/realtime.json'


def get_weather_forecast():
    global weather_url_forecast
    req = urllib.request.Request(weather_url_forecast)
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        weatherjson = json.JSONDecoder().decode(content.decode('utf-8'))
        try:
            if weatherjson['HeWeather5']['status'] == "ok":
                wd = weatherjson['now']
                print(weatherjson['now']['cond']['code'])
                # wo -> weather object
                for i in range(1, 23):
                    wo = Weather.objects.get(
                        datetime=datetime.datetime.now() + datetime.timedelta(hours=i)
                    )
                    wo.temperature = 0,
                    wo.skycon = wd['skycon'][i]
                    wo.humidity = wd['humidity'][i]
                    wo.pm2point5 = wd['pm25'][i]
                    wo.wind_speed = wd['wind'][i]['speed']
                    wo.wind_direction = wd['wind'][i]['direction']
                    wo.precipitation = wd['precipitation'][i]['value']
                    wo.rain_intensity = 0
                    wo.save()
            else:
                return "error"
        except:
            return "error"


def get_weather_now():
    global weather_url_now
    req = urllib.request.Request(weather_url_now)
    resp = urllib.request.urlopen()
    content = resp.read()
    if (content):
        weatherjson = json.JSONDecoder().decode(content)
        try:
            if json['result']['status'] == 'ok':
                wd = weatherjson['result']
                # wo -> weather objects
                wo = None
                if datetime.datetime.now().minute >= 30:
                    wo = Weather.objects.get(datetime=datetime.datetime.now().replace(minute=0) + timedelta(hours=1))
                elif datetime.datetime.now().minute < 30:
                    wo = Weather.objects.get(datetime=datetime.datetime.now().replace(minute=0))
                wo.temperature = wd['temperature']
                wo.skycon = wd['skycon']
                wo.pm2point5 = wd['pm25']
                wo.wind_direction = wd['wind']['direction']
                wo.wind_speed = wd['wind']['speed']
                wo.humidity = wd['humidity']
                wo.rain_intensity = wd['precipitation']['local']['intensity']
                wo.save()
                return 'success'
            else:
                return 'error'
        except:
            return "error"


if __name__ == "__main__":
    while True:
        get_weather_forecast()
        # get_weather_now()
        time.sleep(3600)
