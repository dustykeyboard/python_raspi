#!/usr/bin/python

import time
from picamera import PiCamera
from gpiozero import Button, LED
from signal import pause

button = Button(2)
led = LED(17)
PATH = "/home/pi/cameraroll"
busy = False
camera = PiCamera()
camera.resolution = (1080, 1080)


def ready():
	for i in range(0,3):
		led.on()
		time.sleep(0.1)
		led.off()
		time.sleep(0.1)


def capture(timestamp, loop):
	led.on()
	time.sleep(0.3)
	filename = "{}/{}_{}.jpg".format(PATH, timestamp, loop)
	camera.capture(filename)
	time.sleep(0.2)
	led.off()


# Capture 4 photos, 2 seconds apart
def capture_burst():
	global busy
	if not busy:
		busy = True
		timestamp = time.strftime('%Y-%m-%d_%H%M%S')
		for loop in range(0, 4):
			capture(timestamp, loop)
			time.sleep(2)
		
		busy = False



if __name__ == '__main__':
	time.sleep(2)
	button.when_pressed = capture_burst
	ready()
	pause()
