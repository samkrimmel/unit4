#Sam Krimmel
#3/28/18
#distanceFunction.py - makes the distance formula a function

from math import sqrt

def distance(X1,Y1,X2,Y2):
    return sqrt(((X2-X1)**2)+((Y2-Y1)**2))

print(distance(3,4,-5,2))
