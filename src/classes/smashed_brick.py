import pygame
from settings import settings

class SmashedBrick(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("src/graphics/smashed-column.png")
        self.rect = self.image.get_rect(center=pos)
        self.lifetime = 0.1  # seconds
        self.elapsed_time = 0
    
    def update(self, dt):
        self.rect.y += settings.game.walls.speed * dt

        self.elapsed_time += dt
        if self.elapsed_time >= self.lifetime:
            self.kill()  # Remove sprite from all groups


    