# Core: things needed for every game
class Window:
    def __init__(self):
        self.width = 64 * 12
        self.height = 32 * 24


# Game Specific
class Lanes:
    def __init__(self):
        self.single_lane_width = 64
        self.count = 10
        self.center_x_positions = []
        self._get_lane_center_x_positions()

    def _get_lane_center_x_positions(self):
        for i in range(self.count):
            self.center_x_positions.append(
                i * self.single_lane_width
                + self.single_lane_width
                + self.single_lane_width / 2
            )


class Walls:
    def __init__(self):
        self.initial_y_pos = -64
        self.speed = 350
        # demarcation_line is the y position a wall must reach to activate the next wall
        self.demarcation_line = 450


class Game:
    def __init__(self):
        self.lanes = Lanes()
        self.walls = Walls()


class Settings:
    def __init__(self):
        self.window = Window()
        self.game = Game()


settings = Settings()
