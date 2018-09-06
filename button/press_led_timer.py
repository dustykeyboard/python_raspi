#!/usr/bin/python

from gpiozero import Button, LED
from signal import pause
import time

button = Button(2)
led = LED(17)
busy = False

def ready():
	for i in range(0,3):
		led.on()
		time.sleep(0.1)
		led.off()
		time.sleep(0.1)


def pulse_led():
	global busy
	if busy:
		return

	busy = True
	led.on()
	time.sleep(1)
	led.off()
	busy = False

button.when_pressed = pulse_led

ready()

pause()
