from collections import namedtuple

from lib.opponent import Opponent
from lib.image import Image
from lib.opponent.moves import OpponentHeal


class EvilCloud(Opponent):
    """Class representing the Evil Cloud opponent."""

    NAME = "Evil Cloud"

    def __init__(self, game, max_hp=180, max_mana=300):
        super().__init__(game, max_hp, max_mana)
        self.x = 930
        self.y = 400

        self.normal = Image("evil_cloud/evil_cloud_normal.png", (self.x, self.y))

        Moves = namedtuple("Moves", "heal")
        self.moves = Moves(OpponentHeal(1005, 230, 410))

    def choose_move(self):
        """Return the move that the spook cloud decides to use."""
        return self.moves.heal

    def _idle_display(self):
        self.normal.display()

    def _dead_display(self):
        pass
