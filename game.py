# TODO add player turn in-game
# TODO fix rebuild of interface every damn turn
# TODO strategies
# TODO won screen + stats
# TODO interface not responding if i dont move cursor on it -> maybe insert FPS?
# TODO random first move?
# TODO detect stuck -> add rule that is not allowed to rest in an opponent triangle
# TODO reorder functions files

import pygame as pg
# import numpy as np
import sys
from pygame.locals import *
import random
from engine import *
from engine_2 import *
from gui import *


def main():

    board = build_board()
    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
    player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_sets()
    player1_invalid_home, player2_invalid_home, player3_invalid_home, player4_invalid_home, player5_invalid_home, player6_invalid_home = build_invalid_homes_sets(player1_set, player2_set, player3_set, player4_set, player5_set, player6_set, player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj)
    player1_i_set, player2_i_set, player3_i_set, player4_i_set, player5_i_set, player6_i_set = build_invalid_set()

    display_surface = init_board()

    # player decision
    player_turn = random.randint(1, 6)

    # game start
    game_over = False

    while True:

        draw_board(board, display_surface)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and not game_over:
                if event.key == ord("a"):

                    # change player turn
                    player_turn = player_turn + 1
                    if player_turn == 7:
                        player_turn = 1

                    print("Player", player_turn)

                    # consider the pieces of the player of this turn
                    set_pieces = assign_set(player_turn, player1_set, player2_set, player3_set, player4_set,
                                            player5_set, player6_set)

                    # identify homes of the player of this turn
                    invalid_homes_set = assign_invalid_homes_set(player_turn, player1_invalid_home, player2_invalid_home, player3_invalid_home, player4_invalid_home, player5_invalid_home, player6_invalid_home)

                    # assign objective set of positions
                    obj_set = assign_obj_set(player_turn, player1_obj, player2_obj, player3_obj, player4_obj,
                                             player5_obj, player6_obj)

                    # assign invalid set
                    invalid_set = assign_invalid_set(player_turn, player1_i_set, player2_i_set, player3_i_set,
                                                     player4_i_set, player5_i_set, player6_i_set)

                    # find all legal moves given a piece set of a player
                    #all_legal_moves = find_all_legal_moves(board, set_pieces, obj_set, invalid_set, invalid_homes_set)
                    all_legal_moves = find_all_legal_moves(board, set_pieces, obj_set, invalid_homes_set)

                    move = all_legal_moves[0]
                    [x, y] = move[0]
                    print('Tesssssssst:', board[x][y])

                    # choose the best move
                    # best_move_n = random.randint(0, all_legal_moves.__len__() - 1)
                    # best_move = all_legal_moves[best_move_n]
                    best_move = find_best_move(board, all_legal_moves, obj_set, player_turn, set_pieces, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set)
                    print("player:", player_turn, "best move:", best_move)

                    # highlight the move chosen
                    highlight_best_move(best_move, display_surface)
                    pg.display.update()

                    # do the best move
                    board, set_pieces = do_move(board, best_move, set_pieces)

                    # update set
                    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                        update_player_set(set_pieces, player_turn, player1_set, player2_set, player3_set, player4_set,
                                          player5_set, player6_set)

                    # remove highlighted move
                    # remove_highlight(best_move, display_surface)

                    # update the board

                    # check if the player has won
                    game_over = check_win(set_pieces, obj_set)

                    # pg.display.update()


if __name__ == '__main__':
    main()
