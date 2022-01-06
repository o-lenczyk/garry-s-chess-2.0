import pygame
import conf
import board
import piece
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

board.draw_pieces()

# Run until the user asks to quit
# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            conf.log.debug("clicked  x: %s, y: %s", x, y)
            for piece in conf.all_pieces:
                if piece.rect.collidepoint(x, y):
                    piece.clicked = True
                    conf.log.debug("clicked on: %s", type(piece).__name__)
        elif event.type == MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for piece in conf.all_pieces:
                piece.clicked = False
            conf.log.debug("released x: %s, y: %s", x, y)
        # Did the user hit a key?
        elif event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    for piece in conf.all_pieces:
        if piece.clicked == True:
            x, y = pygame.mouse.get_pos()
            piece.rect.center = (x, y)

    pygame.display.flip()
    conf.screen.fill(conf.BACKGROUND_COLOR)
    board.draw_board()
    conf.all_pieces.draw(conf.screen)
    # all_pieces.update()
    conf.clock.tick(60)
# Done! Time to quit.
pygame.quit()
