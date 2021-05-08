class Page:
    """Class for representing a "page" in the game.

    A page can be a menu, a fight, a cutscene, or anything else that
    should have it's own standalone logic.
    """

    def __init__(self, game):
        self.game = game

    def run(self):
        raise NotImplementedError
