import pygame
import random

class WaterLane(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.frames = [
            pygame.image.load("src/graphics/water-frame-1.png"),
            pygame.image.load("src/graphics/water-frame-2.png"),
            pygame.image.load("src/graphics/water-frame-3.png")
        ]
        
        self.current_frame_index = random.randint(0,2)
        self.animation_speed = random.randint(6,15)

        self.image = self.frames[self.current_frame_index]
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(x=pos.x, y = pos.y)

    def animate(self, dt):
        self.current_frame_index += self.animation_speed * dt

        if self.current_frame_index >= len(self.frames):
            self.current_frame_index = 0

        self.image = self.frames[int(self.current_frame_index)]
        self.image.set_alpha(128)

    def update(self, dt):
        self.animate(dt)