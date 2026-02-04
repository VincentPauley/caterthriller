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

# only 2 walls, wall A and wall B.
# walls can handle reseting the sprites and their position
# each wall has a demarcation line that will emit a signal back here to activate the other wall
# each wall gets a group sprite all_bricks, and attaches it's own group to the sprite as well,
# empty the internal sprite group on reset and see how it works, hopefully can then just pass the
# all_bricks sprite to the group.  There will be a brief period where you're checking collisions
# that aren't possible but it should be a brief and simple sacrifice.

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

    first_wall.update(dt)

    
    all_bricks.draw(display_surface)


    player_sprites.update(dt, all_bricks)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)
    
    pygame.display.flip()

pygame.quit()
