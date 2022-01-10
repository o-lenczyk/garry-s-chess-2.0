import pygame
import conf
import numpy as np


class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, color, square_size, square):
        pygame.sprite.Sprite.__init__(self)
        # class name of Pawn will have color, so this code will avoid BlackBlackPawn.png
        self.type = type(self).__name__.replace("Black", "").replace("White", "")
        filename = f"images/{color}{self.type}.png"

        self.image = pygame.image.load(filename)
        self.color = color
        # resize the image to size of square
        self.image = pygame.transform.scale(self.image, (square_size, square_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.has_moved = False
        self.square = square
        self.row, self.column = 0, 0
        self.update_row_and_column()

    def in_board_range(self, row, column):
        if (row in range(0, 8)) and (column in range(0, 8)):
            return True
        else:
            return False

    def fetch_square_number(self, row, column):
        square_number = conf.square_numbers_matrix[row][column]
        return square_number

    def update_row_and_column(self):
        where = np.where(conf.square_numbers_matrix == self.square)
        self.row = where[0][0]
        self.column = where[1][0]


class BlackPawn(Piece):
    def get_potential_moves(self):

        list_of_potential_moves = []

        row = self.row + 1  # move one square forward
        column = self.column

        if self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_moves.append(move_to_append)

        row = self.row + 2  # move two squares forward
        column = self.column  # TODO: check if row+1 is empty (implement rook first)

        if self.has_moved == False and self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_moves.append(move_to_append)

        return list_of_potential_moves

    def get_potential_captures(self):
        list_of_potential_captures = []

        row = self.row + 1  # capture left (for black)
        column = self.column - 1

        if self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_captures.append(move_to_append)

        row = self.row + 1  # capture right (for black)
        column = self.column + 1

        if self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_captures.append(move_to_append)

        return list_of_potential_captures


class WhitePawn(Piece):
    def get_potential_moves(self):

        list_of_potential_moves = []

        row = self.row - 1  # move one square forward
        column = self.column

        if self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_moves.append(move_to_append)

        row = self.row - 2  # move two squares forward
        column = self.column  # TODO: check if row+1 is empty (implement rook first)

        if self.has_moved == False and self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_moves.append(move_to_append)

        return list_of_potential_moves

    def get_potential_captures(self):
        list_of_potential_captures = []

        row = self.row - 1  # capture left (for black)
        column = self.column - 1

        if self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_captures.append(move_to_append)

        row = self.row - 1  # capture right (for black)
        column = self.column + 1

        if self.in_board_range(row, column):
            move_to_append = self.fetch_square_number(row, column)
            list_of_potential_captures.append(move_to_append)

        return list_of_potential_captures


class King(Piece):
    pass


class Queen(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass
