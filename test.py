import random
import numpy as np

ciao = [[[0, 12], [1, 11]], [[1, 13], [1, 13]]]

print(ciao)
print(ciao[0])
print(ciao[0][0])
print(ciao[0][0][0])

nb = 3
nbc = -2

if 0 <= nb <= 16:
    print(nb)

if nbc in [0, 16]:
    print(nbc)


nb = [3, 4]
print(nb[1])

print(abs(-2))

# i = 0
#
# for x, y in ciao:
#
#     x = x + 3
#     ciao[i] = [x, y]
#     i = i + 1
#
# print(ciao)
#
# random1 = random.randint(1, 6)
# print(random1)

# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
#
# FPS = 30
# fpsClock = pygame.time.Clock()
#
# # set up the window
# DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
# pygame.display.set_caption('Animation')
#
# WHITE = (255, 255, 255)
# catImg = pygame.image.load('cat.png')
# catx = 10
# caty = 10
# direction = 'right'
#
# while True:  # the main game loop
#     DISPLAYSURF.fill(WHITE)
#
#     if direction == 'right':
#         catx += 5
#         if catx == 280:
#             direction = 'down'
#     elif direction == 'down':
#         caty += 5
#         if caty == 220:
#             direction = 'left'
#     elif direction == 'left':
#         catx -= 5
#         if catx == 10:
#             direction = 'up'
#     elif direction == 'up':
#         caty -= 5
#         if caty == 10:
#             direction = 'right'
#
#     DISPLAYSURF.blit(catImg, (catx, caty))
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pygame.display.update()
#     fpsClock.tick(FPS)
