# this guy needs to receive a single sprite group and calculate the positioning
# of the wall for next frame.  The update method of single_wall should be where
# this is received, calculation happens once and then passed down.  This is not
# itself a sprite class, rather just for data mgmt.


# a wall is made of bricks
# get the lane settings from global helper.
import pygame

from classes.lane_settings import LaneSettings
from classes.single_brick import SingleBrick
from settings import WINDOW_HEIGHT

lane_settings = LaneSettings()

class SingleWall:
    def __init__(self, sprite_groups):
        self.sprite_groups = sprite_groups
        self.lane_center_x_positions = lane_settings.get_lane_center_x_positions()
        self.speed = 300
        self.center_y_pos = 0

        # sprite groups are passed in from the caller.
        self.reset_bricks()
        

    def reset_bricks(self):
        # each iteration the wall is re-built with new empties and potentially
        # more differentiation.  this creates a clean wall from scratch.

        for entry in enumerate(self.lane_center_x_positions):
            index = entry[0] # < will be needed later to make some bricks missing
            x_pos = entry[1]

            SingleBrick(pygame.math.Vector2(x_pos, self.center_y_pos), self.sprite_groups)

    def update(self, dt):
        # Check if wall has moved off screen
        if self.center_y_pos > WINDOW_HEIGHT:
            # Remove all sprites from the group
            self.sprite_groups.empty()
            return False  # Signal that wall should be removed
        
        self.center_y_pos += self.speed * dt
        self.sprite_groups.update(self.center_y_pos)
        return True  # Wall is still active

        # this guy should know to reset itself and doesn't need outside involvement to remove
        # itself from the group.  Should detect when it is off-screen and either remove itself
        # or reset to the top, leaning toward just removing itself. not sure if there is any benefit
        # to keeping the class around...

        # the sprite group should not be created here as it needs to be known about elsewhere right?
        # really this should be.

        # honestly just a simple timer might suffice for this and it would be fairly intuitive to 
        # change, might not need a line of demarcation at all.

