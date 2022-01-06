import pygame
import conf
from piece import *


def draw_board():
    # Give the surface a color to separate it from the background
    conf.square.fill(conf.SQUARE_COLOR)
    rect = conf.square.get_rect()

    for i in [0, 2, 4, 6]:
        conf.screen.blit(conf.square, [i * (conf.SCREEN_SIZE / 8), 0])
    for i in [1, 3, 5, 7]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), (conf.SCREEN_SIZE / 8)]
        )
    for i in [0, 2, 4, 6]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), 2 * (conf.SCREEN_SIZE / 8)]
        )
    for i in [1, 3, 5, 7]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), 3 * (conf.SCREEN_SIZE / 8)]
        )
    for i in [0, 2, 4, 6]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), 4 * (conf.SCREEN_SIZE / 8)]
        )
    for i in [1, 3, 5, 7]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), 5 * (conf.SCREEN_SIZE / 8)]
        )
    for i in [0, 2, 4, 6]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), 6 * (conf.SCREEN_SIZE / 8)]
        )
    for i in [1, 3, 5, 7]:
        conf.screen.blit(
            conf.square, [i * (conf.SCREEN_SIZE / 8), 7 * (conf.SCREEN_SIZE / 8)]
        )


def draw_pieces():

    conf.all_pieces.add(Pawn(0, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Pawn(conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(
        Pawn(2 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(3 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(4 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(5 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(6 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(7 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "B", conf.SQUARE_SIZE)
    )

    conf.all_pieces.add(Rook(0, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Knight(conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Bishop(2 * conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(King(3 * conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Queen(4 * conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Bishop(5 * conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Knight(6 * conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))
    conf.all_pieces.add(Rook(7 * conf.SQUARE_SIZE, 0, "B", conf.SQUARE_SIZE))

    conf.all_pieces.add(Pawn(0, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE))
    conf.all_pieces.add(
        Pawn(conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(2 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(3 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(4 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(5 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(6 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(7 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )

    conf.all_pieces.add(Rook(0, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE))
    conf.all_pieces.add(
        Knight(1 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Bishop(2 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Queen(3 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        King(4 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Bishop(5 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Knight(6 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Rook(7 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "W", conf.SQUARE_SIZE)
    )

    conf.all_pieces.update()
