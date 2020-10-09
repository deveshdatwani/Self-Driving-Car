import RPi.GPIO as gpio
from getch import getch

import time

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

while True:
	user_in = getch()
	if ord(user_in) == ord('w'):
		gpio.output(7, True)
		gpio.output(11, False)
		gpio.output(13, True)
		gpio.output(15, False)
		time.sleep(0.1)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(13, False)
		gpio.output(15, False)
	if ord(user_in) == ord('d'):
		gpio.output(7, True)
		gpio.output(11, False)
		gpio.output(13, False)
		gpio.output(15, True)
		time.sleep(0.1)
		gpio.output(7, False)
		gpio.output(15, False)
	if ord(user_in) == ord('a'):
		gpio.output(7, False)
		gpio.output(11, True)
		gpio.output(13, True)
		gpio.output(15, False)
		time.sleep(0.1)
		gpio.output(11, False)
		gpio.output(13, False)
	if ord(user_in) == ord('s'):
		gpio.output(7, False)
		gpio.output(11, True)
		gpio.output(13, False)
		gpio.output(15, True)
		time.sleep(0.1)
		gpio.output(15, False)
		gpio.output(11, False)
