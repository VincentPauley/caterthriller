import pygame

from classes.lane_settings import LaneSettings

lane_settings = LaneSettings()

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load('src/graphics/player-head.png').convert_alpha()
        self.rect = self.image.get_rect(center=(pos))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.velocity = pygame.math.Vector2(0, 0)
        self.max_speed = 600
        self.acceleration = 4000  # pixels per second squared
        self.friction = 3000  # deceleration when no input
        self.player_spots = lane_settings.get_lane_center_x_positions()
        self.overshoot_correction = .3

        # Track Last Direction Moving
        self.last_direction_left = False
        self.last_direction_right = False
        
        # Idle detection
        self.idle_timer = 0
        self.idle_threshold = .25  # seconds
        self.idle_triggered = False

    def on_idle(self):
        # Find the closest spot to the left and right of current position
        previous_spot = None
        next_spot = None
        
        # Find previous spot (closest one less than current x)
        for spot_x in reversed(self.player_spots):
            if spot_x < self.pos.x:
                previous_spot = spot_x
                break
        
        # Find next spot (closest one greater than current x)
        for spot_x in self.player_spots:
            if spot_x > self.pos.x:
                next_spot = spot_x
                break
        
        # If we have both spots, calculate percentage and snap based on thresholds
        if previous_spot is not None and next_spot is not None:
            distance = next_spot - previous_spot
            current_offset = self.pos.x - previous_spot
            percentage = current_offset / distance
            
            if percentage >= 1 - self.overshoot_correction:
                
                self.pos.x = next_spot
            elif percentage <= self.overshoot_correction:
                self.pos.x = previous_spot
            # else: do nothing, player is in the middle 50% range
        elif next_spot is not None:
            # Only next spot exists, snap to it
            self.pos.x = next_spot
        elif previous_spot is not None:
            # Only previous spot exists, snap to it
            self.pos.x = previous_spot

    def move(self, dt):
        # Apply velocity to position
        self.pos.x += self.velocity.x * dt
        self.rect.centerx = int(self.pos.x)

    def input(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            # Accelerate right
            self.velocity.x += self.acceleration * dt
            if self.velocity.x > self.max_speed:
                self.velocity.x = self.max_speed

            # track last direction
            self.last_direction_left = False
            self.last_direction_right = True
            # Reset idle timer on input
            self.idle_timer = 0
            self.idle_triggered = False
        elif keys[pygame.K_LEFT]:
            # Accelerate left
            self.velocity.x -= self.acceleration * dt
            if self.velocity.x < -self.max_speed:
                self.velocity.x = -self.max_speed
            # track last direction
            self.last_direction_left = True
            self.last_direction_right = False
            # Reset idle timer on input
            self.idle_timer = 0
            self.idle_triggered = False
        else:
            # Apply friction when no input
            if self.velocity.x > 0:
                self.velocity.x -= self.friction * dt
                if self.velocity.x < 0:
                    self.velocity.x = 0
            elif self.velocity.x < 0:
                self.velocity.x += self.friction * dt
                if self.velocity.x > 0:
                    self.velocity.x = 0
        
    def update(self, dt):
        self.input(dt)
        self.move(dt)
        
        # Track idle time
        keys = pygame.key.get_pressed()
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            self.idle_timer += dt
            if self.idle_timer >= self.idle_threshold and not self.idle_triggered:
                self.idle_triggered = True
                self.on_idle()