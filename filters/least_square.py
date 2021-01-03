import math
import numpy as np
from numpy.linalg import inv
import RPi.GPIO as GPIO
import time
import pandas as pd
import matplotlib.pyplot as plt

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Set up pins
TRIG = 12
ECHO = 11
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
print('Setting up pins')
distance = []

# Calculate a batch of 200 readings
for i in range(1000):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,True)
    time.sleep(0.1)
    GPIO.output(TRIG,False)
    while GPIO.input(11) == 0:
        start = time.time()
    while GPIO.input(11) == 1:
        end = time.time()
    print('reading number %d' % i)
    
    tl = (end - start) * 34300 / 2
    distance.append(tl)
    GPIO.cleanup()

# Run least square method on the 200 batch readings 
# The model is 
# distance  = H (jacobina matrix) x x (parameter) + e (error)  

#distance = np.ones((200,1),dtype="float")
H = np.ones((1000,1),dtype="float")
x_hat = inv(H.T.dot(H)).dot(H.T.dot(distance))
print('The distance is %f' % x_hat)

# Plotting the readings as a distribution curve

x = pd.DataFrame(distance, columns=['reading'])
plt.hist(x['reading'].values, bins=50)
plt.show()
