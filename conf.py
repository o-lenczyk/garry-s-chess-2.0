"""global configuration variables"""
import logging
import random
import pygame
import numpy as np
import toml

all_pieces = pygame.sprite.Group()
move_indicators = pygame.sprite.Group()

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
FRAMERATE = SETTINGS["board"]["framerate"]

if RANDOM_COLORS is True:
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

# Create a surface and pass in a tuple containing its length and width
square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))

surf_center = (
    (SCREEN_WIDTH - square.get_width()) / 2,
    (SCREEN_HEIGHT - square.get_height()) / 2,
)

square_numbers_matrix = np.arange(64).reshape(8, 8)

square_names_list = []

# the list will represent the board, starting from 8 row:
# a8 a7 a6 ...
# a7 b7 c7 ...
# a6 b6 c6 ...
# .. .. .. ...
# [0]=a1 [8]=a7 [56]=a1 [63]=h1


def permute_square_names():
    for number in range(8, 0, -1):
        for letter in ("a", "b", "c", "d", "e", "f", "g", "h"):
            square_names_list.append(letter + str(number))


square_centers_list = []


def compute_square_centers_list():
    for x_cord in range(0, 8):
        for y_cord in range(0, 8):
            square_centers_list.append(
                (
                    y_cord * SQUARE_SIZE + SQUARE_SIZE / 2,
                    x_cord * SQUARE_SIZE + SQUARE_SIZE / 2,
                )
            )
