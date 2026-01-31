from classes.column import Column

column_width = 64


class BrickRow:
    def __init__(self, pos, sprite_group):
        for i in range(10):
            x_pos = pos.x + ((i + 1) * column_width)

            self.columns.append(Column((x_pos, pos.y), sprite_group))

    columns = []
