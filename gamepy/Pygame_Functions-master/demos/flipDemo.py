# Demo of the flip parameters for transformSprite
# Use direction keys to flip horizontally or vertically
# Use space key to rotate

from pygame_functions import *

screenSize(1024, 768)
jurassic = makeSprite("/Users/leynilson_harden/Dropbox/Programação/PycharmProjects/python/gamepy/Pygame_Functions-master/demos/images/jurassic.jpg")
showSprite(jurassic)

angle = 0
hflip = False
vflip = False

while True:
    if keyPressed("space"):
        angle +=4
    if keyPressed("left") or keyPressed("right"):
        hflip = True
    else:
        hflip = False
    if keyPressed("up") or keyPressed("down"):
        vflip = True
    else:
        vflip = False
    transformSprite(jurassic, angle, 1, hflip, vflip)
    tick(30)

endWait()
