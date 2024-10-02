import sys
from datetime import datetime
from flask import current_app as app
from flask import request


@app.route("/", methods=["GET"])
def root() -> str:
    """
    Returns string for /
    @return: string
    """
    if request.method == "GET":
        return f"<h1>Hello from Vercel!</h1>" \
               f"<img src='/static/img/logo_vercel.png' style='width:200px' /><br>" \
               f"<br />Running on {sys.version}"


@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    if request.method == "GET":
        start = app.config["start"]
        now = datetime.now()
        diff = now - start
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        return f"<h1>OK</h1><br><u>uptime</u>: {days} days, {hours} hours, {minutes}, minutes, {seconds} seconds"
