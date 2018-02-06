
import pygame as pg
import sys
from pygame.locals import *

pg.init()
DISPLAYSURF = pg.display.set_mode((1024, 768), 0, 32)

pg.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF.fill(WHITE)
pg.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pg.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pg.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pg.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pg.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pg.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pg.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pg.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
