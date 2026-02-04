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
        self.get_lane_center_x_positions()

    def get_lane_center_x_positions(self):
        for i in range(self.count):
            self.center_x_positions.append(
                i * self.single_lane_width
                + self.single_lane_width
                + self.single_lane_width / 2
            )


class Game:
    def __init__(self):
        self.lanes = Lanes()


class Settings:
    def __init__(self):
        self.window = Window()
        self.game = Game()


settings = Settings()
