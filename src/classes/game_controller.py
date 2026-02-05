class GameController:
    def __init__(self):
        self.walls_cleared = 0
        self.game_paused = False

    def increment_walls_cleared(self):
        self.walls_cleared += 1

    # manage the level of difficulty increasing on the walls as player progresses
    # keep in mind because of demarcation the switch will happen after you think
    def get_brick_phase(self):
        if self.walls_cleared >= 9:
            return 2
        else:
            return 1


game_controller = GameController()
