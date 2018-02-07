def greedy(all_legal_moves, obj_board):

    min_distance = 100
    move_index = 0
    best_move = 0

    for move in all_legal_moves:

        [x, y] = move[1]

        for obj in obj_board:

            [x_obj, y_obj] = obj

            x_distance = abs(x - x_obj)
            y_distance = abs(y - y_obj)

            total_distance = x_distance + y_distance

            if total_distance <= min_distance:
                min_distance = total_distance
                best_move = move_index

        move_index = move_index + 1

    return all_legal_moves[best_move]
