import pygame
import conf
from piece import *

starting_piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]


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
    for i in range(0, 8):
        conf.all_pieces.add(
            starting_piece_order[i](
                i * conf.SQUARE_SIZE, 0, "black", conf.SQUARE_SIZE, i
            )
        )

    for i in range(0, 8):
        conf.all_pieces.add(
            Pawn(
                i * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "black", conf.SQUARE_SIZE, i + 8
            )
        )

    for i in range(0, 8):
        conf.all_pieces.add(
            Pawn(
                i * conf.SQUARE_SIZE,
                6 * conf.SQUARE_SIZE,
                "white",
                conf.SQUARE_SIZE,
                i + 48,
            )
        )

    for i in range(0, 8):
        conf.all_pieces.add(
            starting_piece_order[i](
                i * conf.SQUARE_SIZE,
                7 * conf.SQUARE_SIZE,
                "white",
                conf.SQUARE_SIZE,
                i + 56,
            )
        )

    conf.all_pieces.update()
