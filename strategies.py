import math
from decimal import Decimal

# def greedy(board, all_legal_moves, obj_board, set_pieces, player_turn):
#
#     min_distance = 100
#     move_index = 0
#     best_move = 0
#
#     # avoid calculate distance from a not-free spot
#     for x, y in set_pieces:
#         if [x, y] in obj_board:
#             obj_board.remove([x, y])
#
#     for x, y in obj_board:
#         if board[x][y] == player_turn:
#             obj_board.remove([x, y])
#
#     for move in all_legal_moves:
#
#         [x, y] = move[1]
#
#         for obj in obj_board:
#
#             [x_obj, y_obj] = obj
#
#             x_distance = abs(x - x_obj)
#             y_distance = abs(y - y_obj)
#
#             total_distance = x_distance + y_distance
#
#             if total_distance <= min_distance:
#                 min_distance = total_distance
#                 best_move = move_index
#
#         move_index = move_index + 1
#
#     return all_legal_moves[best_move]


def greedy(board, all_legal_moves, obj_set, player_turn):

    print("--- Legal moves:          ", all_legal_moves)
    print("--- Obj positions:        ", obj_set)

    obj_available = []

    for pos in obj_set:
        [x, y] = pos
        if board[x][y] != player_turn:
            obj_available.append([x, y])

    print("--- Obj positions (avail):", obj_available)

    max_distance_travel = 0
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

        print("----- Eval move:", move)

        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]

        if board[obj_x, obj_y] != player_turn:

            start_diag = math.sqrt(((obj_x - start_x) ** 2) + ((obj_y - start_y) ** 2))
            end_diag = math.sqrt(((obj_x - end_x) ** 2) + ((obj_y - end_y) ** 2))

            distance_travel = start_diag - end_diag

            print("---------- distance:", round(distance_travel, 2), "- start_diag", round(start_diag, 2), ". end diag",
                  round(end_diag, 2))

            if distance_travel > max_distance_travel:
                best_move = move_index
                max_distance_travel = distance_travel
                print("---------- distance UPDATE: best move", all_legal_moves[best_move])

        else:

            for obj in obj_available:

                print("------- Obj pos:", obj)

                [obj_x, obj_y] = obj

                start_diag = math.sqrt(((obj_x - start_x) ** 2) + ((obj_y - start_y) ** 2))
                end_diag = math.sqrt(((obj_x - end_x) ** 2) + ((obj_y - end_y) ** 2))

                distance_travel = start_diag - end_diag

                print("---------- distance:", round(distance_travel, 2), "- start_diag", round(start_diag, 2), ". end diag", round(end_diag, 2))

                if distance_travel > max_distance_travel:
                    best_move = move_index
                    max_distance_travel = distance_travel
                    print("---------- distance UPDATE: best move", all_legal_moves[best_move])

        move_index = move_index + 1

    return all_legal_moves[best_move]






