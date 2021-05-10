"""Module for base universal move related classes and functions."""
import random

from lib.pages.battle.states.battle_state import BattleState


class Move(BattleState):    # noqa pylint: disable=abstract-method
    """Class representing a character's move."""

    def __init__(self, mana_cost, base_damage=0, damage_variance=0.1, *, mana_damage=0,
                 base_healing=0, healing_variance=0.1):
        self._sound = None
        self.mana_cost = mana_cost
        self.base_damage = base_damage
        self.damage_variance = damage_variance
        self.mana_damage = mana_damage
        self.base_healing = base_healing
        self.healing_variance = healing_variance

    def play_sound(self):
        self.game.music.play_sound(self.sound)

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, value):
        self._sound = value

    @property
    def user(self):
        raise NotImplementedError

    @property
    def opponent(self):
        raise NotImplementedError

    @property
    def damage(self):
        return self.base_damage     # Can be altered by stats (int/str etc.) in the future

    @property
    def min_damage(self):
        return round(self.damage*(1-self.damage_variance))

    @property
    def max_damage(self):
        return round(self.damage*(1+self.damage_variance))

    @property
    def healing(self):
        return self.base_healing    # Can be altered by stats (int) in the future

    @property
    def min_healing(self):
        return round(self.healing*(1-self.healing_variance))

    @property
    def max_healing(self):
        return round(self.healing*(1+self.healing_variance))

    def deal_damage(self):
        """Deal the move's damage to its target's HP."""
        self.opponent.damage(random.randint(self.min_damage, self.max_damage))

    def deal_mana_damage(self):
        """Remove the move's mana damage from its target's mana."""
        self.opponent.damage_mana(self.mana_damage)

    def restore_hp(self):
        """Restore the move's healing to the user."""
        self.user.restore_hp(random.randint(self.min_healing, self.max_healing))


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
