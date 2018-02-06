import random
import numpy as np

ciao = [[[0, 12], [1, 11]], [[1, 13], [1, 13]]]

print(ciao)
print(ciao[0])
print(ciao[0][0])
print(ciao[0][0][0])

miao = [[[4, 18], [4, 16]], [[4, 18], [5, 17]], [[4, 20], [4, 16]], [[4, 20], [6, 18]], [[5, 19], [5, 17]], [[5, 19], [6, 18]], [[5, 21], [5, 17]], [[5, 21], [7, 19]], [[6, 20], [6, 18]], [[6, 20], [7, 19]], [[6, 22], [6, 18]], [[6, 22], [8, 20]], [[7, 21], [7, 19]], [[7, 21], [8, 20]]]

num = 5

print(miao.__len__())
print(miao[13])




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
