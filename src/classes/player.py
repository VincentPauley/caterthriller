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
        
        # Target position for smooth snapping
        self.target_x = None

    def calculate_target_spot(self):
        """Determine which spot to snap to based on velocity and position"""
        if abs(self.velocity.x) < 0.1:
            return None
        
        moving_right = self.velocity.x > 0
        
        if moving_right:
            # Find next spots ahead
            next_spots = [spot for spot in self.player_spots if spot > self.pos.x]
            if not next_spots:
                return None
            
            next_spots.sort()  # Ensure sorted ascending
            immediate_next = next_spots[0]
            
            # Check if we should skip to the spot after
            distance_to_immediate = immediate_next - self.pos.x
            
            # If we have a second spot and conditions warrant skipping
            if len(next_spots) > 1:
                second_next = next_spots[1]
                
                # Skip if: too fast OR too close to immediate next
                # Using a threshold: if distance < 20px OR velocity > 400
                if distance_to_immediate < 20 or abs(self.velocity.x) > 400:
                    return second_next
            
            return immediate_next
            
        else:  # moving left
            # Find next spots behind
            prev_spots = [spot for spot in self.player_spots if spot < self.pos.x]
            if not prev_spots:
                return None
            
            prev_spots.sort(reverse=True)  # Ensure sorted descending
            immediate_prev = prev_spots[0]
            
            # Check if we should skip to the spot before
            distance_to_immediate = self.pos.x - immediate_prev
            
            # If we have a second spot and conditions warrant skipping
            if len(prev_spots) > 1:
                second_prev = prev_spots[1]
                
                # Skip if: too fast OR too close to immediate previous
                if distance_to_immediate < 20 or abs(self.velocity.x) > 400:
                    return second_prev
            
            return immediate_prev

    def move(self, dt):
        # Apply velocity to position
        self.pos.x += self.velocity.x * dt
        self.rect.centerx = int(self.pos.x)

    def apply_snap_deceleration(self, dt):
        """Apply calculated friction to smoothly decelerate to target position"""
        if self.target_x is None:
            return
        
        distance_to_target = self.target_x - self.pos.x
        
        # If we're very close to target, snap and stop
        if abs(distance_to_target) < 1:
            self.pos.x = self.target_x
            self.velocity.x = 0
            self.target_x = None
            return
        
        # Calculate required deceleration to stop at target
        # Using physics: v² = v₀² + 2ad, solving for a when v = 0
        if abs(self.velocity.x) > 0.1:
            # Deceleration needed = v² / (2 * distance)
            required_decel = (self.velocity.x * self.velocity.x) / (2 * abs(distance_to_target))
            
            # Apply friction in the opposite direction of velocity
            if self.velocity.x > 0:
                self.velocity.x -= min(required_decel, self.friction) * dt
                if self.velocity.x < 0:
                    self.velocity.x = 0
            elif self.velocity.x < 0:
                self.velocity.x += min(required_decel, self.friction) * dt
                if self.velocity.x > 0:
                    self.velocity.x = 0
        else:
            # Velocity too low, just stop
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
        
    def update(self, dt):
        self.input(dt)
        self.move(dt)