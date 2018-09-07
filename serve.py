#!/usr/bin/python

import os
from flask import Flask, request, send_from_directory


app = Flask(__name__)


@app.route("/")
def listPhotos():
	return "Photobooth", 200


@app.route("/static/<path:path>")
def send_static(path):
	return send_from_directory("static", path)


@app.route("/cameraroll/<path:path>")
def send_cameraroll(path):
	return send_from_directory("/home/pi/cameraroll", path)


app.run(host='0.0.0.0', port=8080, debug=True)
