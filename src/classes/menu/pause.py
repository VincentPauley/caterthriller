import pygame

from classes.game_controller import game_controller
from settings import settings

pygame.init()

font = pygame.font.SysFont("Arial", 24)

menu_title = font.render("Paused", True, (255, 255, 255))


menu_title.get_rect(center=(settings.window.width // 2, 300))


class PauseMenu:
    def __init__(self):
        self.overlay_image = pygame.image.load(
            "src/graphics/black-overlay.png"
        ).convert_alpha()

        self.target_alpha = 170
        self.overlay_completed = False
        self.resume_requested = False
        self.reset()

    def reset(self):
        self.overlay_completed = False
        self.resume_requested = False
        self.current_alpha = 0
        self.overlay_image.set_alpha(self.current_alpha)

        # TODO: ^ reset should be private... Realistically the event loop will
        # call an action here and then this class will handle fadeout etc.

    def update(self, dt):
        if not self.overlay_completed:
            # initiate the pause
            if self.current_alpha <= self.target_alpha:
                self.current_alpha += 800 * dt
                self.overlay_image.set_alpha(self.current_alpha)
            else:
                self.overlay_completed = True
        if self.resume_requested:
            if self.current_alpha > 0:
                self.current_alpha -= 800 * dt
                self.overlay_image.set_alpha(self.current_alpha)
            else:
                self.reset()
                game_controller.game_paused = False

    def draw(self, surface):
        surface.blit(self.overlay_image, (0, 0))

        surface.blit(menu_title, (300, 300))

    def resume(self):
        self.resume_requested = True
