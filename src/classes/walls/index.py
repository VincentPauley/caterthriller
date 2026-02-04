import pygame
from classes.walls.single_wall import SingleWall

class WallManager:
    def __init__(self):
        self.all_brick_sprites = pygame.sprite.Group()

        self.wall_a = SingleWall(self.all_brick_sprites, True, lambda: self.receive_wall_demarcation_hit("A"))
        self.wall_b = SingleWall(self.all_brick_sprites, False, lambda: self.receive_wall_demarcation_hit("B"))

    def receive_wall_demarcation_hit(self, id):
        if id == 'A':
            self.wall_b.active = True
        if id == 'B':
            self.wall_a.active = True
        
    def update(self, dt):
        self.wall_a.update(dt)
        self.wall_b.update(dt)




# wall_a = SingleWall(all_bricks, True, lambda: receive_wall_demarcation_hit("A"))
# wall_b = SingleWall(all_bricks, False, lambda: receive_wall_demarcation_hit("B"))

# def receive_wall_demarcation_hit(id):
#     if id == 'A':
#         wall_b.active = True
#     if id == 'B':
#         wall_a.active = True



