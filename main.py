import logging
import pygame
from board import *
from piece import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
    )
log = logging.getLogger(__name__)

SCREEN_SIZE = 512
SCREEN_WIDTH = SCREEN_SIZE
SCREEN_HEIGHT = SCREEN_SIZE
SQUARE_SIZE = SCREEN_SIZE/8

BACKGROUND_COLOR = (70, 140, 255)
SQUARE_COLOR = (140, 50, 60)

pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
# Variable to keep the main loop running
running = True

# Create a surface and pass in a tuple containing its length and width
square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))

surf_center = (
    (SCREEN_WIDTH-square.get_width())/2,
    (SCREEN_HEIGHT-square.get_height())/2
)

all_pieces=draw_pieces(SQUARE_SIZE)
all_pieces.update()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            log.debug("clicked x: %s, y: %s",x,y)
        # Did the user hit a key?
        elif event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
       # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    pygame.display.flip()
    screen.fill(BACKGROUND_COLOR)
    draw_board(screen, square, SQUARE_COLOR, SCREEN_SIZE)
    all_pieces.draw(screen)
    #all_pieces.update()
    clock.tick(60)
# Done! Time to quit.
pygame.quit()