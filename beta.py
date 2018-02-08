
# import pygame as pg
# import numpy as np
import sys
from pygame.locals import *
import random
from engine import *
from gui import *

FPS = 30


def main():

    fps_lock = pg.time.Clock()

    board = build_board()
    # player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_boards(board)
    player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_sets()
    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()

    display_surface = init_board()

    # player decision
    player_turn = random.randint(1, 6)

    # game start
    game_over = False

    while True and not game_over:

        draw_board(board, display_surface)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()


            # change player turn
            player_turn = player_turn + 1
            if player_turn == 7:
                player_turn = 1

            # consider the pieces of the player of this turn
            set_pieces = assign_set(player_turn, player1_set, player2_set, player3_set, player4_set,
                                    player5_set, player6_set)

            # assign objective set of positions
            # obj_board = assign_obj_board(player_turn, player1_obj, player2_obj, player3_obj, player4_obj,
            #                              player5_obj, player6_obj)
            obj_set = assign_obj_set(player_turn, player1_obj, player2_obj, player3_obj, player4_obj,
                                     player5_obj, player6_obj)

            # find all legal moves given a piece set of a player
            all_legal_moves = find_all_legal_moves(board, set_pieces, obj_set)

            # check if a player has won ------------------------------------------WRONG!
            if not all_legal_moves:
                print('Player', player_turn, 'won')
                pg.time.wait(60000)

            # choose the best move
            # best_move_n = random.randint(0, all_legal_moves.__len__() - 1)
            # best_move = all_legal_moves[best_move_n]
            best_move = find_best_move(board, all_legal_moves, obj_set, set_pieces, player_turn)
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

            #pg.time.wait(600)
            fps_lock.tick(FPS)


if __name__ == '__main__':
    main()
