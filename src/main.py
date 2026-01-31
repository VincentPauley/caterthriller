import pygame

from classes.brick_row import BrickRow
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

all_sprites = pygame.sprite.Group()


pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

brick_row = BrickRow(pygame.math.Vector2(30, 100), all_sprites)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("gray")

    all_sprites.draw(display_surface)

    pygame.display.flip()

pygame.quit()
