import pygame

from classes.place_marker import PlaceMarker
from classes.player import Player
from classes.walls.index import WallManager
from settings import settings

pygame.init()
display_surface = pygame.display.set_mode(
    (settings.window.width, settings.window.height), pygame.SCALED, vsync=1
)
pygame.display.set_caption("Caterthriller")
clock = pygame.time.Clock()


place_markers = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()

player_y_pos = 500

# return the bottom of player so that the wall pass can tell when it has passed a player
player = Player(player_sprites, pygame.math.Vector2(400, player_y_pos))

wall_manager = WallManager(player.rect.bottom)

all_brick_sprites = wall_manager.all_brick_sprites

running = True

bg = pygame.image.load("src/graphics/background.png").convert()


# show player spots (for debug)
for x_pos in settings.game.lanes.center_x_positions:
    PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    wall_manager.update(dt)  # update needs to know what player's current position is in
    # order to know if it was passed or not.
    player_sprites.update(dt, all_brick_sprites)

    # ^ update of player can return the bottom position of the player
    # or better yet... player stays constant and the background moves
    # to indicate closer to edge.  no need for update every frame and
    # player stays in the same y pos making things way easier.

    all_brick_sprites.draw(display_surface)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)

    pygame.display.flip()

pygame.quit()
