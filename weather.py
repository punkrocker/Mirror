from urllib import request
import json

city_code = '101120201'
url = 'http://t.weather.sojson.com/api/weather/city/' + city_code
weather_info = request.urlopen(url)
readable_info = weather_info.read().decode('utf-8')
weather_json = json.loads(readable_info)['data']
print(weather_json)
print('湿度：' + weather_json['shidu'])
print('PM2.5：' + str(weather_json['pm25']))
print('PM10：' + str(weather_json['pm10']))
print('空气质量：' + weather_json['quality'])
print('当前温度：' + str(weather_json['wendu']) + '℃')
