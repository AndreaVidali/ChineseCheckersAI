# TODO add player turn in-game
# TODO fix rebuild of interface every damn turn
# TODO won screen + stats
# TODO interface not responding if i dont move cursor on it -> maybe insert FPS?
# TODO reorder functions files

# import numpy as np
import sys
from pygame.locals import *
import random
from engine import *
from engine_2 import *
from gui import *


def main():

    # win counters
    p1_win = 0
    p2_win = 0
    p3_win = 0
    p4_win = 0
    p5_win = 0
    p6_win = 0

    # stuck counter
    stuck_counter = 0

    board = build_board()
    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
    player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_sets()
    player1_invalid_home, player2_invalid_home, player3_invalid_home, player4_invalid_home, player5_invalid_home, \
        player6_invalid_home = build_invalid_homes_sets(player1_set, player2_set, player3_set, player4_set,
                                                        player5_set, player6_set, player1_obj, player2_obj,
                                                        player3_obj, player4_obj, player5_obj, player6_obj)

    display_surface = init_board()

    # player decision
    player_turn = random.randint(1, 6)

    # game start
    game_over = False
    first_turn = True
    first_round = True
    save_first_p = 100

    while True:

        draw_board(board, display_surface)

        for event in pg.event.get():

            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == ord("r"):

                    board = build_board()
                    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
                    player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_sets()
                    player1_invalid_home, player2_invalid_home, player3_invalid_home, player4_invalid_home, \
                        player5_invalid_home, player6_invalid_home = build_invalid_homes_sets(
                            player1_set, player2_set, player3_set, player4_set, player5_set, player6_set, player1_obj,
                            player2_obj, player3_obj, player4_obj, player5_obj, player6_obj)
                    display_surface = init_board()

                    # player decision
                    player_turn = random.randint(1, 6)

                    draw_board(board, display_surface)
                    pg.display.update()

                    # game restart
                    game_over = False
                    first_turn = True
                    first_round = True
                    save_first_p = 100

                    break

            if event.type == pg.KEYDOWN and not game_over:
                if event.key == ord("a"):

                    # change player turn
                    player_turn = player_turn + 1
                    if player_turn == 7:
                        player_turn = 1

                    # randomize first move
                    if player_turn == save_first_p:
                        first_round = False
                    if first_turn:
                        save_first_p = player_turn
                        first_turn = False

                    # print("Player", player_turn)

                    # consider the pieces of the player of this turn
                    set_pieces = assign_set(player_turn, player1_set, player2_set, player3_set, player4_set,
                                            player5_set, player6_set)

                    # identify homes of the player of this turn
                    invalid_homes_set = assign_invalid_homes_set(player_turn, player1_invalid_home,
                                                                 player2_invalid_home, player3_invalid_home,
                                                                 player4_invalid_home, player5_invalid_home,
                                                                 player6_invalid_home)

                    # assign objective set of positions
                    obj_set = assign_obj_set(player_turn, player1_obj, player2_obj, player3_obj, player4_obj,
                                             player5_obj, player6_obj)

                    # find all legal moves given a piece set of a player
                    # all_legal_moves = find_all_legal_moves(board, set_pieces, obj_set, invalid_set, invalid_homes_set)
                    all_legal_moves = find_all_legal_moves(board, set_pieces, obj_set, invalid_homes_set)

                    # choose the best move
                    if first_round:
                        best_move_index = random.randint(0, len(all_legal_moves) - 1)
                        best_move = all_legal_moves[best_move_index]
                    else:
                        best_move = find_best_move(board, all_legal_moves, obj_set, player_turn, set_pieces,
                                                   player1_set, player2_set, player3_set, player4_set, player5_set,
                                                   player6_set)
                    # print("player:", player_turn, "best move:", best_move)

                    if best_move is None:

                        game_over = True
                        stuck_counter = stuck_counter + 1
                        print('Game stuck counter:', stuck_counter)
                        print('[]------------------[]')

                        break

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

                    if game_over:
                        if player_turn == 1:
                            p1_win = p1_win + 1
                        if player_turn == 2:
                            p2_win = p2_win + 1
                        if player_turn == 3:
                            p3_win = p3_win + 1
                        if player_turn == 4:
                            p4_win = p4_win + 1
                        if player_turn == 5:
                            p5_win = p5_win + 1
                        if player_turn == 6:
                            p6_win = p6_win + 1
                        print('Player 1 wins:', p1_win)
                        print('Player 2 wins:', p2_win)
                        print('Player 3 wins:', p3_win)
                        print('Player 4 wins:', p4_win)
                        print('Player 5 wins:', p5_win)
                        print('Player 6 wins:', p6_win)
                        print('[]------------------[]')

                    # pg.display.update()


if __name__ == '__main__':
    main()
