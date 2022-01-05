import pygame

class Pawn(pygame.sprite.Sprite):
    def __init__(self,x,y,color,size):
        pygame.sprite.Sprite.__init__(self)
        if color=="B":
            self.image = pygame.image.load("images/BP.png")
        else:
            self.image = pygame.image.load("images/WP.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class King(pygame.sprite.Sprite):
    def __init__(self,x,y,color,size):
        pygame.sprite.Sprite.__init__(self)
        if color=="B":
            self.image = pygame.image.load("images/BK.png")
        else:
            self.image = pygame.image.load("images/WK.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Queen(pygame.sprite.Sprite):
    def __init__(self,x,y,color,size):
        pygame.sprite.Sprite.__init__(self)
        if color=="B":
            self.image = pygame.image.load("images/BQ.png")
        else:
            self.image = pygame.image.load("images/WQ.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Rook(pygame.sprite.Sprite):
    def __init__(self,x,y,color,size):
        pygame.sprite.Sprite.__init__(self)
        if color=="B":
            self.image = pygame.image.load("images/BR.png")
        else:
            self.image = pygame.image.load("images/WR.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Knight(pygame.sprite.Sprite):
    def __init__(self,x,y,color,size):
        pygame.sprite.Sprite.__init__(self)
        if color=="B":
            self.image = pygame.image.load("images/BN.png")
        else:
            self.image = pygame.image.load("images/WN.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Bishop(pygame.sprite.Sprite):
    def __init__(self,x,y,color,size):
        pygame.sprite.Sprite.__init__(self)
        if color=="B":
            self.image = pygame.image.load("images/BB.png")
        else:
            self.image = pygame.image.load("images/WB.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)