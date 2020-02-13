#!flask/bin/python
import requests
import os
import sys
import logging
import datetime
import time
import socket

from flask import Flask, request
from flask_prometheus import monitor

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

hostname = socket.gethostname()
if "MESSAGE" in os.environ:
  message = os.getenv("MESSAGE")
else:
  message = "Hello, Avinash"

@app.route('/')
def index():
  timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))	
  app.logger.debug("Finished at: " + timestamp)
  return timestamp + " " + message + "\n"

if __name__ == '__main__':
    misbehave = False
    monitor(app, port=8000)
    app.run(host='0.0.0.0', port=8080)
