# this manages display for how man coins a player has at a time
import pygame
from classes.game_controller import game_controller

sound_effect = pygame.mixer.Sound("src/sounds/woosh.wav")

class CoinIndicator(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.inactive_image = pygame.image.load("src/graphics/empty-spot.png").convert_alpha()
        self.active_image = pygame.image.load("src/graphics/active-spot.png").convert_alpha()
        self.active = False

        self.image = self.active_image if self.active else self.inactive_image
        self.rect = self.image.get_rect(x=pos.x, y=pos.y)
    

    def update(self, dt):
        self.image = self.active_image if self.active else self.inactive_image


class CoinPurse():
    def __init__(self):
        self.indicator_group = pygame.sprite.Group()

        self.coin_1 = CoinIndicator(pygame.math.Vector2(10,10),  self.indicator_group)
        self.coin_2 = CoinIndicator(pygame.math.Vector2(40,10),  self.indicator_group)
        self.coin_3 = CoinIndicator(pygame.math.Vector2(70,10),  self.indicator_group)
        self.last_known = 0
        self.delay_timer = None
        self.delay_duration = 1.0  # 1 second
    
    def delayed_action(self):
        # cash in coins and reward player
        sound_effect.play()
        self.coin_3.active = False
        self.coin_2.active = False
        self.coin_1.active = False
        game_controller.current_player_coins = 0

    def draw(self, display_surface):
        self.indicator_group.draw(display_surface)

    def update(self, dt):
        # Update delay timer if active
        if self.delay_timer is not None:
            self.delay_timer += dt
            if self.delay_timer >= self.delay_duration:
                self.delayed_action()
                self.delay_timer = None  # Reset timer
        
        if game_controller.current_player_coins == 3 and self.last_known != 3:
            self.coin_3.active = True
            self.coin_2.active = True
            self.coin_1.active = True
            self.last_known = 3
            self.delay_timer = 0  # Start the delay timer
        elif game_controller.current_player_coins == 2 and self.last_known != 2:
            self.coin_3.active = False
            self.coin_2.active = True
            self.coin_1.active = True
            self.last_known = 2
        elif game_controller.current_player_coins == 1 and self.last_known != 1:
            self.coin_3.active = False
            self.coin_2.active = False
            self.coin_1.active = True
            self.last_known = 1


        self.indicator_group.update(dt)

