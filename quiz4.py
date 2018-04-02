#Sam Krimmel
#4/2/18
#quiz4.py

def count(num):
    for i in range(1,num+1):
        print(i)

def excitedPrint(word):
    print(word.upper(),'!!!')

def firstLetter(word):
    for ch in word:
        return ch

def repeats(a,b,c):
    if a==b or a==c:
        return True
    else:
        return False
