import pygame


class PauseMenu:
    def __init__(self):
        self.overlay_image = pygame.image.load(
            "src/graphics/black-overlay.png"
        ).convert_alpha()

        self.target_alpha = 170
        self.reset()

    def reset(self):
        self.current_alpha = 0
        self.overlay_image.set_alpha(self.current_alpha)

    def update(self, dt):
        if self.current_alpha < self.target_alpha:
            self.current_alpha += 800 * dt
            self.overlay_image.set_alpha(self.current_alpha)

    def draw(self, surface):
        surface.blit(self.overlay_image, (0, 0))

    # note: fadout would require calling game_controller from here...
