import pygame

from settings import settings

LOW_POINT = settings.window.height
KILL_POINT = settings.game.player_y_pos + 30


class SpiderHead(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.total_dist = LOW_POINT - KILL_POINT

        self.one_hit_location = LOW_POINT - (self.total_dist * 0.33)

        self.two_hit_location = LOW_POINT - (self.total_dist * 0.66)

        self.image = pygame.image.load("src/graphics/fish.png").convert_alpha()
        self.rect = self.image.get_rect(center=(settings.window.width / 2, LOW_POINT))
