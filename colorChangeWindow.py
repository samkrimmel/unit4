#Sam Krimmel
#3/19/18
#colorChangeWindow.py - pops up window that changes to a random color every time you click it

from random import randint

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
yellow = Color(0xFFE500,1)
blue = Color(0x4DA9F9,1)
red = Color(0xFF0F0F,1)
green = Color(0x08D63F,1)

def mouseClick(event):
    num = randint(1,7)
    if num == 1:
        color = white
    elif num ==2:
        color = black
    elif num ==3:
        color = yellow
    elif num == 4:
        color = blue
    elif num == 5:
        color = red
    else:
        color = green
    window = RectangleAsset(300,60,color)
    Sprite(window)
    App().run()
