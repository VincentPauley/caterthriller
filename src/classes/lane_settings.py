class LaneSettings:
    def __init__(self):
        self.lane_width = 64
        self.lane_count = 10
        self.center_x_positions = self.get_lane_center_x_positions()

    def get_lane_center_x_positions(self):
        x_positions = []

        for i in range(self.lane_count):
            x_positions.append(
                i * self.lane_width + self.lane_width + self.lane_width / 2
            )

        return x_positions


# NOTE: example of singleton usage
lane_settings = LaneSettings()
