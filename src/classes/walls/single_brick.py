import pygame


class SingleBrick(pygame.sprite.Sprite):
    def __init__(self, pos, groups, wall_index):
        super().__init__(groups)
        self.pos = pos
        self.image = pygame.image.load("src/graphics/rock-texture.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)
        self.wall_index = wall_index

    # position is determined from the entire wall, received as param
    def update(self, new_center_y):
        self.pos.y = new_center_y

        # move rect according to rounded int
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y
