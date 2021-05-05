import random

from lib.move import OpponentMove
from lib.image import Image
from lib.music import Audio


class KanyeSnakeMove(OpponentMove):     # noqa pylint: disable=abstract-method
    """Class for representing Kayne Snake's moves."""


class ConfuseMove(KanyeSnakeMove):
    def __init__(self):
        super().__init__(-10)
        self.sound = Audio("sunni_snake_confuse.ogg", 0.3)

        self.is_moving = None
        self.facing_forwards = None
        self.confuse_duration = None
        self.set_initial_values()

        self.START_X = 930
        self.END_X = 450

        self.total_confuse_duration = self.game.fps

    def set_initial_values(self):
        self.is_moving = False
        self.facing_forwards = False
        self.confuse_duration = 0

    def run(self):
        if self.user.x > self.END_X:
            self.opponent.idle_display()
            image = self.user.SNAKE_MOVING if self.is_moving else self.user.SNAKE_NORMAL
            image.display(self.user.x, self.user.y)
            self.is_moving = not self.is_moving
            self.user.x -= 24
        elif self.confuse_duration < self.total_confuse_duration:
            if self.facing_forwards:
                self.user.SNAKE_NORMAL.display(self.user.x, self.user.y)
                player_image = self.opponent.character_backwards
            else:
                self.play_sound()
                self.user.SNAKE_BACKWARDS.display(0, self.user.y)
                player_image = self.opponent.character_normal
            player_image.display(self.opponent.x, self.opponent.y)
            self.facing_forwards = not self.facing_forwards
            self.confuse_duration += 1
        else:
            self.user.x = self.START_X
            self.user.idle_display()
            self.opponent.damage_mana(20)
            self.set_initial_values()
            self.opponent.next_move()


class VenomMove(KanyeSnakeMove):
    def __init__(self):
        super().__init__(20)
        self.sound = Audio("sunni_snake_venom.ogg", 0.5)
        self.beam = Image("sunni_snake_venom_beam.png")

        self.duration = None
        self._set_initial_values()
        self.total_duration = 2 * self.game.fps

    def _set_initial_values(self):
        self.duration = 0

    def run(self):
        self.user.SNAKE_VENOM_STANCE.display()
        if self.duration < self.total_duration:
            if self.duration == 0:
                self.play_sound()
            elif self.duration == self.total_duration // 2:
                self.opponent.damage(random.randint(15, 25))
            for n in range(4):
                self.beam.display(730 - 180*n, self.user.y)
            self.duration += 1
        else:
            self._set_initial_values()
            self.opponent.next_move()
        self.opponent.idle_display()    # Ensure it shows on top of the beam
