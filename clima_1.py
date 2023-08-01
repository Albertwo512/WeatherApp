import requests, math

city = input('Enter a city:')

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=e97d4e183422cfadb9e54db519a092f3&units=metrics".format(city)

res = requests.get(url)

data = res.json()

temp = data["main"]["temp"]
temp = math.trunc(temp - 273.15)
wind_speed = data["wind"]["speed"]

latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]

description = data["weather"][0]["description"]

print("temperatura:", temp)
print("Velocidad de viento:", wind_speed, "m/s")
print("Latitud:",latitude)
print("Descripcion:",description)

