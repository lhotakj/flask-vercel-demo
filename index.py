import Cors
import os
import time
import views

app = Cors.App

if __name__ == "__main__":
    app.config["start"] = time.time()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
