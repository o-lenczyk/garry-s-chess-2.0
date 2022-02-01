import conf


def get_legal_captures(piece, checking_first_time):
    potential_captures = piece.get_potential_captures()
    legal_captures = []

    potential_captures[:] = [
        potential_capture
        for potential_capture in potential_captures
        if not is_in_check_after_move(piece, potential_capture, checking_first_time)
    ]

    for potential_capture in potential_captures:
        if is_occupied_by_enemy(
            piece,
            potential_capture,
        ):
            legal_captures.append(potential_capture)

    return legal_captures


def is_occupied_by_enemy(focused_piece, square):
    for potential_enemy in conf.all_pieces:
        if (
            potential_enemy.square == square
            and focused_piece.color is not potential_enemy.color
        ):
            return True
    return False


def get_legal_moves(piece):
    potential_moves = piece.get_potential_moves()
    legal_moves = []

    potential_moves[:] = [
        potential_move
        for potential_move in potential_moves
        if not is_in_check_after_move(piece, potential_move, True)
    ]

    for potential_move in potential_moves:
        if not is_occupied(potential_move):
            legal_moves.append(potential_move)

    return legal_moves


def is_in_check_after_move(piece, next_move, checking_first_time):
    previous_square = piece.square
    piece.square = next_move

    if is_under_check(piece.color, checking_first_time):
        piece.square = previous_square
        return True

    piece.square = previous_square
    return False


def is_under_check(color, checking_first_time):
    if checking_first_time:
        king_square = 99
        for king in conf.all_pieces:
            if king.type == "King" and king.color == color:
                king_square = king.square

        for enemy_piece in conf.all_pieces:
            if enemy_piece.color != color and get_legal_captures(
                enemy_piece, False
            ).__contains__(king_square):
                return True
    return False


def is_occupied(square):
    for piece in conf.all_pieces:
        if piece.square == square:
            return True
    return False


def in_board_range(row, column):
    return bool(row in range(0, 8)) and (column in range(0, 8))


def is_castling_square_attacked(square, my_color):
    for enemy in conf.all_pieces:
        if (enemy.color != my_color) and enemy.type != "King":
            for enemy_move in get_legal_moves(enemy):
                if enemy_move == square:
                    return True
    return False
