#Sam Krimmel
#3/29/18
#recursionDemo.py - recursive version of countdown.py

def countdownr(n):
    if n == 0: #easiest case (base case)
        print('BOOM!')
    else: #function that calls itself (recursive step)
        print(n)
        countdownr(n-1)

countdownr(23)