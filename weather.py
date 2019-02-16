from urllib import request
import json

weather_info = request.urlopen("http://www.weather.com.cn/data/sk/101120201.html")
readable_info = weather_info.read().decode('utf-8')
weather_json = json.loads(readable_info)
print(weather_json['weatherinfo']['city'])
