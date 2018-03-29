#Sam Krimmel
#3/29/18
#triangle.py - computes area of triangle given vertex coordinates

from math import sqrt

def triangle(x1,y1,x2,y2,x3,y3):
    side12 = sqrt(((x2-x1)**2)+((y2-y1)**2))
    side23 = sqrt(((x3-x2)**2)+((y3-y2)**2))
    side13 = sqrt(((x3-x1)**2)+((y3-y1)**2))
    s = 0.5*(side12 + side23 + side13)
    return float(sqrt(s((s-side12)(s-side23)(s-side13))))
    
print(triangle(3,4,-5,2,-7,1))

    
