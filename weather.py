import requests
import math
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    ciudad = "Tequila"  # Ciudad por defecto
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=e97d4e183422cfadb9e54db519a092f3&units=metric".format(ciudad)
    res = requests.get(url)
    data = res.json()

    temperatura = data["main"]["temp"]
    temperatura = math.trunc(temperatura)
    velocidad_viento = data["wind"]["speed"]

    latitud = data["coord"]["lat"]
    longitud = data["coord"]["lon"]

    descripcion = data["weather"][0]["description"]
    main = data["weather"][0]["main"]

    return render_template('clima.html', ciudad=ciudad, temperatura=temperatura, velocidad_viento=velocidad_viento, latitud=latitud, longitud=longitud, descripcion=descripcion, main=main)
if __name__ == '__main__':
    app.run(port = 8000)
