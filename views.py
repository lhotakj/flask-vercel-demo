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
        start = app.config["start"]

        import datetime
        data2 = datetime.datetime.now()

        diff = data2 - start

        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        return f"OK<br><u>uptime</u>: {days} days, {hours} hours, {minutes}, minutes, {seconds} seconds"
