import pygame

# image for column is 64 width x 128 height


class Column(pygame.sprite.Sprite):
    def __init__(self, topLeftPos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("src/graphics/rock-column-1.png").convert_alpha()
        self.top_left_pos = topLeftPos
        self.rect = self.image.get_rect(topleft=self.top_left_pos)

    def update(self, y_pos_change):
        self.top_left_pos.y = y_pos_change
        # round y pos for rendering to avoid sub-pixel rendering issues
        self.rect.y = int(self.top_left_pos.y)
