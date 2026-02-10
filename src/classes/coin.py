import pygame
from settings import settings

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 8
        self.pos = pygame.math.Vector2(pos)
        self.frames = [
            pygame.image.load("src/graphics/coin-0.png").convert_alpha(),
            pygame.image.load("src/graphics/coin-1.png").convert_alpha(),
            pygame.image.load("src/graphics/coin-2.png").convert_alpha()
        ]

        self.image = self.frames[1]
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos.y += settings.game.ground.speed * dt
        self.rect.y = int(self.pos.y)
    
    def update(self, dt):
        self.move(dt)
        self.frame_index += self.animation_speed * dt

        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]