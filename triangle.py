#Sam Krimmel
#3/29/18
#triangle.py - computes area of triangle given vertex coordinates

from math import sqrt

def distance(x1,y1,x2,y2):
    return sqrt(((x2-x1)**2)+((y2-y1)**2))

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

def triangle(x1,y1,x2,y2,x3,y3):
    side1 = distance(x1,y1,x2,y2)
    side2 = distance(x1,y1,x3,y3)
    side3 = distance(x2,y2,x3,y3)
    s = 0.5*(side1 + side2 + side3)
    return sqrt(s*((s-side1)*(s-side2)*(s-side3)))

print(triangle(x1,y1,x2,y2,x3,y3))

    
