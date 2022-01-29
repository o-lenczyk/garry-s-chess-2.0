"""functions needed to move and capture pieces"""
import pygame
import numpy as np
import conf
import rules
import board


def pick_piece():
    x_cords, y_cords = pygame.mouse.get_pos()
    conf.log.debug("clicked  x: %s, y: %s", x_cords, y_cords)
    for piece in conf.all_pieces:
        if piece.rect.collidepoint(x_cords, y_cords):
            piece.clicked = True

            piece.legal_moves = rules.get_legal_moves(piece)
            piece.legal_captures = rules.get_legal_captures(piece)

            conf.log.debug("legal moves: %s", piece.legal_moves)
            conf.log.debug("legal captures: %s", piece.legal_captures)

            board.draw_legal_moves(piece.legal_moves)
            board.draw_legal_captures(piece.legal_captures)

            conf.log.debug(
                "clicked on: %s %s, from %s",
                piece.color,
                piece.icon,
                conf.square_names_list[piece.square],
            )
            conf.all_pieces.move_to_front(piece)
            return piece


def move_focused_piece_to_cursor():
    for piece in conf.all_pieces:
        if piece.clicked is True:
            x_cords, y_cords = pygame.mouse.get_pos()
            piece.rect.center = (x_cords, y_cords)


def closest_square(x_cords, y_cords):
    mouse_position = [(x_cords, y_cords)]
    diffs = np.abs(np.array(conf.square_centers_list) - np.array(mouse_position))
    dists = np.sum(diffs, axis=1)
    closest_point_index = np.argmin(dists)
    return closest_point_index


def get_closest_square_center(x_cords, y_cords):
    closest_square_index = closest_square(x_cords, y_cords)
    closest_square_center = conf.square_centers_list[closest_square_index]
    return closest_square_center


def release_piece(piece):
    x_cords, y_cords = pygame.mouse.get_pos()
    current_square = closest_square(x_cords, y_cords)

    conf.log.debug("dropping on: %s", current_square)

    if (current_square not in piece.legal_moves) and (
        current_square not in piece.legal_captures
    ):
        return_to_original_square(piece)
        board.erase_legal_moves()
        return False

    set_sprite_center(piece, x_cords, y_cords)

    piece_captured = check_if_captures(piece)

    if piece_captured:
        capture(piece_captured)
        conf.log.info(
            "%s x %s",
            conf.square_names_list[piece.square],
            conf.square_names_list[current_square],
        )
    else:
        conf.log.info(
            "%s -> %s",
            conf.square_names_list[piece.square],
            conf.square_names_list[current_square],
        )

    if piece.type == "King" and (5 > abs(piece.square - current_square) > 1):
        conf.log.debug("castling")
        handle_castling(piece, current_square)

    move_piece_to_square(piece, current_square)
    board.erase_legal_moves()
    return True


def set_sprite_center(piece, x_cords, y_cords):
    # magnet sprite to closest square center
    x_cords, y_cords = get_closest_square_center(x_cords, y_cords)
    piece.rect.center = (x_cords, y_cords)


def handle_castling(king, target_king_square):
    if king.square + 2 == target_king_square:
        for piece in conf.all_pieces:
            if (
                piece.has_moved is False
                and piece.color is king.color
                and piece.type == "Rook"
                and piece.square > king.square
            ):
                rook_x_coords = conf.square_centers_list[king.square + 1][0]
                rook_y_coords = conf.square_centers_list[king.square + 1][1]
                set_sprite_center(piece, rook_x_coords, rook_y_coords)
                move_piece_to_square(piece, king.square + 1)
                conf.log.debug("short castle")
        conf.log.debug("short castle")
    elif king.square - 2 == target_king_square:
        for piece in conf.all_pieces:
            if (
                piece.has_moved is False
                and piece.color is king.color
                and piece.type == "Rook"
                and piece.square < king.square
            ):
                rook_x_coords = conf.square_centers_list[king.square - 1][0]
                rook_y_coords = conf.square_centers_list[king.square - 1][1]
                set_sprite_center(piece, rook_x_coords, rook_y_coords)
                move_piece_to_square(piece, king.square - 1)
        conf.log.debug("long castle")
    else:
        conf.log.error("castling error")
        exit()


def move_piece_to_square(piece, target_square):
    piece.clicked = False
    piece.has_moved = True
    piece.square = target_square
    piece.update_row_and_column()


def return_to_original_square(piece):
    piece.clicked = False
    piece.rect.center = conf.square_centers_list[piece.square]
    conf.log.debug(
        "%s %s returned to: %s",
        piece.color,
        piece.icon,
        conf.square_names_list[piece.square],
    )


def check_if_captures(piece_above):
    for piece_below in conf.all_pieces:
        if (
            pygame.sprite.collide_rect(piece_above, piece_below)
            and piece_below.clicked is False
        ):
            return piece_below
    return False


def capture(piece):
    conf.all_pieces.remove(piece)
