import pygame
import conf
import numpy as np
import rules


def pick_piece():
    x, y = pygame.mouse.get_pos()
    conf.log.debug("clicked  x: %s, y: %s", x, y)
    for piece in conf.all_pieces:
        if piece.rect.collidepoint(x, y):
            piece.clicked = True
            conf.log.debug(
                "clicked on: %s %s, picked up from %s",
                piece.color,
                type(piece).__name__,
                conf.square_names_list[piece.square],
            )
            return piece


def move_focused_piece_to_cursor():
    for piece in conf.all_pieces:
        if piece.clicked == True:
            x, y = pygame.mouse.get_pos()
            piece.rect.center = (x, y)


def closest_square(x, y):
    mouse_position = [(x, y)]
    diffs = np.abs(np.array(conf.square_centers_list) - np.array(mouse_position))
    dists = np.sum(diffs, axis=1)
    closest_point_index = np.argmin(dists)
    return closest_point_index


def get_closest_square_center(x, y):
    closest_square_index = closest_square(x, y)
    closest_square_center = conf.square_centers_list[closest_square_index]
    return closest_square_center


def release_piece(piece):
    x, y = pygame.mouse.get_pos()
    current_square = closest_square(x, y)

    legal_captures = rules.get_legal_captures(piece)
    legal_moves = rules.get_legal_moves(piece)

    conf.log.debug("current square: %s", current_square)
    conf.log.debug("potential moves: %s", legal_moves)
    conf.log.debug("legal captures: %s", legal_captures)

    if (current_square not in legal_moves) and (current_square not in legal_captures):
        return_to_original_square(piece)
        return False

    # magnet to closest square center
    x, y = get_closest_square_center(x, y)
    piece.rect.center = (x, y)

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


def return_to_original_square(piece):
    piece.clicked = False
    piece.rect.center = conf.square_centers_list[piece.square]
    conf.log.debug(
        "%s %s returned to original position: %s",
        piece.color,
        type(piece).__name__,
        conf.square_names_list[piece.square],
    )


def check_if_captures(piece_above):
    for piece_below in conf.all_pieces:
        if (
            pygame.sprite.collide_rect(piece_above, piece_below)
            and piece_below.clicked == False
        ):
            return piece_below
    return False


def capture(piece):
    conf.all_pieces.remove(piece)
