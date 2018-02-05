# TO DO
# 1. creare GUI per campo

import random
import numpy as np
from operations import build_board, assign_pieces

board = np.zeros((17, 25))

board = build_board(board)

# -1 = NOT_VALID_SPACE
# 0 = EMPTY_CELL
# 1 = PLAYER 1
# 2 = PLAYER 2
# 3 = PLAYER 3
# 4 = PLAYER 4
# 5 = PLAYER 5
# 6 = PLAYER 6

player1_set = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3,9], [3, 11], [3, 13], [3, 15]]
player2_set = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
player3_set = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
player4_set = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]
player5_set = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
player6_set = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6,2], [6, 4], [7, 3]]

# decidi player
turno_player = random.randint(1, 6)

while not match_end:

    set_pieces = assign_pieces(turno_player, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set)

    all_legal_moves[] = find_all_legal_moves(board, turno_player, set_pieces)
    # find_best_move(board, all_legal_moves[]) Returns: my_move
    # do_move(board, my_move) Throws: error ILLEGAL_MOVE Updates: board

    turno_player = turno_player + 1
    if turno_player == 7:
        turno_player = 1

print(board)
