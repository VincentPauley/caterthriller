import pygame


class WaterEdge(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.frames = [
            pygame.image.load("src/graphics/water-edge-1.png").convert_alpha(),
            pygame.image.load("src/graphics/water-edge-2.png").convert_alpha(),
            pygame.image.load("src/graphics/water-edge-3.png").convert_alpha(),
        ]

        self.current_frame_index = 0

        self.image = self.frames[self.current_frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_speed = 8

    def animate(self, dt):
        self.current_frame_index += self.animation_speed * dt

        if self.current_frame_index >= len(self.frames):
            self.current_frame_index = 0

        self.image = self.frames[int(self.current_frame_index)]

    def update(self, dt):
        self.animate(dt)
