#Sam Krimmel
#3/19/18
#countdownn.py - takes integer and counts down to zero from that number

def countdownn(num):
    for i in range (num,-1,-1):
    if i == 0:
        print('BOOM!')
    else:
        print(i)
