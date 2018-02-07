import pygame as pg
import sys
from pygame.locals import *

import random
import numpy as np
from engine import build_board, assign_set, find_all_legal_moves, do_move, update_set
from gui import init_board, draw_board, highlight_best_move#, remove_highlight


def main():

    board = np.zeros((17, 25))
    board = build_board(board)

    player1_set = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
    player2_set = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
    player3_set = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
    player4_set = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]
    player5_set = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
    player6_set = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]

    display_surface = init_board()

    # player decision
    player_turn = random.randint(1, 6)

    while True:

        draw_board(board, display_surface)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == ord("a"):

                    set_pieces = assign_set(player_turn, player1_set, player2_set, player3_set, player4_set,
                                            player5_set, player6_set)

                    all_legal_moves = find_all_legal_moves(board, set_pieces)

                    best_move_n = random.randint(0, all_legal_moves.__len__() - 1)
                    best_move = all_legal_moves[best_move_n]
                    print("player:", player_turn, "best move:", best_move)

                    # my_move = find_best_move(board, all_legal_moves)

                    # highlight the move chosen
                    highlight_best_move(best_move, display_surface)
                    pg.display.update()

                    # do the best move
                    board, set_pieces = do_move(board, best_move, set_pieces)

                    # update set
                    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                        update_set(set_pieces, player_turn, player1_set, player2_set, player3_set, player4_set,
                                   player5_set, player6_set)

                    # remove highlighted move
                    # remove_highlight(best_move, display_surface)

                    # update the board

                    # change player turn
                    player_turn = player_turn + 1
                    if player_turn == 7:
                        player_turn = 1

                    #pg.display.update()


if __name__ == '__main__':
    main()
