# Simple Web Application running hosted on Vercel

A simple web application demo of [Python Flask](https://flask.palletsprojects.com/) hosted on free plan (hobby)
on [Vercel Serverless Functions](https://vercel.com/).
Demo can be seen at https://flask.lhotak.net/ and https://flask.lhotak.net/heartbeat

## Preamble

* If you want to use Vercel for hosting your production using
  a [hobby plan](https://vercel.com/docs/accounts/plans/hobby) be aware of certain limitations.
* Vercel currently supports (only) [Python 3.9](https://www.python.org/downloads/release/python-390/) released back in
  2020 see [doc](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
* Vercel Serverless Functions is primarily built for Type Script web apps, don't expect much Python support
* In addition to the serverless functions Vercel platform a couple of serverless storage products:
    * Vercel KV: Durable Redis - preferred option of key-value data
    * Vercel Postgres: Serverless SQL - preferred option when relation database is required
    * Vercel Blob: Large file storage
    * Vercel Edge Config: Global, low-latency data store
* But it's free, so why not to try it out?

## Flask extensions
* [CORS](https://flask-cors.readthedocs.io/en/latest/) - handling Cross Origin Resource Sharing 
* [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) - simplified static file serving without relying on Nginx


## 1. Install Python 3

Ubuntu 22.04 and Python

    sudo apt-get install -y -q python3 python3-setuptools python3-dev build-essential

## 2. Install and Configure Web Server

Install Python Flask dependency

    pip install -r ./requirements.txt

- Copy app.py or download it from source repository

## 3. Start Web Server

Start web server

    FLASK_APP=app.py flask run --host=0.0.0.0

## 4. Test

Open a browser and go to URL

    http://<IP>:5000/                           => Hello world
    http://<IP>:5000/heartbeat                  => ok

## Credits

* https://github.com/harshan1996/flask-vercel/blob/main/backend/views.py
* https://vercel.com/docs/functions/serverless-functions/runtimes/python
