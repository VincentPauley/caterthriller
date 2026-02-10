# this should be a single class that can handle the placement and movement of all of
# the non-colliding elements in the background. dirt patch, stain, rock patch etc...
import random

import pygame

from settings import settings


class BackgroundElement(pygame.sprite.Sprite):
    def __init__(self, image_path, groups):
        super().__init__(groups)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        # randomly rotate image for variety
        self.image = pygame.transform.rotate(self.image, random.randrange(0, 360))

        min_x = 0 - (self.rect.width / 2)
        max_x = settings.window.width - (self.rect.width / 2)

        x = random.randrange(int(min_x), int(max_x))

        min_y = self.rect.height
        max_y = 500

        y = -1 * random.randrange(int(min_y), int(max_y))

        self.pos = pygame.math.Vector2(x, y)

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def update(self, dt):
        self.pos.y += settings.game.ground.speed * dt
        # TODO: could use easement in the movement to create paralax illusion
        self.rect.y = int(self.pos.y)
        if self.pos.y > settings.window.height:
            self.kill()
