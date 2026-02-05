class GameController:
    def __init__(self):
        self.walls_cleared = 0

    def increment_walls_cleared(self):
        self.walls_cleared += 1


game_controller = GameController()
