#Sam Krimmel
#3/22/18
#monkeyBanana.py - the best game ever

from ggame import *

#constants
ROWS = 26
COLS = 50
CELL_SIZE = 20

if __name__ == '__main__':
    
    #colors
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    
    Sprite(jungleBox)
    Sprite(monkeyBox)
    
    App().run()
