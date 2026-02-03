class LaneSettings:
    def __init__(self):
        self.lane_width = 64
        self.lane_count = 10

    def get_lane_x_positions(self):
        x_positions = []

        for i in range(self.lane_count):
            x_positions.append(i * self.lane_width + self.lane_width)  # one extra for padding

        return x_positions