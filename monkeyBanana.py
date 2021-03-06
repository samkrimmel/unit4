#Sam Krimmel
#3/22/18
#monkeyBanana.py - the best game ever

from random import randint
from ggame import *

#constants
ROWS = 24
COLS = 50
CELL_SIZE = 20

#moves monkey right one cell if possible
def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves monkey up one cell if possible
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves monkey down one cell if possible
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves monkey left one cell if possible
def moveLeft(event):
    if monkey.x > 0 :
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves banana to random position and resets timer
def moveBanana():
    data['frames'] = 0
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    
#increase score and display new text at the bottom of the screen
def updateScore():
    data['score'] += 10
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))

#keeps track of how many frames have happened and moves banana if frames exceed 300 since last move
def step():
    data['frames'] += 1
    if data['frames'] == 300:
        moveBanana()
    
#sets up and runs the game
if __name__ == '__main__':
    
    #hold variables in a dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    #colors
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xffff00,1)
    
    #graphics
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().run(step)
