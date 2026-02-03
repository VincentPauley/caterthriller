import pygame
# represents a spot where a player can idle within the play area

class PlaceMarker(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load('src/graphics/place-marker.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)