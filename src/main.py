import pygame

from classes.lane_settings import LaneSettings
from classes.place_marker import PlaceMarker
from classes.player import Player
from classes.walls.index import WallManager

from settings import WINDOW_HEIGHT, WINDOW_WIDTH


pygame.init()
display_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED, vsync=1
)
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()

wall_manager = WallManager()

all_brick_sprites = wall_manager.all_brick_sprites

place_markers = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()

player_y_pos = 500

player = Player(player_sprites, pygame.math.Vector2(400, player_y_pos))

running = True

bg = pygame.image.load("src/graphics/background.png").convert()

lane_settings = LaneSettings()

# show player spots (for debug)
# for x_pos in lane_settings.get_lane_center_x_positions():
#     PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    wall_manager.update(dt)
    player_sprites.update(dt, all_brick_sprites)

    all_brick_sprites.draw(display_surface)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)
    
    pygame.display.flip()

pygame.quit()
