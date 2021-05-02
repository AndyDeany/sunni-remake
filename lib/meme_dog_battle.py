from lib.battle import Battle
from lib.meme_dog import MemeDog


class MemeDogBattle(Battle):
    def __init__(self, game):
        super().__init__(game)
        self.opponent = MemeDog(self.game, 100, 100)

    def run(self):
        super().run()

