import random

import pygame

from settings import settings


class DirtPatch(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.pos = pygame.math.Vector2((0, 0))
        self.image = pygame.image.load(
            "src/graphics/dirt-effect-texture.png"
        ).convert_alpha()

        self.image = pygame.transform.rotate(self.image, random.randrange(0, 360))

        self.rect = self.image.get_rect()

        self.pos.x = random.randrange(0, self.get_max_x())
        self.pos.y = random.randrange(200, 700) * -1

        self.rect.center = self.pos

    def get_max_x(self):
        return settings.window.width - self.rect.width

    def update(self, dt):
        self.pos.y += settings.game.ground.speed * dt
        self.rect.y = int(self.pos.y)

        if self.pos.y > settings.window.height:
            self.kill()
