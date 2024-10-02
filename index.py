
import os
from datetime import datetime

from flask import Flask, render_template
from whitenoise import WhiteNoise


app = Flask(__name__, root_path="app",  template_folder="views")
static_dir = os.path.join(os.path.dirname(__file__), 'static')
app.wsgi_app = WhiteNoise(app.wsgi_app, root="app", prefix='static/')
app.config["start"] = datetime.now()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
