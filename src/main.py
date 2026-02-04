import pygame

from classes.lane_settings import LaneSettings
from classes.place_marker import PlaceMarker
from classes.player import Player
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

player = Player(player_sprites, pygame.math.Vector2(400, player_y_pos))

running = True

bg = pygame.image.load("src/graphics/background.png").convert()

lane_settings = LaneSettings()

# show player spots (for debug)
# for x_pos in lane_settings.get_lane_center_x_positions():
#     PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)

all_bricks = pygame.sprite.Group()

wall_a = SingleWall(all_bricks, True, lambda: receive_wall_demarcation_hit("A"))
wall_b = SingleWall(all_bricks, False, lambda: receive_wall_demarcation_hit("B"))

def receive_wall_demarcation_hit(id):
    if id == 'A':
        wall_b.active = True
    if id == 'B':
        wall_a.active = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    wall_a.update(dt)
    wall_b.update(dt)
    player_sprites.update(dt, all_bricks)

    all_bricks.draw(display_surface)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)
    
    pygame.display.flip()

pygame.quit()
