import pygame

class SingleBrick(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('src/graphics/rock-column-1.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)