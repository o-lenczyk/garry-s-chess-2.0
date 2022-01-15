"""functions needed to move and capture pieces"""
import pygame
import conf
import numpy as np
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

    conf.log.debug("current square: %s", current_square)

    if (current_square not in piece.legal_moves) and (
        current_square not in piece.legal_captures
    ):
        return_to_original_square(piece)
        board.erase_legal_moves()
        return False

    # magnet to closest square center
    x_cords, y_cords = get_closest_square_center(x_cords, y_cords)
    piece.rect.center = (x_cords, y_cords)

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

    piece.clicked = False
    piece.has_moved = True
    piece.square = current_square
    piece.update_row_and_column()

    board.erase_legal_moves()
    return True


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
