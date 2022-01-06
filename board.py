import pygame
from piece import *


def draw_board(screen, square, SQUARE_COLOR, SCREEN_SIZE):
    # Give the surface a color to separate it from the background
    square.fill(SQUARE_COLOR)
    rect = square.get_rect()

    for i in [0, 2, 4, 6]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 0])
    for i in [1, 3, 5, 7]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), (SCREEN_SIZE / 8)])
    for i in [0, 2, 4, 6]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 2 * (SCREEN_SIZE / 8)])
    for i in [1, 3, 5, 7]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 3 * (SCREEN_SIZE / 8)])
    for i in [0, 2, 4, 6]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 4 * (SCREEN_SIZE / 8)])
    for i in [1, 3, 5, 7]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 5 * (SCREEN_SIZE / 8)])
    for i in [0, 2, 4, 6]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 6 * (SCREEN_SIZE / 8)])
    for i in [1, 3, 5, 7]:
        screen.blit(square, [i * (SCREEN_SIZE / 8), 7 * (SCREEN_SIZE / 8)])


def draw_pieces(SQUARE_SIZE):
    all_pieces = pygame.sprite.Group()

    all_pieces.add(Pawn(0, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(2 * SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(3 * SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(4 * SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(5 * SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(6 * SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))
    all_pieces.add(Pawn(7 * SQUARE_SIZE, SQUARE_SIZE, "B", SQUARE_SIZE))

    all_pieces.add(Rook(0, 0, "B", SQUARE_SIZE))
    all_pieces.add(Knight(SQUARE_SIZE, 0, "B", SQUARE_SIZE))
    all_pieces.add(Bishop(2 * SQUARE_SIZE, 0, "B", SQUARE_SIZE))
    all_pieces.add(King(3 * SQUARE_SIZE, 0, "B", SQUARE_SIZE))
    all_pieces.add(Queen(4 * SQUARE_SIZE, 0, "B", SQUARE_SIZE))
    all_pieces.add(Bishop(5 * SQUARE_SIZE, 0, "B", SQUARE_SIZE))
    all_pieces.add(Knight(6 * SQUARE_SIZE, 0, "B", SQUARE_SIZE))
    all_pieces.add(Rook(7 * SQUARE_SIZE, 0, "B", SQUARE_SIZE))

    all_pieces.add(Pawn(0, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(2 * SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(3 * SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(4 * SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(5 * SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(6 * SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Pawn(7 * SQUARE_SIZE, 6 * SQUARE_SIZE, "W", SQUARE_SIZE))

    all_pieces.add(Rook(0, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Knight(1 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Bishop(2 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Queen(3 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(King(4 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Bishop(5 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Knight(6 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))
    all_pieces.add(Rook(7 * SQUARE_SIZE, 7 * SQUARE_SIZE, "W", SQUARE_SIZE))

    return all_pieces
