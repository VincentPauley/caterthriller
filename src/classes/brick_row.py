import pygame

from classes.column import Column

column_width = 64


class BrickRow:
    speed = 220

    columns = []

    def __init__(self, pos, sprite_group):
        for i in range(10):
            x_pos = pos.x + ((i + 1) * column_width)

            self.columns.append(Column(pygame.math.Vector2(x_pos, pos.y), sprite_group))

    def update(self, dt):
        for column in self.columns:
            # update y pos according to row speed
            column.update(column.rect.y + (self.speed * dt))
