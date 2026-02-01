import pygame

from classes.brick_row import BrickRow
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

all_sprites = pygame.sprite.Group()


pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

# architecture can be way better here.

# have 3 constants that represent all possible brick sets
# to reset one: determine brick pattern and position to the top of screen, set speed to 0
#
# brick_rows: list: [0,1,2]

# brick_row needs to activate the next index, if there is no next index, reset to the first index.

# at one time there can only be 2 visible bricks at once so maintain them as the same.

# could get by with 3 constant defined brick sets, set starting

brick_rows = []


def next_row_callback():
    print("Next row callback triggered")
    print(len(brick_rows))

    if (len(brick_rows)) < 5:
        brick_rows.append(
            BrickRow(pygame.math.Vector2(64, -200), all_sprites, next_row_callback)
        )


brick_rows.append(
    BrickRow(pygame.math.Vector2(64, -200), all_sprites, next_row_callback)
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
