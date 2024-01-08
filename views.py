from Cors import App
from flask import request
import json

data = []


# modified
@App.route("/", methods=["GET", "POST"])
def sample_api():
    if request.method == "POST":
        data.append(request.get_json())
    return json.dumps(data)

@App.route("/heartbeat", methods=["GET"])
def heartbeat():
    if request.method == "GET":
        return "OK"
