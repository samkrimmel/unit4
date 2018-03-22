#Sam Krimmel
#3/22/18
#monkeyBanana.py - the best game ever

from ggame import *

if __name__ == '__main__':
    
    #colors
    green = Color(0x006600,1)
    
    jungleBox = RectangleAsset(800,500,LineStyle(1,green),green)
    
    Sprite(JungleBox)
    
    App().run()
