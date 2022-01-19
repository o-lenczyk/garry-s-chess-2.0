import conf


def get_legal_captures(piece):
    potential_captures = piece.get_potential_captures()
    legal_captures = []

    for potential_capture in potential_captures:
        if is_occupied_by_enemy(piece, potential_capture):
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

    for potential_move in potential_moves:
        if not is_occupied(potential_move):
            legal_moves.append(potential_move)

    return legal_moves


def is_occupied(square):
    for piece in conf.all_pieces:
        if piece.square == square:
            return True
    return False


def in_board_range(row, column):
    return bool(row in range(0, 8)) and (column in range(0, 8))
