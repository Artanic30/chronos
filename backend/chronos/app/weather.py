from jpspapp.models import Weather
import datetime
weather_url_forecast = 'https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/121.6544,25.1552/forecast.json'
weather_url_now = 'https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/121.6544,25.1552/realtime.json'
def get_weather_forecast():
    global weather_url_forecast
    req = urllib.request.Request(weather_url_forecast)
    resp=urllib.request.urlopen(req)
    content = resp.read()
    if(content):
        weatherJSON = json.JSONDecoder().decode(content)
        #print(content)
        try:
            if weatherJSON['result']['hourly']['status'] == "ok":
                wd = weatherJSON['result']['hourly']
                return weatherJSON['result']['hourly']['pm25'][0]['value']
                # wo -> weather object
                for i in range(1,23):
                    wo = Weather.objects.get(
                        datetime = datetime.datetime.now()+timedelta(hours=i)
                    )
                    wo.temperature = 0,
                    wp.skycron = wd['skycon'][i]
                    wp.humidity = wd['humidity'][i]
                    wp.pm2point5 = wd['pm25'][i]
                    wp.wind_speed= wd['wind'][i]['speed']
                    wp.wind_direction = wd['wind'][i]['direction']
                    wp.precipitation = wd['precipitation'][i]['value']
                    wp.rain_intensity = 0
                    wp.save()
            else:
                return "error"
        except:
            return "error"

def get_weather_now():
    global weather_url_now
    req = urllib.request.Request(weather_url_now)
    resp = urllib.request.urlopen()
    content = resp.read()
    if(content):
        weatherJSON = json.JSONDecoder().decode(content)
        try:
            if weatherJSON['result']['status'] == 'ok':
                wd = weatherJSON['result']
                # wo -> weather objects
                wo = None
                if datetime.datetime.now().minute >=30:
                    wo = Weather.objects.get(datetime=datetime.datetime.now().replace(minute=0)+timedelta(hours=1))
                elif datetime.datetime.now().minute <30:
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
        get_weather_now()
        time.sleep(3600)
