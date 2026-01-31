import pygame

from classes.column import Column
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

all_sprites = pygame.sprite.Group()


pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

column = Column(all_sprites)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("limegreen")

    all_sprites.draw(display_surface)

    pygame.display.flip()

pygame.quit()
