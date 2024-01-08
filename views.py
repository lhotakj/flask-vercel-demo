from Cors import App
from flask import request
from flask import current_app as app
import sys


@App.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        return f"<h1>Hello world!</h1><br />Running on {sys.version}"


@App.route("/heartbeat", methods=["GET"])
def heartbeat():
    if request.method == "GET":
        start: str = str(app.config["start"])
        return f"OK<br>{start}"
