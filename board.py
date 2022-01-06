import pygame
import conf
from piece import *


def draw_board():
    # Give the surface a color to separate it from the background
    conf.square.fill(conf.SQUARE_COLOR)
    rect = conf.square.get_rect()

    for y in range(0, 8):
        for x in range(0, 8):
            if y % 2 ^ x % 2:
                conf.screen.blit(
                    conf.square, [y * (conf.SQUARE_SIZE), x * (conf.SQUARE_SIZE)]
                )


def draw_pieces():

    conf.all_pieces.add(Pawn(0, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(
        Pawn(conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(2 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(3 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(4 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(5 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(6 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(7 * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE)
    )

    conf.all_pieces.add(Rook(0, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(Knight(conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(Bishop(2 * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(King(3 * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(Queen(4 * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(Bishop(5 * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(Knight(6 * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))
    conf.all_pieces.add(Rook(7 * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE))

    conf.all_pieces.add(Pawn(0, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE))
    conf.all_pieces.add(
        Pawn(conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(2 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(3 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(4 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(5 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(6 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Pawn(7 * conf.SQUARE_SIZE, 6 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )

    conf.all_pieces.add(Rook(0, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE))
    conf.all_pieces.add(
        Knight(1 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Bishop(2 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Queen(3 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        King(4 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Bishop(5 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Knight(6 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )
    conf.all_pieces.add(
        Rook(7 * conf.SQUARE_SIZE, 7 * conf.SQUARE_SIZE, "white", conf.SQUARE_SIZE)
    )

    conf.all_pieces.update()
