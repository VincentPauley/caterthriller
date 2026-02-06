import pygame

from classes.game_controller import game_controller
from settings import settings

pygame.init()


title_font = pygame.font.SysFont("Arial", 48)
font = pygame.font.SysFont("Arial", 24)

menu_title = title_font.render("Paused", True, (255, 255, 255))


menu_title.get_rect(center=(settings.window.width // 2, 300))


class Option:
    def __init__(self, text, pos):
        self.active = False
        self.color = (255, 255, 255)
        self.base_text = text
        self.text = font.render(text, True, self.color)
        self.rect = self.text.get_rect(center=pos)

    def update(self):
        # modify options basaed on active state
        if self.active:
            self.color = (255, 255, 255)
            self.text = font.render(self.base_text + " *", True, self.color)
        else:
            self.color = (150, 150, 150)
            self.text = font.render(self.base_text, True, self.color)


class PauseMenu:
    def __init__(self):
        self.overlay_image = pygame.image.load(
            "src/graphics/black-overlay.png"
        ).convert_alpha()

        self.target_alpha = 170
        self.overlay_completed = False
        self.resume_requested = False

        self.menu_title_rect = menu_title.get_rect(
            center=(settings.window.width / 2, 250)
        )

        self.option_resume = Option("Resume", (settings.window.width / 2, 325))
        self.option_quit = Option("Quit Game", (settings.window.width / 2, 400))

        self.option_resume.active = True

        self.options = [self.option_resume, self.option_quit]
        self.active_option_index = 0

        self.reset()

    def reset(self):
        self.overlay_completed = False
        self.resume_requested = False
        self.current_alpha = 0
        self.overlay_image.set_alpha(self.current_alpha)

        # TODO: ^ reset should be private... Realistically the event loop will
        # call an action here and then this class will handle fadeout etc.

    def handle_input(self, event):
        # NOTE: this is inefficient and should be refactored for any number
        # of potential menu inputs.
        if event == "down":
            if self.active_option_index == 0:
                self.active_option_index = 1
                self.option_resume.active = False
                self.option_quit.active = True
            elif self.active_option_index == 1:
                self.active_option_index = 0
                self.option_resume.active = True
                self.option_quit.active = False
        if event == "up":
            if self.active_option_index == 0:
                self.active_option_index = 1
                self.option_resume.active = False
                self.option_quit.active = True
            elif self.active_option_index == 1:
                self.active_option_index = 0
                self.option_resume.active = True
                self.option_quit.active = False

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

        # update menu options
        self.option_resume.update()
        self.option_quit.update()

    def draw(self, surface):
        surface.blit(self.overlay_image, (0, 0))

        surface.blit(menu_title, self.menu_title_rect)

        surface.blit(self.option_resume.text, self.option_resume.rect)
        surface.blit(self.option_quit.text, self.option_quit.rect)

    def resume(self):
        self.resume_requested = True
