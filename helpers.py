import pygame
import conf


class PossibleMoves(pygame.sprite.Sprite):
    def __init__(self, square):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = conf.square_centers_list[square]


class PossibleCaptures(pygame.sprite.Sprite):
    def __init__(self, square):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = conf.square_centers_list[square]
