class Page:

    def __init__(self, game):
        self.game = game

    def run(self):
        raise NotImplementedError

    def visit(self):
        self.game.page = self
