"""Module for base universal move related classes and functions."""
from lib.pages.battle.states import BattleState


class Move(BattleState):    # noqa
    """Class representing a character's move."""

    def __init__(self, mana_cost):
        self._sound = None
        self.mana_cost = mana_cost

    def play_sound(self):
        self.game.music.play_sound(self.sound)

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, value):
        self._sound = value


def opponent_move(player_move_subclass):
    """Convert the given player's move (a PlayerMove subclass) into a version that can be used by opponents."""
    class OpponentMove(player_move_subclass):
        @property
        def user(self):
            return self.game.opponent

        @property
        def opponent(self):
            return self.game.player

    OpponentMove.__doc__ = f"Class for representing an opponent's {player_move_subclass.__name__.lower()} move."
    return OpponentMove
