import RPi.GPIO as GPIO
import math
import time

TRIG = 12
ECHO = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.1)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    distance = (end - start) * 34300 / 2 

    print(distance)
