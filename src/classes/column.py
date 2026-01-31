import pygame


class Column(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("src/graphics/column-v1.png").convert()
        self.rect = self.image.get_rect()
