import Cors
import os
import time
import views

app = Cors.App
app.config["start"] = time.time()
app.config["a"] = "a"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
