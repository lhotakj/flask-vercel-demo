# Simple Web Application running on Vercel

This is a simple web application using [Python Flask](http://flask.pocoo.org/) and hosted on Vercel
see https://flask.lhotak.net/
and https://flask.lhotak.net/heartbeat
 
  Below are the steps required to get this working on a base linux system.
  
  - Install Python3
  - Install and Configure Web Server
  - Setup Vercel
   
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
https://github.com/harshan1996/flask-vercel/blob/main/backend/views.py
https://vercel.com/docs/functions/serverless-functions/runtimes/python