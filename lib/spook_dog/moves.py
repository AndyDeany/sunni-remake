import random
import math

from lib.move import OpponentMove
from lib.image import Image
from lib.music import Audio


class SpookDogMove(OpponentMove):     # noqa pylint: disable=abstract-method
    """Class for representing Spook Dog's moves."""


class Glide(SpookDogMove):
    def __init__(self):
        super().__init__(10)
        self.sound = Audio("sunni_ghost_dog_glide.ogg")

        self.START_X = 930
        self.SOUND_X = 570
        self.END_X = -366
        self.DAMAGE_X = 210
        self.FORWARD_STEP = 24

        self.AMPLITUDE = 200
        self.OSCILLATIONS = 1.5
        self.RANGE = self.FORWARD_STEP * math.ceil(self.game.screen.get_width()/self.FORWARD_STEP)
        self.WAVELENGTH = self.RANGE/self.OSCILLATIONS

    def run(self):
        self.opponent.display()
        y = self.user.y + int(self.AMPLITUDE*math.sin((2*math.pi/self.WAVELENGTH)*(self.user.x - self.START_X)))
        self.user.idle_animation(self.user.x, y)
        if self.user.x == self.SOUND_X:
            self.play_sound()
        elif self.user.x == self.DAMAGE_X:
            self.opponent.damage(random.randint(20, 30))
        elif self.user.x <= 0:
            self.user.idle_animation(self.user.x + self.RANGE, y)

        if self.user.x == self.END_X:
            self.opponent.next_move()
            self.user.x = self.START_X
        else:
            self.user.x -= self.FORWARD_STEP
