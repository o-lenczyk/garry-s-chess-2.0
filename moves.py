import pygame
import conf


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


def release_piece():
    x, y = pygame.mouse.get_pos()
    check_for_captures(x, y)
    for piece in conf.all_pieces:
        piece.clicked = False
    conf.log.debug("released x: %s, y: %s", x, y)


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
