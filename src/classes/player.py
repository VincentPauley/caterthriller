import pygame

from classes.lane_settings import LaneSettings

lane_settings = LaneSettings()

# TODO LIST
#  
# [ ] - dash mechanic (big swings are too much to reach now)
# [ ] - edge needs to be handled. either insta kill or bounce player off the wall (prob later is more fun)
        # potential dash into wall causes a jump 

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load('src/graphics/player-head.png').convert_alpha()
        self.rect = self.image.get_rect(center=(pos))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.velocity = pygame.math.Vector2(0, 0)
        self.max_speed = 600
        self.acceleration = 4000  # pixels per second squared
        self.deceleration_time = 0.2  # seconds to decelerate to target spot
        self.player_spots = lane_settings.get_lane_center_x_positions()
        
        # Target position for smooth snapping
        self.target_x = None

    def calculate_target_spot(self):
        """Find the next spot in the direction of movement"""
        if abs(self.velocity.x) < 0.1:
            return None
        
        moving_right = self.velocity.x > 0
        
        if moving_right:
            # Find next spot ahead
            next_spots = [spot for spot in self.player_spots if spot > self.pos.x]
            return next_spots[0] if next_spots else None
        else:
            # Find next spot behind
            prev_spots = [spot for spot in self.player_spots if spot < self.pos.x]
            prev_spots.sort(reverse=True)
            return prev_spots[0] if prev_spots else None

    def move(self, dt):
        # Apply velocity to position
        self.pos.x += self.velocity.x * dt
        self.rect.centerx = int(self.pos.x)

    def apply_snap_deceleration(self, dt):
        """Decelerate to target position within deceleration_time"""
        if self.target_x is None:
            return
        
        distance_to_target = self.target_x - self.pos.x
        
        # If we're very close to target, snap and stop
        if abs(distance_to_target) < 1:
            self.pos.x = self.target_x
            self.velocity.x = 0
            self.target_x = None
            return
        
        # Check if we overshot the target
        if (self.velocity.x > 0 and self.pos.x >= self.target_x) or \
           (self.velocity.x < 0 and self.pos.x <= self.target_x):
            self.pos.x = self.target_x
            self.velocity.x = 0
            self.target_x = None
            return
        
        # Calculate minimum velocity needed to reach target in deceleration_time
        # Using: distance = average_velocity * time = (v_initial + 0) / 2 * time
        # Solving for v_initial: v_initial = 2 * distance / time
        min_velocity_needed = (2 * abs(distance_to_target)) / self.deceleration_time
        
        # If current velocity is too low, accelerate to minimum needed velocity
        if abs(self.velocity.x) < min_velocity_needed:
            target_direction = 1 if distance_to_target > 0 else -1
            # Set velocity to minimum needed (with proper direction)
            self.velocity.x = min_velocity_needed * target_direction
        
        # Now apply deceleration
        # Calculate deceleration rate: a = v / t
        decel_rate = abs(self.velocity.x) / self.deceleration_time
        
        # Apply deceleration in opposite direction of velocity
        if self.velocity.x > 0:
            self.velocity.x -= decel_rate * dt
            if self.velocity.x < 0:
                self.velocity.x = 0
        elif self.velocity.x < 0:
            self.velocity.x += decel_rate * dt
            if self.velocity.x > 0:
                self.velocity.x = 0

    def input(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            # Accelerate right
            self.velocity.x += self.acceleration * dt
            if self.velocity.x > self.max_speed:
                self.velocity.x = self.max_speed
            
            # Clear target when actively moving
            self.target_x = None
        elif keys[pygame.K_LEFT]:
            # Accelerate left
            self.velocity.x -= self.acceleration * dt
            if self.velocity.x < -self.max_speed:
                self.velocity.x = -self.max_speed
            
            # Clear target when actively moving
            self.target_x = None
        else:
            # Keys released - calculate target and apply snap deceleration
            if self.target_x is None and abs(self.velocity.x) > 0.1:
                self.target_x = self.calculate_target_spot()
            
            self.apply_snap_deceleration(dt)
        
    def update(self, dt, collision_groups):
        self.input(dt)
        self.move(dt)

        if len(collision_groups) > 0:
            for brick in collision_groups.sprites():
                if brick.rect.colliderect(self.rect):
                    brick.kill()