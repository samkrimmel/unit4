#Sam Krimmel
#3/26/18
#warmup11.py - write a function that returns True if a number is prime and false otherwise

def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
    
print(prime(5903840932))