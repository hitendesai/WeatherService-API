from flask import Flask

app = Flask(__name__)

key = "???"
# Use your own API Key above. something like ca4c035917ed4142ab395429170206

BASE_URL = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=" + key + "&format=json"

from app import weather
