from flask import Flask 

app = Flask(__name__)


BASE_URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=ca4c035917ed4142ab395429170207&format=json'

from app import weather 
