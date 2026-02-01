import pygame

from classes.column import Column

column_width = 64


class BrickRow:
    speed = 220

    callback_triggered = False

    def __init__(self, pos, sprite_group, next_row_callback):
        self.next_row_callback = next_row_callback
        self.columns = []

        for i in range(10):
            x_pos = pos.x + ((i + 1) * column_width)

            self.columns.append(Column(pygame.math.Vector2(x_pos, pos.y), sprite_group))

    def update(self, dt):
        # y pos is identical for all columns so just use 1st for calculation
        new_y_pos = self.columns[0].rect.y + self.speed * dt

        for column in self.columns:
            column.update(new_y_pos)

        if new_y_pos >= 600 and not self.callback_triggered:
            print(f"printing new, new_y_pos: {new_y_pos}")
            self.callback_triggered = True
            self.next_row_callback()
