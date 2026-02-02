import pygame


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
        elif keys[pygame.K_LEFT]:
            # Accelerate left
            self.velocity.x -= self.acceleration * dt
            if self.velocity.x < -self.max_speed:
                self.velocity.x = -self.max_speed
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