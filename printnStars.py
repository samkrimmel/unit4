#Sam Krimmel
#3/19/18
#printnStars.py - takes integer and prints that many lines of stars

def printnStars(num):
    for i in range(1,num):
        print(' '*((num-1)-i),' *'*i)

printnStars(6)
