from jpspapp.models import Weather
import datetime
weather_url_forecast = 'https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/121.6544,25.1552/forecast.json'
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

if __name__ == "__main__":
    while True:
        time.sleep(3600)
