#Sam Krimmel
#3/30/18
#multiply.py - multiplication practice with encouragement

from random import randint

def encourage():
    message = randint(1,10)
    if message == 1:
        message = "Way to go!"
    elif message == 2:
        message = "Multiply those numbers!"
    elif message == 3:
        message = "Yea!"
    elif message == 4:
        message = "wOw!"
    elif message == 5:
        message = "That's a number!"
    print(message)
    
numWrong = 0
while True:
    num1 = randint(1,12)
    num2 = randint(1,12)
    answer = int(input('What is ' + str(num1) + ' + ' + str(num2) + '? '))
    if answer =! num1 + num2:
        print('WRONG!!')
        print('The answer was', num1+num2)
        encourage()
        
