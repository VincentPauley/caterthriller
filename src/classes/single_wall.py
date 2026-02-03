# this guy needs to receive a single sprite group and calculate the positioning
# of the wall for next frame.  The update method of single_wall should be where
# this is received, calculation happens once and then passed down.  This is not
# itself a sprite class, rather just for data mgmt.

# a wall is made of bricks
# get the lane settings from global helper.
import pygame

from classes.lane_settings import LaneSettings
from classes.single_brick import SingleBrick

lane_settings = LaneSettings()

class SingleWall:
    def __init__(self, sprite_groups):
        self.sprite_Groups = sprite_groups
        self.lane_center_x_positions = lane_settings.get_lane_center_x_positions()
        # sprite groups are passed in from the caller.
        self.reset_bricks()

    def reset_bricks(self):
        # each iteration the wall is re-built with new empties and potentially
        # more differentiation.  this creates a clean wall from scratch.

        for entry in enumerate(self.lane_center_x_positions):
            index = entry[0] # < will be needed later to make some bricks missing
            x_pos = entry[1]

            SingleBrick(pygame.math.Vector2(x_pos,400), self.sprite_Groups)

        # the sprite group should not be created here as it needs to be known about elsewhere right?

