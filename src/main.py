import pygame

from classes.player import Player
from classes.walls.index import WallManager
from events import WALL_CLEARED
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
# for x_pos in settings.game.lanes.center_x_positions:
#     PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)


font = pygame.font.SysFont("Arial", 15)

walls_cleared = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == WALL_CLEARED:
            walls_cleared += 1
            print(f"Cleared Wall {walls_cleared}")

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (0, 0))

    wall_manager.update(dt)
    player_sprites.update(dt, all_brick_sprites)

    all_brick_sprites.draw(display_surface)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)

    # show score temporarily
    score_text = font.render(f"Walls Cleared: {walls_cleared}", True, (255, 255, 255))
    display_surface.blit(score_text, (10, settings.window.height - 30))

    pygame.display.flip()

pygame.quit()
