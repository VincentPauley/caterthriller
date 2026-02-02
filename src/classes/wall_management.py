import pygame
import random

from settings import WINDOW_HEIGHT
from classes.column import Column

brick_rows = []
column_x_positions = []

# these positions are always constant
for i in range(10):
    column_x_positions.append(i * 64 + 64)


class SingleWallManager:
    def __init__(self, display_surface, index, active, demarcation_callback):
        self.display_surface = display_surface
        self.wall_index = index
        self.active = active
        self.demarcation_callback = demarcation_callback
        self.has_called_next = False
        self.y_pos = -200
        self.column_speed = 415
        self.column_sprite_group = pygame.sprite.Group()
        self.create_group_sprites()

    def update(self, dt):
        self.update_pos(dt)
        self.column_sprite_group.update(self.y_pos)

    def draw(self):
        self.column_sprite_group.draw(self.display_surface)

    def reset(self):
        self.active = False
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
            self.has_called_next = True
            self.demarcation_callback(self.wall_index)

        self.y_pos = self.y_pos + self.column_speed * dt

    def create_group_sprites(self):
        # one block chosen to be missing at random
        missing_block_index = random.randint(0, 9)

        for index, x_pos in enumerate(column_x_positions):
            if index != missing_block_index:
                Column(pygame.math.Vector2(x_pos, self.y_pos), self.column_sprite_group)


class WallManagement:
    def __init__(self, display_surface):
        self.walls = []
        self.display_surface = display_surface

        # NOTE: at the moment this is an array to future proof in case more walls are needed
        # if it truly only ever needs 2 this could be refactored to allow for faster and simpler
        # calculations
        for i in range(2):
            # first wall is the only active
            active = i < 1
            self.walls.append(SingleWallManager(self.display_surface, i, active, self.demarcation_callback)) 

        # current wall that has potential to hit the player (needs collisions)
        # self.active_wall_index = 0

    def demarcation_callback(self, caller_index):
        # Activate the next wall, wrapping around to 0 if at the end
        next_index = (caller_index + 1) % len(self.walls)
        self.walls[next_index].active = True

    def update(self, dt):
        # print('update')
        for wall in self.walls:
            if wall.active:
                wall.update(dt)
                wall.draw()