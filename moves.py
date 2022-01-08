import pygame
import conf
import numpy as np


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


def release_piece(piece):
    x, y = pygame.mouse.get_pos()
    closest_square_index = closest_square(x, y)

    conf.log.debug(
        "closest square to release is %s", conf.square_names_list[closest_square_index]
    )
    x, y = conf.square_centers_list[closest_square_index]

    piece.rect.center = (x, y)
    piece_captured = check_if_captures(piece)

    if piece_captured:
        capture(piece_captured)

    piece.clicked = False


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
    conf.log.debug("killed: %s %s", piece.color, type(piece).__name__)
