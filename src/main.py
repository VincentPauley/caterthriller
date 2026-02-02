import random

import pygame

from classes.column import Column
from classes.wall_management import WallManagement
from classes.player import Player
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

all_sprites = pygame.sprite.Group()

pygame.init()
display_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED, vsync=1
)
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

player_sprites = pygame.sprite.Group()

wall_manager = WallManagement(display_surface)
player = Player(player_sprites, pygame.math.Vector2(400, 500))

running = True

bg = pygame.image.load("src/graphics/background.png").convert()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    wall_manager.update(dt)
    player_sprites.update(dt)
    player_sprites.draw(display_surface)

    pygame.display.flip()

pygame.quit()
