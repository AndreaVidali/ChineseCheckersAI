from engine_2 import *


player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_sets()
player1_inv_homes, player2_inv_homes, player3_inv_homes, player4_inv_homes, player5_inv_homes, player6_inv_homes = \
    build_invalid_homes_sets(player1_set, player2_set, player3_set, player4_set, player5_set, player6_set, player1_obj,
                             player2_obj, player3_obj, player4_obj, player5_obj, player6_obj)


def minimax(board, depth, player, first_player):

    print('MINIMAX - depth:', depth, '. player', player, '. first player', first_player)

    if depth == 0:
        board_score = calculate_board_score(board, player)
        print('score:', board_score, 'for player', player, 'at depth', depth)
        return board_score, None
    
    set_pieces = assign_set(player, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set)
    obj_set = assign_obj_set(player, player1_obj, player2_obj, player3_obj, player4_obj,
                             player5_obj, player6_obj)
    inv_homes_set = assign_invalid_homes_set(player, player1_inv_homes, player2_inv_homes, player3_inv_homes,
                                             player4_inv_homes, player5_inv_homes, player6_inv_homes)

    valid_moves = find_all_legal_moves(board, set_pieces, obj_set, inv_homes_set)

    scores = []
    moves = []

    for move in valid_moves:
        new_board, new_set_pieces = do_move(board, move, set_pieces)

        next_player = player + 1
        if next_player == 7:
            next_player = 1

        score, something = minimax(new_board, depth - 1, next_player, first_player)
        scores.append(score)
        moves.append(move)

    if player == first_player:
        max_score_index = scores.index(max(scores))
        best_move = moves[max_score_index]
        return scores[max_score_index], best_move
    else:
        min_score_index = scores.index(min(scores))
        worst_opponent_move = moves[min_score_index]
        return scores[min_score_index], worst_opponent_move


def calculate_board_score(board, player_turn):

    p1_pieces = find_player_pieces(board, 1)
    p2_pieces = find_player_pieces(board, 2)
    p3_pieces = find_player_pieces(board, 3)
    p4_pieces = find_player_pieces(board, 4)
    p5_pieces = find_player_pieces(board, 5)
    p6_pieces = find_player_pieces(board, 6)

    p1_avg_distance = find_avg_distance(p1_pieces, [16, 12])
    p2_avg_distance = find_avg_distance(p2_pieces, [12, 0])
    p3_avg_distance = find_avg_distance(p3_pieces, [4, 0])
    p4_avg_distance = find_avg_distance(p4_pieces, [0, 12])
    p5_avg_distance = find_avg_distance(p5_pieces, [4, 24])
    p6_avg_distance = find_avg_distance(p6_pieces, [12, 24])

    score = calculate_score(player_turn, p1_avg_distance, p2_avg_distance, p3_avg_distance, p4_avg_distance,
                            p5_avg_distance, p6_avg_distance)

    return score


def find_player_pieces(board, player):

    p_pieces = []
    p_coords = np.where(board == player)
    print(player, p_coords[0], p_coords[1])
    for i in range(0, 10):
        x = p_coords[0][i]
        y = p_coords[1][i]
        p_pieces.append([x, y])

    return p_pieces


def find_avg_distance(p_pieces, obj):

    total_distance = 0
    [obj_x, obj_y] = obj

    for piece in p_pieces:

        [x, y] = piece

        square_y = (y * 17) / 25
        square_obj_y = (obj_y * 17) / 25

        distance_diag = math.sqrt(((obj_x - x) ** 2) + ((square_obj_y - square_y) ** 2))

        total_distance = total_distance + distance_diag

    avg_distance = total_distance / 10

    return avg_distance


def calculate_score(player_turn, p1_avg_distance, p2_avg_distance, p3_avg_distance, p4_avg_distance, p5_avg_distance,
                    p6_avg_distance):

    score = 0

    if player_turn == 1:
        pturn_avg_distance = p1_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 2:
        pturn_avg_distance = p2_avg_distance
        score = ((p1_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 3:
        pturn_avg_distance = p3_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 4:
        pturn_avg_distance = p4_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 5:
        pturn_avg_distance = p5_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 6:
        pturn_avg_distance = p6_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance)) / 5

    return score



