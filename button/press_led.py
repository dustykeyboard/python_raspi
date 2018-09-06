from gpiozero import Button, LED

button = Button(2)
led = LED(17)

while True:
	if button.is_pressed():
		led.on()
	else:
		led.off()
