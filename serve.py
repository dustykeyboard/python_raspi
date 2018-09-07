#!/usr/bin/python

from os import listdir
from os.path import isfile, join
from flask import Flask, jsonify, render_template, request, send_from_directory


app = Flask(__name__)
path = "/home/pi/cameraroll"


@app.route("/")
def listPhotos():
	photos = [join("cameraroll/", photo) for photo in listdir(path) if isfile(join(path, photo))]
	photos.sort(reverse=True)
	photos = photos[0:20]
	return render_template("photobooth.html", photos=photos), 200


@app.route("/latest.json")
def listPhotosJson():
	photos = [join("cameraroll/", photo) for photo in listdir(path) if isfile(join(path, photo))]
	photos.sort(reverse=True)
	photos = photos[0:20]
	return jsonify({'photos':photos}), 200


@app.route("/static/<path:path>")
def send_static(path):
	return send_from_directory("static", path)


@app.route("/cameraroll/<path:path>")
def send_cameraroll(path):
	return send_from_directory("/home/pi/cameraroll", path)


app.run(host='0.0.0.0', port=8080)
