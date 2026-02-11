import pygame

from classes.game_controller import game_controller
from settings import settings

LOW_POINT = settings.window.height
KILL_POINT = settings.game.player_y_pos + 30


class SpiderHead(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.total_dist = LOW_POINT - KILL_POINT

        self.one_hit_location = LOW_POINT - (self.total_dist * 0.33)

        self.two_hit_location = LOW_POINT - (self.total_dist * 0.66)

        self.head_positions = [
            LOW_POINT,
            LOW_POINT - (self.total_dist * 0.33),
            LOW_POINT - (self.total_dist * 0.66),
            KILL_POINT,
        ]

        self.image = pygame.image.load("src/graphics/spider-head.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(
            center=(settings.window.width / 2, self.head_positions[0])
        )

    def update(self, dt):
        self.rect.centery = self.head_positions[game_controller.current_player_hits]

        if game_controller.current_player_hits >= len(self.head_positions) -1:
            print("!!! GAME OVER !!!")
            pygame.quit()