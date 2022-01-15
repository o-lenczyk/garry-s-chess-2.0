"""this module contains Piece class and all the subclasses"""
import pygame
import numpy as np
import conf
import rules


class Piece(pygame.sprite.Sprite):
    """abstract of a piece. will contain all the variables but possible moves"""

    def __init__(self, x_cords, y_cords, color, square_size, square):
        pygame.sprite.Sprite.__init__(self)
        # class name of Pawn will have color, so this code will avoid BlackBlackPawn.png
        self.type = type(self).__name__.replace("Black", "").replace("White", "")
        filename = f"images/{color}{self.type}.png"

        self.image = pygame.image.load(filename)
        self.color = color
        # resize the image to size of square
        self.image = pygame.transform.scale(self.image, (square_size, square_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_cords, y_cords)
        self.clicked = False
        self.has_moved = False
        self.square = square
        self.row, self.column = 0, 0
        self.update_row_and_column()
        self.legal_moves = []
        self.legal_captures = []

    def update_row_and_column(self):
        where = np.where(conf.square_numbers_matrix == self.square)
        self.row = where[0][0]
        self.column = where[1][0]

    def get_potential_moves(self):
        potential_moves = []

        for direction in self.move_directions:

            temp_row = self.row
            temp_column = self.column

            row_direction = direction[0]
            column_direction = direction[1]

            move_range = self.move_range

            while (
                rules.in_board_range(
                    temp_row + row_direction, temp_column + column_direction
                )
                and move_range > 0
            ):
                potential_move = conf.fetch_square_number(
                    temp_row + row_direction, temp_column + column_direction
                )

                potential_moves.append(potential_move)

                if rules.is_occupied(potential_move):
                    break

                if isinstance(self, Pawn) and self.has_moved is False:
                    potential_move = conf.fetch_square_number(
                        temp_row + 2 * row_direction, temp_column
                    )

                potential_moves.append(potential_move)

                temp_row += row_direction
                temp_column += column_direction
                move_range -= 1
        return potential_moves


class Pawn(Piece):
    """abstract of a pawn. black moves down, white moves up"""


class BlackPawn(Pawn):
    """♟"""

    move_directions = {(1, 0)}
    capture_directions = {(1, 1), (1, -1)}
    move_range = 1
    icon = "♟"


class WhitePawn(Pawn):
    """♙"""

    move_directions = {(-1, 0)}
    capture_directions = {(-1, -1), (-1, 1)}
    move_range = 1
    icon = "♙"


class King(Piece):
    """♔ or ♚"""

    move_directions = {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }
    move_range = 1
    icon = "♔"


class Queen(Piece):
    """♕ or ♛"""

    move_directions = {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }
    move_range = 666
    icon = "♕"


class Rook(Piece):
    """♖ or ♜"""

    move_directions = {(-1, 0), (0, -1), (0, 1), (1, 0)}
    move_range = 8
    icon = "♖"


class Knight(Piece):
    """♘ or ♞"""

    move_directions = {
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    }
    move_range = 1
    icon = "♘"


class Bishop(Piece):
    """♗ or ♝"""

    move_directions = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
    move_range = 8
    icon = "♗"
