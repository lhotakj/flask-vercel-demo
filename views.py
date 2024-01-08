from Cors import App
from flask import request

@App.route("/", methods=["GET"])
def heartbeat():
    if request.method == "GET":
        return "Hello world!"

@App.route("/heartbeat", methods=["GET"])
def heartbeat():
    if request.method == "GET":
        return "OK"
