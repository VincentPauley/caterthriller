import pygame

# image for column is 64 width x 128 height


class Column(pygame.sprite.Sprite):
    def __init__(self, topLeftPos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("src/graphics/column-v1.png").convert()
        self.rect = self.image.get_rect(topleft=topLeftPos)
