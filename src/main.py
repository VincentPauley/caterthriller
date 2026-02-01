import pygame

from classes.column import Column
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

all_sprites = pygame.sprite.Group()

column_group_1 = pygame.sprite.Group()


pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

# architecture can be way better here.

# have 3 constants that represent all possible brick sets
# to reset one: determine brick pattern and position to the top of screen, set speed to 0
#
# brick_rows: list: [0,1,2]

brick_rows = []

class ColumnGroupManager:
    def __init__(self):
        self.y_pos = -200
        self.column_speed = 115
    
    def update_pos(self, dt):
        if self.y_pos > WINDOW_HEIGHT + 10:
            self.y_pos = -200

        self.y_pos = self.y_pos + self.column_speed * dt

column_group_1_positions = ColumnGroupManager()

def init_row(x_positions):
    starting_y = column_group_1_positions.y_pos

    for x_pos in x_positions:
        Column(pygame.math.Vector2(x_pos, starting_y), column_group_1)


column_x_positions = []


for i in range(10):
    column_x_positions.append(i * 64 + 64)

init_row(column_x_positions)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.fill("gray")

    column_group_1_positions.update_pos(dt)

    column_group_1.update(column_group_1_positions.y_pos)
    column_group_1.draw(display_surface)

    pygame.display.flip()

pygame.quit()
