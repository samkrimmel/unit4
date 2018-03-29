#Sam Krimmel
#3/29/18
#warmup12.py - function that returns the GCF of two numbers.

def GCF(x,y):
    if x>y:
        for i in range((x+1),1,-1):
            if i%x == 0 and i%y == 0:
                return i
    else:
        for i in range((y+1),1,-1):
            if i%x == 0 and i%y == 0:
                return i
