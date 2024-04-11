import requests
import math
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os



load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    ciudad = "Tequila"  # Ciudad por defecto
    url = os.getenv("URL")
    url = url.format(ciudad)
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

@app.route('/clima', methods=['POST'])
def clima():
    ciudad = request.form['ciudad']
    url = os.getenv("URL")
    url = url.format(ciudad)
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
