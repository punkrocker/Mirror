from urllib import request
import json


class Weather:
    def __init__(self):
        city_code = '101120201'
        url = 'http://t.weather.sojson.com/api/weather/city/' + city_code
        weather_info = request.urlopen(url)
        readable_info = weather_info.read().decode('utf-8')
        weather_json = json.loads(readable_info)['data']
        self.wet = weather_json['shidu']
        self.pm25 = str(weather_json['pm25'])
        self.pm10 = str(weather_json['pm10'])
        self.air_quality = weather_json['quality']
        self.current_temperature = str(weather_json['wendu']) + '℃'
