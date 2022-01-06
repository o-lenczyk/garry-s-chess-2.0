import pygame
import conf
import board
import piece
import moves
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

conf.permute_square_names()
conf.compute_square_centers()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            moves.pick_piece()
        elif event.type == MOUSEBUTTONUP:
            moves.release_piece()
        # Did the user hit a key?
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    moves.move_focused_piece_to_cursor()

    pygame.display.flip()
    conf.screen.fill(conf.BACKGROUND_COLOR)
    board.draw_board()
    conf.all_pieces.draw(conf.screen)
    # all_pieces.update()
    conf.clock.tick(conf.FRAMERATE)

pygame.quit()
