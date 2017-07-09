import json
import urllib.request
import datetime
import time
import ssl
import urllib.parse
ssl._create_default_https_context = ssl._create_unverified_context
weather_url_forecast = 'https://free-api.heweather.com/v5/now?city=CN101020600&key=b1887d6fc0bc4f279f00e8627a3f292f'
weather_url_now = 'https://free-api.heweather.com/v5/now?city=CN101020600&key=b1887d6fc0bc4f279f00e8627a3f292f'


# def get_weather_forecast():
#     global weather_url_forecast
#     req = urllib.request.Request(weather_url_forecast)
#     resp = urllib.request.urlopen(req)
#     content = resp.read()
#     if content:
#         weatherjson = json.JSONDecoder().decode(content.decode('utf-8'))
#         try:
#             if weatherjson['HeWeather5']['status'] == "ok":
#                 wd = weatherjson['now']
#                 print(weatherjson['now']['cond']['code'])
#                 for i in range(1, 23):
#                     data = urllib.parse.urlencode({'temperature': 1, 'skycon': wd['skycon'][i], 'humidity': wd['humidity'][i],})
#                     data = data.encode('utf-8')
#                     request = urllib.request.Request("http://requestb.in/xrbl82xr")
#                     # adding charset parameter to the Content-Type header.
#                     request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
#                     f = urllib.request.urlopen(request, data)
#                     print(f.read().decode('utf-8'))
#                     wo.temperature = 0,
#                     wo.skycon =
#                     wo.humidity =
#                     wo.pm2point5 = wd['pm25'][i]
#                     wo.wind_speed = wd['wind'][i]['speed']
#                     wo.wind_direction = wd['wind'][i]['direction']
#                     wo.precipitation = wd['precipitation'][i]['value']
#                     wo.rain_intensity = 0
#
#             else:
#                 return "error"
#         except:
#             return "error"


def get_weather_now():
    global weather_url_now
    req = urllib.request.Request(weather_url_now)
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if (content):
        weatherjson = json.JSONDecoder().decode(content.decode('utf-8'))
        print(weatherjson)
        print()
        if weatherjson['HeWeather5'][0]['status'] == 'ok':
            wd = weatherjson['HeWeather5'][0]['now']
            try:
                data = urllib.parse.urlencode(
                    {'temperature': wd['tmp'], 'skycon': wd['cond']['txt'], 'humidity': wd['hum'], 'rain-intensity': wd['pcpn'],'wind-direction': wd['wind']['spd'],'wind-intensity':wd['wind']['sc'][0:1],})
                data = data.encode('utf-8')
                request = urllib.request.Request("http://127.0.0.1:8000/api/weather/add/now")
                request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
                # f = urllib.request.urlopen(request, data)
                # print(f.read().decode('utf-8'))
            except:
                return -1


if __name__=='__main__':
    get_weather_now()