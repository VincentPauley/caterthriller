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

wall_initial_y = -64 # < half the vert of a column (pos right at the top of the screen edge)

class SingleWall:
    def __init__(self, shared_sprite_group: pygame.sprite.Group, active: bool, demarcation_callback):
        self.active = active
        # sprite groups
        self.shared_sprite_group = shared_sprite_group
        self.internal_sprite_group = pygame.sprite.Group()

        self.lane_center_x_positions = lane_settings.get_lane_center_x_positions()
        self.speed = 300
        self.center_y_pos = wall_initial_y

        self.demarcation_line = 450
        self.demarcation_emitted = False
        self.demarcation_callback = demarcation_callback

        # sprite groups are passed in from the caller.
        self.reset_bricks()

    def reset_bricks(self):
        # each iteration the wall is re-built with new empties and potentially
        # more differentiation.  this creates a clean wall from scratch.
        self.center_y_pos = wall_initial_y
        self.demarcation_emitted = False

        for entry in enumerate(self.lane_center_x_positions):
            index = entry[0] # < will be needed later to make some bricks missing
            x_pos = entry[1]

            SingleBrick(pygame.math.Vector2(x_pos, self.center_y_pos), [self.shared_sprite_group, self.internal_sprite_group])

    def update(self, dt):
        if not self.active:
            return
        
        if not self.demarcation_emitted and self.center_y_pos > self.demarcation_line:
            self.demarcation_callback()
            self.demarcation_emitted = True


        # Check if wall has moved off screen
        if self.center_y_pos > WINDOW_HEIGHT:
            # Remove all sprites from ALL groups they belong to
            for sprite in self.internal_sprite_group:
                sprite.kill()

            self.reset_bricks()

        else:
            self.center_y_pos += self.speed * dt
            self.internal_sprite_group.update(self.center_y_pos)

        # this guy should know to reset itself and doesn't need outside involvement to remove
        # itself from the group.  Should detect when it is off-screen and either remove itself
        # or reset to the top, leaning toward just removing itself. not sure if there is any benefit
        # to keeping the class around...

        # the sprite group should not be created here as it needs to be known about elsewhere right?
        # really this should be.

        # honestly just a simple timer might suffice for this and it would be fairly intuitive to 
        # change, might not need a line of demarcation at all.

