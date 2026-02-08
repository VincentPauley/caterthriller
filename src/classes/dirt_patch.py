import pygame


class DirtPatch(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.pos = pos
        self.image = pygame.image.load(
            "src/graphics/dirt-effect-texture.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)
