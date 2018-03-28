#Sam Krimmel
#3/28/18
#printSquares.py - prints out a grid of squares

def printSquares(vert,horz):
    for i in range(0,vert):
        print(horz*'+--' + '+')
        print(horz*'|  ' + '|')
    print(horz*'+--' + '+')

printSquares(2,4)