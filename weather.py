from urllib import request

weather_info = request.urlopen("http://www.weather.com.cn/data/sk/101010100.html")
readable_info = weather_info.read().decode('utf-8')
print(readable_info)

