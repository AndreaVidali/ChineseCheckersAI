import math

def greedy(board, all_legal_moves, obj_set, player_turn):

    print("--- Obj positions:        ", obj_set)

    obj_available = []

    for pos in obj_set:
        [x, y] = pos
        if board[x][y] != player_turn:
            obj_available.append([x, y])

    print("--- Obj positions (avail):", obj_available)

    max_distance_metric = 0
    move_index = 0
    best_move = 0

    for move in all_legal_moves:

        if player_turn == 1:
            obj_x = 16
            obj_y = 12
        if player_turn == 2:
            obj_x = 12
            obj_y = 0
        if player_turn == 3:
            obj_x = 4
            obj_y = 0
        if player_turn == 4:
            obj_x = 0
            obj_y = 12
        if player_turn == 5:
            obj_x = 4
            obj_y = 24
        if player_turn == 6:
            obj_x = 12
            obj_y = 24

        #print("----- Eval move:", move)

        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]

        for obj in obj_available:

            #print("------- Obj pos:", obj)

            [obj_x, obj_y] = obj

            # trasform y coord imaging the board as a square, which it should be
            square_start_y = (start_y * 14.43) / 25
            square_end_y = (end_y * 14.43) / 25
            square_obj_y = (obj_y * 14.43) / 25

            start_diag = math.sqrt(((obj_x - start_x) ** 2) + ((square_obj_y - square_start_y) ** 2))
            end_diag = math.sqrt(((obj_x - end_x) ** 2) + ((square_obj_y - square_end_y) ** 2))

            distance_travel = start_diag - end_diag
            distance_metric = distance_travel + start_diag * 0.4

            if distance_metric > max_distance_metric:
                best_move = move_index
                max_distance_metric = distance_metric
                #print("---------- distance:", round(distance_travel, 2), "- start_diag", round(start_diag, 2),
                #      ". end diag", round(end_diag, 2))
                #print("---------- distance UPDATE: best move", all_legal_moves[best_move])

        move_index = move_index + 1

    #print("---------- best move", all_legal_moves[best_move], "distance:", max_distance_metric)

    return all_legal_moves[best_move]



