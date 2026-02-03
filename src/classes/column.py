import random

import pygame

# image for column is 64 width x 128 height


class Column(pygame.sprite.Sprite):
    def __init__(self, topLeftPos, groups):
        super().__init__(groups)
        self.set_image()
        self.top_left_pos = topLeftPos
        self.rect = self.image.get_rect(topleft=self.top_left_pos)

    def set_image(self):
        image_number = random.randint(1, 2)

        self.image = pygame.image.load(
            f"src/graphics/rock-column-{image_number}.png"
        ).convert_alpha()

    def update(self, y_pos_change):
        self.top_left_pos.y = y_pos_change
        # round y pos for rendering to avoid sub-pixel rendering issues
        self.rect.y = int(self.top_left_pos.y)
