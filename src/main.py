import pygame

from classes.lane_settings import LaneSettings
from classes.wall_management import WallManagement
from classes.place_marker import PlaceMarker
from classes.player import Player
from classes.single_brick import SingleBrick
from classes.single_wall import SingleWall

from settings import WINDOW_HEIGHT, WINDOW_WIDTH


pygame.init()
display_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED, vsync=1
)
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

place_markers = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()

player_y_pos = 500

wall_manager = WallManagement(display_surface)
player = Player(player_sprites, pygame.math.Vector2(400, player_y_pos))

running = True

bg = pygame.image.load("src/graphics/background.png").convert()

lane_settings = LaneSettings()

# show player spots (for debug)
# for x_pos in lane_settings.get_lane_center_x_positions():
#     PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)

all_bricks = pygame.sprite.Group()


first_wall = SingleWall(all_bricks)

# ok need to make a more dynamic way rahter than hard-coding, also don't want to 
# clear the sprites from all bricks so might need separate group rather than this...

# all bricks can be used for draw but probably need a local sprite group to handle specific
# deletes

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    # wall manager returns sprites that player should check for collisions
    # collision_walls = wall_manager.update(dt)
    collision_walls=[]

    player_sprites.update(dt, collision_walls)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)
    
    # Update wall and remove if it goes off screen
    if first_wall and not first_wall.update(dt):
        first_wall = None  # Remove the wall instance
    
    if first_wall:
        all_bricks.draw(display_surface)

    pygame.display.flip()

pygame.quit()
