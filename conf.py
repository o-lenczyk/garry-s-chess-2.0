import pygame
import logging
import random
import toml

all_pieces = pygame.sprite.Group()

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

# Create a surface and pass in a tuple containing its length and width
square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))

surf_center = (
    (SCREEN_WIDTH - square.get_width()) / 2,
    (SCREEN_HEIGHT - square.get_height()) / 2,
)
