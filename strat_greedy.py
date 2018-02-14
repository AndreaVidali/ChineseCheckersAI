import math


def greedy(board, all_legal_moves, obj_set, player_turn):

    obj_available = []

    for pos in obj_set:
        [x, y] = pos
        if board[x][y] != player_turn:
            obj_available.append([x, y])

    max_distance_metric = 0
    move_index = 0
    best_move = 0

    for move in all_legal_moves:

        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]

        for obj in obj_available:

            [obj_x, obj_y] = obj

            # trasform y coord thinking about the board as a square, which it should be
            square_start_y = (start_y * 14.43) / 25
            square_end_y = (end_y * 14.43) / 25
            square_obj_y = (obj_y * 14.43) / 25

            start_diag = math.sqrt(((obj_x - start_x) ** 2) + ((square_obj_y - square_start_y) ** 2))
            end_diag = math.sqrt(((obj_x - end_x) ** 2) + ((square_obj_y - square_end_y) ** 2))

            distance_travel = start_diag - end_diag
            distance_metric = distance_travel + start_diag * 0.5

            if distance_metric > max_distance_metric:
                best_move = move_index
                max_distance_metric = distance_metric

        move_index = move_index + 1

    return all_legal_moves[best_move]



