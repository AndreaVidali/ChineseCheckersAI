def build_board(board):

    board[:][:] = -1

    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9] = 1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

    board[4][18] = 2
    board[4][20] = 2
    board[4][22] = 2
    board[4][24] = 2
    board[5][19] = 2
    board[5][21] = 2
    board[5][23] = 2
    board[6][20] = 2
    board[6][22] = 2
    board[7][21] = 2

    board[9][21] = 3
    board[10][20] = 3
    board[10][22] = 3
    board[11][19] = 3
    board[11][21] = 3
    board[11][23] = 3
    board[12][18] = 3
    board[12][20] = 3
    board[12][22] = 3
    board[12][24] = 3

    board[13][9] = 4
    board[13][11] = 4
    board[13][13] = 4
    board[13][15] = 4
    board[14][10] = 4
    board[14][12] = 4
    board[14][14] = 4
    board[15][11] = 4
    board[15][13] = 4
    board[16][12] = 4

    board[9][21 - 18] = 5
    board[10][20 - 18] = 5
    board[10][22 - 18] = 5
    board[11][19 - 18] = 5
    board[11][21 - 18] = 5
    board[11][23 - 18] = 5
    board[12][18 - 18] = 5
    board[12][20 - 18] = 5
    board[12][22 - 18] = 5
    board[12][24 - 18] = 5

    board[4][18 - 18] = 6
    board[4][20 - 18] = 6
    board[4][22 - 18] = 6
    board[4][24 - 18] = 6
    board[5][19 - 18] = 6
    board[5][21 - 18] = 6
    board[5][23 - 18] = 6
    board[6][20 - 18] = 6
    board[6][22 - 18] = 6
    board[7][21 - 18] = 6

    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0

    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0

    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0

    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0

    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0

    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

    board[12][8] = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


def assign_pieces(turno_player, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set):

    set_player = player1_set

    if turno_player == 1:
        set_player = player1_set
    if turno_player == 2:
        set_player = player2_set
    if turno_player == 3:
        set_player = player3_set
    if turno_player == 4:
        set_player = player4_set
    if turno_player == 5:
        set_player = player5_set
    if turno_player == 6:
        set_player = player6_set

    return set_player


def find_all_legal_moves(board, player_turn, set_pieces):

    valid_moves = []
    for x, y in set_pieces:
        valid_moves = check_moves([x, y], 0, [x, y], None, valid_moves)


def check_moves(board, start, depth, origin, previous, valid_moves):

    [start_x, start_y] = start
    neighbors_list = neighbors(start)

    for x_v1, y_v1 in neighbors_list:
        if board[x_v1][y_v1] == 0 and depth == 0:
            valid_moves.append([start, [x_v1, y_v1]])
        if board[x_v1][y_v1] > 0 and depth == 0:
            x_v2 = x_v1 + (x_v1 - start_x)
            y_v2 = y_v1 + (y_v1 - start_y)
            if board[x_v2][y_v2] == 0:
                valid_moves.append([start, [x_v2, y_v2]])
                check_moves(board, [x_v2, y_v2], depth + 1, origin, [x_v1, y_v1], valid_moves)
        if board[x_v1][y_v1] > 0 and depth > 0 and previous != [x_v1, y_v1]:
            x_v2 = x_v1 + (x_v1 - start_x)
            y_v2 = y_v1 + (y_v1 - start_y)
            if board[x_v2][y_v2] == 0:
                valid_moves.append([origin, [x_v2, y_v2]])
                check_moves(board, [x_v2, y_v2], depth + 1, origin, [x_v1, y_v1], valid_moves)

    return valid_moves


def neighbors(node):

    [x, y] = node

    neighbors_list = []

    nb = [x, y + 2]
    if 0 <= nb[1] <= 24:
        neighbors_list.append([x, y + 2])

    nb = [x, y - 2]
    if 0 <= nb[1] <= 24:
        neighbors_list.append([x, y - 2])

    nb = [x + 1, y + 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24 :
        neighbors_list.append([x + 1, y + 1])

    nb = [x + 1, y - 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x + 1, y - 1])

    nb = [x - 1, y + 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x - 1, y + 1])

    nb = [x - 1, y - 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x - 1, y - 1])

    return neighbors_list