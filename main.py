import logging
import random
import toml
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
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

SETTINGS = toml.load("config.toml")
log.debug("loaded config file: %s", SETTINGS)

SCREEN_SIZE = SETTINGS["board"]["screen_size"]
SCREEN_WIDTH = SCREEN_SIZE
SCREEN_HEIGHT = SCREEN_SIZE
SQUARE_SIZE = SCREEN_SIZE / 8

BACKGROUND_COLOR = SETTINGS["board"]["background_color"]
SQUARE_COLOR = SETTINGS["board"]["square_color"]
RANDOM_COLORS = SETTINGS["board"]["random_colors"]

if RANDOM_COLORS == True:
    BACKGROUND_COLOR = (
        random.randint(127, 200),
        random.randint(127, 200),
        random.randint(127, 200),
    )
    SQUARE_COLOR = (
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
    )

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
    (SCREEN_WIDTH - square.get_width()) / 2,
    (SCREEN_HEIGHT - square.get_height()) / 2,
)

all_pieces = draw_pieces(SQUARE_SIZE)
all_pieces.update()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            log.debug("clicked  x: %s, y: %s", x, y)
            for piece in all_pieces:
                if piece.rect.collidepoint(x, y):
                    piece.clicked = True
                    log.debug("clicked on: %s", type(piece).__name__)
        elif event.type == MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for piece in all_pieces:
                piece.clicked = False
            log.debug("released x: %s, y: %s", x, y)
        # Did the user hit a key?
        elif event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    for piece in all_pieces:
        if piece.clicked == True:
            x, y = pygame.mouse.get_pos()
            piece.rect.center = (x, y)

    pygame.display.flip()
    screen.fill(BACKGROUND_COLOR)
    draw_board(screen, square, SQUARE_COLOR, SCREEN_SIZE)
    all_pieces.draw(screen)
    # all_pieces.update()
    clock.tick(60)
# Done! Time to quit.
pygame.quit()
