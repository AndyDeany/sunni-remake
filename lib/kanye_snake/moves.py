"""Module containing Kanye Snake's (unique) moves."""
import random

from lib.opponent.moves import OpponentMove
from lib.image import Image
from lib.music import Audio


class KanyeSnakeMove(OpponentMove):     # noqa pylint: disable=abstract-method
    """Class for representing Kayne Snake's moves."""


class Confuse(KanyeSnakeMove):
    """Class for representing the Confuse move."""

    START_X = 930
    END_X = 450

    def __init__(self):
        super().__init__(-10)
        self.sound = Audio("kanye_snake/snake_confuse.ogg", 0.3)

        self.is_moving = None
        self.facing_forwards = None
        self.confuse_duration = None
        self.set_initial_values()

        self.total_confuse_duration = self.game.fps

    def set_initial_values(self):
        self.is_moving = False
        self.facing_forwards = False
        self.confuse_duration = 0

    def run(self):
        if self.user.x > self.END_X:
            self.opponent.display()
            image = self.user.snake_moving if self.is_moving else self.user.snake_normal
            image.display(self.user.x, self.user.y)
            self.is_moving = not self.is_moving
            self.user.x -= 24
        elif self.confuse_duration < self.total_confuse_duration:
            if self.facing_forwards:
                self.user.snake_normal.display(self.user.x, self.user.y)
                player_image = self.opponent.character_backwards
            else:
                self.play_sound()
                self.user.snake_backwards.display(0, self.user.y)
                player_image = self.opponent.character_normal
            player_image.display(self.opponent.x, self.opponent.y)
            self.facing_forwards = not self.facing_forwards
            self.confuse_duration += 1
        else:
            self.opponent.display()
            self.user.x = self.START_X
            self.user.display()
            self.opponent.damage_mana(20)
            self.set_initial_values()
            self.opponent.next_move()


class BeamMove(KanyeSnakeMove):
    """Base class for Kanye's beam move (since he has two)."""
    def __init__(self, mana_cost, min_damage, max_damage):
        super().__init__(mana_cost)
        self.beam = None
        self.min_damage = min_damage
        self.max_damage = max_damage

        self.duration = None
        self._set_initial_values()
        self.total_duration = 2 * self.game.fps

    @property
    def beam_stance(self):
        raise NotImplementedError

    def _set_initial_values(self):
        self.duration = 0

    def run(self):
        self.beam_stance.display()
        if self.duration < self.total_duration:
            if self.duration == 0:
                self.play_sound()
            elif self.duration == self.total_duration // 2:
                self.opponent.damage(random.randint(self.min_damage, self.max_damage))
            for n in range(4):
                self.beam.display(730 - 180 * n, self.user.y)
            self.duration += 1
        else:
            self._set_initial_values()
            self.opponent.next_move()
        self.opponent.display()  # Ensure it shows on top of the beam


class Venom(BeamMove):
    """Class for representing the Venom move."""
    def __init__(self):
        super().__init__(20, 15, 25)
        self.sound = Audio("kanye_snake/snake_venom.ogg", 0.5)
        self.beam = Image("kanye_snake/snake_venom_beam.png")

    @property
    def beam_stance(self):
        return self.user.snake_venom_stance


class Laser(BeamMove):
    """Class for representing the Laser move."""
    def __init__(self):
        super().__init__(40, 10, 40)
        self.sound = Audio("kanye_snake/snake_laser.ogg", 0.5)
        self.beam = Image("kanye_snake/snake_laser_beam.png")

    @property
    def beam_stance(self):
        return self.user.snake_laser_stance
