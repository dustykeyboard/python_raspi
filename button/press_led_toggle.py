#!/usr/bin/python

from gpiozero import Button, LED
from signal import pause

button = Button(2)
led = LED(17)

def toggle_led():
	led.toggle()

button.when_pressed = toggle_led

pause()
