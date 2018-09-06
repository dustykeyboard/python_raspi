import time
import picamera

PATH = "/home/pi/cameraroll"

def capture():
	filename = "{}/{}.jpg".format(PATH, time.strftime('%Y-%m-%d_%H-%M-%S'))
	print("Capturing: {}".format(filename)
	camera.capture(filename)

def capture_burst():
	# Capture 4 photos, 2 seconds apart
	with picamera.PiCamera() as camera:
		camera.resolution = (1080, 1080)
		camera.start_preview()

		for loop in range(0, 4):
			# Camera warm-up time and time between shots
			time.sleep(2)
			capture()


if __name__ == '__main__':
	capture_burst()
