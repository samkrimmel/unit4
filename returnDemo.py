#Sam Krimmel
#3/19/18
#returnDemo.py - how to use return

from random import randint

def randEven(low,high):
    n = randint(low,high)
    while n%2 != 0:
        n = randint(low,high)
    return n
    
print("your even nmbers are", randEven(11,99),randEven(11,99),randEven(11,99)) #test of randEven
num4 = randEven(1000,2000)

if num4 < 1500:
    print(num4, "is pretty big")
else:
    print(num4, "is really big")