import conf


def get_legal_captures(piece):
    potential_captures = piece.get_potential_captures()
    legal_captures = []

    for potential_capture in potential_captures:
        if is_occupied_by_enemy(piece, potential_capture):
            legal_captures.append(potential_capture)

    return legal_captures


def is_occupied_by_enemy(piece, square):
    for enemy_piece in conf.all_pieces:
        if enemy_piece.square == square and piece.color is not enemy_piece.color:
            return True
    return False
