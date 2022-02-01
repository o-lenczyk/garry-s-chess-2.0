"""this module contains Piece class and all the subclasses"""
import pygame
import numpy as np
import conf
import rules


class Piece(pygame.sprite.Sprite):
    """abstract of a piece. will contain all the variables but possible moves"""
    #TODO:  x_cords, y cords can be fetched from conf.compute_square_centers_list"""
    #TODO: use square center for image positioning instead of TOPLEFT"""

    def __init__(self, x_cords, y_cords, color, square):
        pygame.sprite.Sprite.__init__(self)
        # class name of Pawn will have color, so this code will avoid BlackBlackPawn.png
        self.type = type(self).__name__.replace("Black", "").replace("White", "")
        filename = f"images/{color}{self.type}.png"

        self.image = pygame.image.load(filename)
        self.color = color
        # resize the image to size of square
        self.image = pygame.transform.scale(self.image, (conf.SQUARE_SIZE, conf.SQUARE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_cords, y_cords)
        self.clicked = False
        self.has_moved = False
        self.square = square
        self.row, self.column = 0, 0
        self.update_row_and_column()
        self.legal_moves = []
        self.legal_captures = []
        icon=""

        match f"{color}{self.type}":
            case "WhiteKing":
                self.icon="♔"
            case "WhiteQueen":
                self.icon="♕"
            case "WhiteRook":
                self.icon="♖"
            case "WhiteBishop":
                self.icon="♗"
            case "WhiteKnight":
                self.icon="♘"
            case "WhitePawn":
                self.icon="♙"
            case "BlackKing":
                self.icon="♚"
            case "BlackQueen":
                self.icon="♛"
            case "BlackRook":
                self.icon="♜"
            case "BlackBishop":
                self.icon="♝"
            case "BlackKnight":
                self.icon="♞"
            case "BlackPawn":
                self.icon="♟"

    def update_row_and_column(self):
        where = np.where(conf.square_numbers_matrix == self.square)
        self.row = where[0][0]
        self.column = where[1][0]

    def get_potential_moves(self):
        potential_moves = []

        if self.type == "King":
            self.check_for_castling()

        for direction in self.move_directions:

            temp_row = self.row
            temp_column = self.column

            row_direction = direction[0]
            column_direction = direction[1]

            potential_move_row = temp_row + row_direction
            potential_move_column = temp_column + column_direction

            move_range = self.move_range

            while (
                rules.in_board_range(potential_move_row, potential_move_column)
                and move_range > 0
            ):
                potential_move = conf.fetch_square_number(
                    potential_move_row, potential_move_column
                )

                potential_moves.append(potential_move)

                if rules.is_occupied(potential_move):
                    break

                potential_move_row += row_direction
                potential_move_column += column_direction
                move_range -= 1

        return potential_moves

    def get_potential_captures(self):
        potential_captures = self.get_potential_moves()
        return potential_captures


class Pawn(Piece):
    """abstract of a pawn. black moves down, white moves up"""

    def get_potential_moves(self):
        row_direction = list(self.move_directions)[0][0]
        potential_moves = []
        temp_row = self.row
        temp_column = self.column

        potential_move = conf.fetch_square_number(temp_row + row_direction, temp_column)

        if rules.is_occupied(potential_move):
            return potential_moves

        potential_moves.append(potential_move)

        if self.has_moved is False:
            potential_move = conf.fetch_square_number(
                temp_row + 2 * row_direction, temp_column
            )
            potential_moves.append(potential_move)
        return potential_moves

    def get_potential_captures(self):
        potential_captures = []

        for capture_direction in self.capture_directions:
            temp_row = self.row
            temp_column = self.column
            row_direction = capture_direction[0]
            column_direction = capture_direction[1]

            if rules.in_board_range(
                temp_row + row_direction, temp_column + column_direction
            ):
                potential_capture = conf.fetch_square_number(
                    temp_row + row_direction, temp_column + column_direction
                )
                potential_captures.append(potential_capture)
        return potential_captures


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

    def get_potential_moves(self):
        potential_moves = self.get_potential_captures()

        castling_squares = self.check_for_castling()

        for castling_square in castling_squares:
            potential_moves.append(castling_square)

        return potential_moves

    def get_potential_captures(self):
        potential_captures = []

        for direction in self.move_directions:

            row_direction = direction[0]
            column_direction = direction[1]

            potential_move_row = self.row + row_direction
            potential_move_column = self.column + column_direction

            if rules.in_board_range(potential_move_row, potential_move_column):
                potential_move = conf.fetch_square_number(
                    potential_move_row, potential_move_column
                )

                potential_captures.append(potential_move)

        return potential_captures

    def check_for_castling(self):
        castling_squares = []
        for piece in conf.all_pieces:
            if (
                self.has_moved is False
                and piece.has_moved is False
                and piece.color is self.color
                and piece.type == "Rook"
            ):
                if (
                    piece.square > self.square
                    and not rules.is_occupied(self.square + 1)
                    and not rules.is_castling_square_attacked(self.square+1, piece.color)
                    and not rules.is_occupied(self.square + 2)
                    and not rules.is_castling_square_attacked(self.square+2, piece.color)
                ):
                    conf.log.debug("O-O possible")
                    castling_squares.append(self.square + 2)
                if (
                    piece.square < self.square
                    and not rules.is_occupied(self.square - 1)
                    and not rules.is_castling_square_attacked(self.square-1, piece.color)
                    and not rules.is_occupied(self.square - 2)
                    and not rules.is_castling_square_attacked(self.square-2, piece.color)
                    and not rules.is_occupied(self.square - 3)
                ):
                    conf.log.debug("O-O-O possible")
                    castling_squares.append(self.square - 2)
        return castling_squares


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


class Rook(Piece):
    """♖ or ♜"""

    move_directions = {(-1, 0), (0, -1), (0, 1), (1, 0)}
    move_range = 8


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


class Bishop(Piece):
    """♗ or ♝"""

    move_directions = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
    move_range = 8
