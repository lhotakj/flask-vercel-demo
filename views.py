from Cors import App
from flask import request
from flask import current_app as app
import os


@App.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        return f"<h1>Hello world!</h1><br />Running on {os.name}"


@App.route("/heartbeat", methods=["GET"])
def heartbeat():
    if request.method == "GET":
        start: str = str(app.config)
        return f"OK {start}"
