import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello world!"


@app.route('/heartbeat')
def hello():
    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
