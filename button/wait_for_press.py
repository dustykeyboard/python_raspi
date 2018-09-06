from gpiozero import Button

button = Button(2)

print("Press the button")
button.wait_for_press()

print("You pressed the button")
