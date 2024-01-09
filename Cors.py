from flask import Flask
from flask_cors import CORS
from whitenoise import WhiteNoise

App = Flask(__name__)
cors = CORS(App)
App.wsgi_app = WhiteNoise(App.wsgi_app, root="app/",prefix="/")
