"""
This is a class object to store data from sensors
It contains 3 parameters (measurements from magnetometer):
    x: magnetic field measured alone x axis (unit: uT)
    y: magnetic field measured alone y axis (unit: uT)
    z: magnetic field measured alone z axis (unit: uT)
"""


import math
import numpy as np

class emi_measurement:
    # variables to store measurement
    x = math.inf
    y = math.inf
    z = math.inf
    
    def __init__(self, emi_x = math.inf, emi_y = math.inf, emi_z = math.inf):
        self.x = emi_x
        self.y = emi_y
        self.z = emi_z

# overloading the operators
    def __add__(self, other):
        emi_x = self.x + other.x
        emi_y = self.y + other.y
        emi_z = self.z + other.z
        return emi_measurement(emi_x, emi_y, emi_z)
    
    def __sub__(self, other):
        emi_x = self.x - other.x
        emi_y = self.y - other.y
        emi_z = self.z - other.z
        return emi_measurement(emi_x, emi_y, emi_z)
    
    def __truediv__(self, num):
        emi_x = self.x / num
        emi_y = self.y / num
        emi_z = self.z / num
        return emi_measurement(emi_x, emi_y, emi_z)
    
    def __mul__(self, num):
        emi_x = self.x * num
        emi_y = self.y * num
        emi_z = self.z * num
        return emi_measurement(emi_x, emi_y, emi_z)
    
    def __str__(self):
        return  "({0},{1},{2})".format(self.x, self.y, self.z)   

# define necessary functions    
    def get_magnitude(self):
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
'''    
a = emi_measurement(1,1,1)
b = emi_measurement(1,1,1)
print(a+b)
print (a/2)
'''
