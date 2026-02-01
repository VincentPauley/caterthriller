import pygame

from classes.brick_row import BrickRow
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

all_sprites = pygame.sprite.Group()


pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

brick_rows = []


def next_row_callback():
    print("Next row callback triggered")
    print(len(brick_rows))

    if (len(brick_rows)) < 5:
        brick_rows.append(
            BrickRow(pygame.math.Vector2(30, 100), all_sprites, next_row_callback)
        )


brick_rows.append(
    BrickRow(pygame.math.Vector2(30, 100), all_sprites, next_row_callback)
)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    for row in brick_rows:
        row.update(dt)

    display_surface.fill("gray")

    all_sprites.draw(display_surface)

    pygame.display.flip()

pygame.quit()
