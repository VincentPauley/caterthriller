import pygame

# image for column is 64 width x 128 height


class Column(pygame.sprite.Sprite):
    def __init__(self, topLeftPos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("src/graphics/column-v1.png").convert()
        self.top_left_pos = topLeftPos
        self.rect = self.image.get_rect(topleft=self.top_left_pos)

    def update(self, y_pos_change):
        self.top_left_pos.y = y_pos_change
        # round y pos for rendering
        self.rect.y = round(self.top_left_pos.y)
