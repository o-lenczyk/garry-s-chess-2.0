"""main loop"""
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)
import conf
import board
import moves

board.draw_pieces()

# Run until the user asks to quit
# Variable to keep the main loop RUNNING
RUNNING = True

conf.permute_square_names()
conf.compute_square_centers_list()


# Main loop
while RUNNING:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            picked = moves.pick_piece()

        elif event.type == MOUSEBUTTONUP and picked:
            moves.release_piece(picked)
        # Did the user hit a key?
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            RUNNING = False

    moves.move_focused_piece_to_cursor()

    pygame.display.flip()
    conf.screen.fill(conf.BACKGROUND_COLOR)
    board.draw_board()
    conf.all_pieces.draw(conf.screen)
    conf.move_indicators.draw(conf.screen)

    conf.clock.tick(conf.FRAMERATE)
