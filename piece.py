import pygame
import conf
import numpy as np


class Pawn(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BP.png")
        else:
            self.image = pygame.image.load("images/WP.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.has_moved = False
        self.square = square
        self.row, self.column = 0, 0
        self.update_row_and_column()

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


class King(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BK.png")
        else:
            self.image = pygame.image.load("images/WK.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BQ.png")
        else:
            self.image = pygame.image.load("images/WQ.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Rook(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BR.png")
        else:
            self.image = pygame.image.load("images/WR.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BN.png")
        else:
            self.image = pygame.image.load("images/WN.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Bishop(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BB.png")
        else:
            self.image = pygame.image.load("images/WB.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square
