#Sam Krimmel
#3/26/18
#localDemo.py - what is a local variables?

def f():
    x = 20           #x within the function exists only within the function (local variable)
    y = 200
    
x = 2
f()
print(x)
print(y)
