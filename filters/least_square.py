import math
import numpy as np
from numpy.linalg import inv

# Calculate a batch of 200 readings

for i in range(200):
    a = 1



# Run least square method on the 200 batch readings 
# The model is 
# distance  = H (jacobina matrix) x x (parameter) + e (error)  

distance = np.ones((200,1),dtype="float")
H = np.ones((200,1),dtype="float")
x_hat = inv(H.T.dot(H)).dot(H.T.dot(distance))
print('The sitance is %s', x_hat)
