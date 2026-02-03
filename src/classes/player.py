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

        # Track Last Direction Moving
        self.last_direction_left = False
        self.last_direction_right = False
        
        # Idle detection
        self.idle_timer = 0
        self.idle_threshold = .25  # seconds
        self.idle_triggered = False

    def on_idle(self):
        if (self.last_direction_left):
            # iterate the list backwards until you find the first number less than x
            for index, spot_x in reversed(list(enumerate(self.player_spots))):
                if spot_x < self.pos.x:
                    self.pos.x = spot_x
                    break

        elif (self.last_direction_right):
            # iterate the list positively until you find the first number greater than x
            for index, spot_x in enumerate(self.player_spots):
                if spot_x > self.pos.x:
                    self.pos.x = spot_x
                    break




        else:
            print('no direction!')


        # print("Player has been idle for 2 seconds!")
        # Add your custom logic here

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