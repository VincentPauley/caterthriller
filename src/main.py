import pygame

from classes.dirt_patch import DirtPatch
from classes.game_controller import game_controller
from classes.menu.pause import PauseMenu
from classes.place_marker import PlaceMarker
from classes.player import Player
from classes.smashed_brick import SmashedBrick
from classes.walls.index import WallManager
from events import BRICK_SMASHED, WALL_CLEARED
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

dirt_patches = pygame.sprite.Group()

# return the bottom of player so that the wall pass can tell when it has passed a player
player = Player(player_sprites, pygame.math.Vector2(player_x, player_y_pos))

wall_manager = WallManager(player.rect.bottom)

all_brick_sprites = wall_manager.all_brick_sprites

running = True

dirt_background = pygame.image.load("src/graphics/dirt-bg-2.png").convert()

if settings.debug_on:
    for x_pos in settings.game.lanes.center_x_positions:
        PlaceMarker(pygame.math.Vector2(x_pos, player_y_pos), place_markers)


font = pygame.font.SysFont("Arial", 15)

pause_menu = PauseMenu()

smashes = pygame.sprite.Group()


def spawn_dirt_patches():
    DirtPatch(dirt_patches)
    DirtPatch(dirt_patches)
    DirtPatch(dirt_patches)
    DirtPatch(dirt_patches)


spawn_dirt_patches()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_controller.game_paused = True
            if event.key == pygame.K_SPACE:
                if game_controller.game_paused:
                    pause_menu.resume()
            if event.key == pygame.K_DOWN:
                if game_controller.game_paused:
                    pause_menu.handle_input("down")
            if event.key == pygame.K_UP:
                if game_controller.game_paused:
                    pause_menu.handle_input("up")
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if game_controller.game_paused:
                    pause_menu.handle_input("enter")

        if event.type == WALL_CLEARED:
            game_controller.increment_walls_cleared()
            spawn_dirt_patches()
        if event.type == BRICK_SMASHED:
            brick_pos = event.pos
            # Create smashed brick animation at that position
            SmashedBrick(pygame.math.Vector2(brick_pos[0], brick_pos[1]), [smashes])

    dt = clock.tick(60) / 1000  # limits to 60 FPS and provides dt

    if not game_controller.game_paused:
        # run core game features
        # update
        wall_manager.update(dt)
        player_sprites.update(dt, all_brick_sprites)
        smashes.update(dt)
        dirt_patches.update(dt)
        # draw

    display_surface.blit(dirt_background, (0, 0))
    dirt_patches.draw(display_surface)
    all_brick_sprites.draw(display_surface)
    smashes.draw(display_surface)
    player_sprites.draw(display_surface)
    place_markers.draw(display_surface)

    if game_controller.game_paused:
        pause_menu.update(dt)
        pause_menu.draw(display_surface)

    # Debug Info
    if settings.debug_on:
        score_text = font.render(
            f"Walls Cleared: {game_controller.walls_cleared}", True, (255, 255, 255)
        )
        display_surface.blit(score_text, (10, settings.window.height - 30))

    pygame.display.flip()

pygame.quit()
