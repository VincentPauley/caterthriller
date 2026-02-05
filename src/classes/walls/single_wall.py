import random

import pygame

from classes.game_controller import game_controller
from classes.walls.single_brick import SingleBrick
from events import WALL_CLEARED
from settings import settings


class SingleWall:
    def __init__(
        self,
        shared_sprite_group: pygame.sprite.Group,
        active: bool,
        player_bottom_y_pos: float,
        demarcation_callback,
    ):
        self.active = active
        # sprite groups
        self.shared_sprite_group = shared_sprite_group
        self.internal_sprite_group = pygame.sprite.Group()
        # potentially track the number wall
        self.wall_clear_event = pygame.event.Event(WALL_CLEARED, {})

        self.lane_center_x_positions = settings.game.lanes.center_x_positions
        self.speed = settings.game.walls.speed
        self.center_y_pos = settings.game.walls.initial_y_pos

        self.demarcation_line = settings.game.walls.demarcation_line
        self.demarcation_emitted = False
        self.demarcation_callback = demarcation_callback

        self.pass_detected = False
        self.player_bottom_y_pos = player_bottom_y_pos

        # sprite groups are passed in from the caller.
        self.reset_bricks()

    def determine_empty_indexes(self):
        brick_phase = game_controller.get_brick_phase()

        if brick_phase == 1:
            """two sequential blocks empty at random"""
            empty_index = random.randrange(1, settings.game.lanes.count - 2)

            if random.randint(0, 1) == 0:
                return [empty_index, empty_index - 1]
            else:
                return [empty_index, empty_index + 1]

        if brick_phase == 2:
            """two non-sequential guaranteed blocks empty at random"""
            empty_index = random.randrange(3, settings.game.lanes.count - 3)

            if random.randint(0, 1) == 0:
                return [
                    empty_index,
                    random.randrange(0, empty_index - 1),
                ]
            else:
                return [
                    empty_index,
                    random.randrange(empty_index + 1, settings.game.lanes.count - 1),
                ]

    def reset_bricks(self):
        empty_indexes = self.determine_empty_indexes()
        # NOTE: game controller provides wall clear count:
        # print("Walls Cleared:", game_controller.walls_cleared)

        # each iteration the wall is re-built with new empties and potentially
        # more differentiation.  this creates a clean wall from scratch.
        self.center_y_pos = settings.game.walls.initial_y_pos
        self.demarcation_emitted = False
        self.pass_detected = False

        for entry in enumerate(self.lane_center_x_positions):
            index = entry[0]
            x_pos = entry[1]

            if index not in empty_indexes:
                SingleBrick(
                    pygame.math.Vector2(x_pos, self.center_y_pos),
                    [self.shared_sprite_group, self.internal_sprite_group],
                )

    def update(self, dt):
        if not self.active:
            return

        if not self.demarcation_emitted and self.center_y_pos > self.demarcation_line:
            self.demarcation_callback()
            self.demarcation_emitted = True

        # check if wall has passed a player now
        if self.center_y_pos - 64 > self.player_bottom_y_pos and not self.pass_detected:
            self.pass_detected = True
            # NOTE: should be able to tell if the wall was collided with or not
            # by the number of sprites in the group during reset vs clearing.
            pygame.event.post(self.wall_clear_event)

        # Check if wall has moved off screen
        if self.center_y_pos > settings.window.height:
            self.active = False
            # Remove all sprites from ALL groups they belong to
            for sprite in self.internal_sprite_group:
                sprite.kill()

            self.reset_bricks()

        else:
            # check here for events about player position

            self.center_y_pos += self.speed * dt
            self.internal_sprite_group.update(self.center_y_pos)
