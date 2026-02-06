import pygame

from classes.game_controller import game_controller
from classes.place_marker import PlaceMarker
from classes.player import Player
from classes.walls.index import WallManager
from classes.water_lane import WaterLane
from classes.smashed_brick import SmashedBrick
from events import WALL_CLEARED, BRICK_SMASHED
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
player_x = settings.game.lanes.center_x_positions[4]

# return the bottom of player so that the wall pass can tell when it has passed a player
player = Player(player_sprites, pygame.math.Vector2(player_x, player_y_pos))

wall_manager = WallManager(player.rect.bottom)

all_brick_sprites = wall_manager.all_brick_sprites

running = True

bg = pygame.image.load("src/graphics/bg.png").convert()

if settings.debug_on:
    for x_pos in settings.game.lanes.center_x_positions:
        PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)

font = pygame.font.SysFont("Arial", 15)

overlay = pygame.image.load("src/graphics/black-overlay.png").convert_alpha()

overlay.set_alpha(128) # < 128 is 50%

smashes = pygame.sprite.Group()

water_sprites = pygame.sprite.Group()

for x in settings.game.lanes.x_positions:
    water_sprite = WaterLane(pygame.math.Vector2(x, 0), water_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_controller.game_paused = True
            if event.key == pygame.K_SPACE:
                game_controller.game_paused = False

        if event.type == WALL_CLEARED:
            game_controller.increment_walls_cleared()
        if event.type == BRICK_SMASHED:
            brick_pos = event.pos  # Access the position data
            # Create smashed brick animation at that position
            SmashedBrick(pygame.math.Vector2(brick_pos[0], brick_pos[1]), [smashes])

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    display_surface.blit(bg, (64, 0))

    if not game_controller.game_paused:
        wall_manager.update(dt)
        player_sprites.update(dt, all_brick_sprites)
        water_sprites.update(dt)
        smashes.update(dt)


    water_sprites.draw(display_surface)
    all_brick_sprites.draw(display_surface)
    smashes.draw(display_surface)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)
    

    if game_controller.game_paused:
        display_surface.blit(overlay, (0,0))

    # Debug Info
    if settings.debug_on:
        score_text = font.render(
            f"Walls Cleared: {game_controller.walls_cleared}", True, (255, 255, 255)
        )
        display_surface.blit(score_text, (10, settings.window.height - 30))

    pygame.display.flip()

pygame.quit()
