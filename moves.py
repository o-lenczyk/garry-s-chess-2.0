import pygame
import conf
import numpy as np


def pick_piece():
    x, y = pygame.mouse.get_pos()
    conf.log.debug("clicked  x: %s, y: %s", x, y)
    for piece in conf.all_pieces:
        if piece.rect.collidepoint(x, y):
            piece.clicked = True
            conf.log.debug("clicked on: %s %s", piece.color, type(piece).__name__)


def move_focused_piece_to_cursor():
    for piece in conf.all_pieces:
        if piece.clicked == True:
            x, y = pygame.mouse.get_pos()
            piece.rect.center = (x, y)


def closest_square(x, y):
    mouse_position = [(x, y)]
    diffs = np.abs(np.array(conf.square_centers) - np.array(mouse_position))
    dists = np.sum(diffs, axis=1)
    closest_point_index = np.argmin(dists)
    return closest_point_index


def release_piece():
    x, y = pygame.mouse.get_pos()
    closest_square_index = closest_square(x, y)

    conf.log.debug(
        "closest square to release is %s", conf.square_names[closest_square_index]
    )
    x, y = conf.square_centers[closest_square_index]

    for piece in conf.all_pieces:
        if piece.clicked == True:
            piece.rect.center = (x, y)
            check_for_captures(x, y)
            piece.clicked = False


def check_for_captures(x, y):
    for piece_above in conf.all_pieces:
        if piece_above.clicked == True:
            for piece_below in conf.all_pieces:
                if (
                    pygame.sprite.collide_rect(piece_above, piece_below)
                    and piece_below.clicked == False
                ):
                    conf.all_pieces.remove(piece_below)
                    conf.log.debug(
                        "killed: %s %s", piece_below.color, type(piece_below).__name__
                    )
