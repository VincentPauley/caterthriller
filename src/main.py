import random

import pygame

from classes.column import Column
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

print(WINDOW_WIDTH, WINDOW_HEIGHT)

all_sprites = pygame.sprite.Group()

column_group_1 = pygame.sprite.Group()


pygame.init()
display_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED, vsync=1
)
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

# architecture can be way better here.

# have 3 constants that represent all possible brick sets
# to reset one: determine brick pattern and position to the top of screen, set speed to 0
#
# brick_rows: list: [0,1,2]

brick_rows = []

column_x_positions = []

# these positions are always constant
for i in range(10):
    column_x_positions.append(i * 64 + 64)


class SingleWallManager:
    def __init__(self, column_sprite_group):
        self.has_called_next = False
        self.y_pos = -200
        self.column_speed = 415
        self.column_sprite_group = column_sprite_group
        self.create_group_sprites()

    def reset(self):
        self.y_pos = -200
        self.has_called_next = False
        self.column_sprite_group.empty()
        self.create_group_sprites()

    def update_pos(self, dt):
        # if colum group moves below screen then clear an reset it
        if self.y_pos > WINDOW_HEIGHT + 10:
            self.reset()

        # create line to detect when next row should be activated
        # first find out when that is

        if self.y_pos > WINDOW_HEIGHT / 2 and not self.has_called_next:
            # create next column group
            # column_group_2_positions.y_pos = -200
            # column_group_2_positions.create_group_sprites()
            self.has_called_next = True
            print("Call Next Grouping")

        self.y_pos = self.y_pos + self.column_speed * dt

    def create_group_sprites(self):
        # one block chosen to be missing at random
        missing_block_index = random.randint(0, 9)

        for index, x_pos in enumerate(column_x_positions):
            if index != missing_block_index:
                Column(pygame.math.Vector2(x_pos, self.y_pos), self.column_sprite_group)


column_group_1_positions = SingleWallManager(column_group_1)

running = True

bg = pygame.image.load("src/graphics/background.png").convert()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    column_group_1_positions.update_pos(dt)

    column_group_1.update(column_group_1_positions.y_pos)
    column_group_1.draw(display_surface)

    pygame.display.flip()

pygame.quit()
