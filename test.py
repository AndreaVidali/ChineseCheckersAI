import random
import numpy as np

ciao = [0, 12]
while()
[x, y] = ciao

print(ciao)
#
# player5_set = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
#
# x = 99
# y = 48
# xx = 10
# xy = 4
#
# print(player5_set)
# player5_set.remove([xx, xy])
# print(player5_set)
# player5_set.append([x, y])
# print(player5_set)
#
# set_pieces = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
#
# start_x = 2
# start_y = 14
# end_x = 4
# end_y = 16
#
# print("originale:", set_pieces, "toRemove:", [start_x, start_y])
# set_pieces.remove([start_x, start_y])
# print("remove:", set_pieces, "toAppend:", [end_x, end_y])
# set_pieces.append([end_x, end_y])
# print("append:", set_pieces)



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

# import numpy as np
# board = np.zeros((5, 7))
#
# print(board)
#
# new_board = np.full(board.shape, 15)

print(new_board)
print(board.shape)
