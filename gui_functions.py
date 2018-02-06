import pygame as pg
# import sys
# from pygame.locals import *

# -1 = NOT_VALID_SPACE
BACKGROUND = (242, 213, 171)
# 0 = EMPTY_CELL
EMPTY_CELL = (183, 162, 130)
# 1 = PLAYER 1
PLAYER1_BLACK = (0, 0, 0)
# 2 = PLAYER 2
PLAYER2_WHITE = (255, 255, 255)
# 3 = PLAYER 3
PLAYER3_RED = (255, 0, 0)
# 4 = PLAYER 4
PLAYER4_BLUE = (0, 0, 255)
# 5 = PLAYER 5
PLAYER5_GREEN = (0, 255, 0)
# 6 = PLAYER 6
PLAYER6_YELLOW = (255, 255, 0)

# costants of the board
H_MARGIN_DISTANCE = 20
V_MARGIN_DISTANCE = 20
CIRCLE_RADIUS = 20
H_SPACING = 8
V_SPACING = 1
WINDOW_WIDTH = (H_MARGIN_DISTANCE * 2) + (CIRCLE_RADIUS * 13 * 2) + (H_SPACING * 12)
WINDOW_HEIGHT = (V_MARGIN_DISTANCE * 2) + (CIRCLE_RADIUS * 17 * 2) + (V_SPACING * 16)


def init_board(board):
    pg.init()
    display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('Chinese Checkers AI')
    draw_board(board, display_surface)


def draw_board(board, display_surface):

    display_surface.fill(BACKGROUND)

    y_coord = V_MARGIN_DISTANCE + CIRCLE_RADIUS

    for row in range(0, 17):

        x_coord_long = H_MARGIN_DISTANCE + CIRCLE_RADIUS
        x_coord_short = int(H_MARGIN_DISTANCE + CIRCLE_RADIUS * 2 + (H_SPACING / 2))

        for circle_in_a_row in range(0, 13):
            if row % 2 == 0:

                board_value = board[row][circle_in_a_row * 2]
                color_circle(board_value, display_surface, x_coord_long, y_coord)

                x_coord_long = x_coord_long + CIRCLE_RADIUS * 2 + H_SPACING

            elif row % 2 != 0 and circle_in_a_row != 12:

                board_value = board[row][circle_in_a_row * 2 + 1]
                color_circle(board_value, display_surface, x_coord_short, y_coord)

                x_coord_short = x_coord_short + CIRCLE_RADIUS * 2 + H_SPACING

        y_coord = y_coord + CIRCLE_RADIUS * 2 + V_SPACING


def color_circle(board_value, display_surface, x_coord, y_coord):

    if board_value == -1:
        pg.draw.circle(display_surface, BACKGROUND, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 0:
        pg.draw.circle(display_surface, EMPTY_CELL, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 1:
        pg.draw.circle(display_surface, PLAYER1_BLACK, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 2:
        pg.draw.circle(display_surface, PLAYER2_WHITE, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 3:
        pg.draw.circle(display_surface, PLAYER3_RED, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 4:
        pg.draw.circle(display_surface, PLAYER4_BLUE, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 5:
        pg.draw.circle(display_surface, PLAYER5_GREEN, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 6:
        pg.draw.circle(display_surface, PLAYER6_YELLOW, (x_coord, y_coord), CIRCLE_RADIUS, 0)
