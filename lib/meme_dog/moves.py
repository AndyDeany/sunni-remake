"""Module containing Meme Dog's (unique) moves."""
import random

from lib.opponent.moves import OpponentMove
from lib.music import Audio


class MemeDogMove(OpponentMove):    # noqa pylint: disable=abstract-method
    """Class for representing one of Meme Dog's moves."""
    def __init__(self, mana_cost):
        super().__init__(mana_cost)
        self.sounds = [Audio(f"meme_dog/dog_attack{n}.ogg") for n in range(1, 4)]

    @property
    def sound(self):
        return random.choice(self.sounds)


class Bark(MemeDogMove):
    """Class for representing the Bark move."""
    def __init__(self):
        super().__init__(-10)
        self.duration = 0
        self.total_duration = 2*self.game.fps

    def run(self):
        self.opponent.display()
        self.user.dog_bark_stance.display()

        if self.duration < self.total_duration:
            if self.duration == 0:
                self.play_sound()
            elif self.duration == self.total_duration//3:
                self.play_sound()
            elif self.duration == self.total_duration//2:
                self.opponent.damage(random.randint(5, 20))
            self.duration += 1
        else:   # Resetting variables for next time
            self.duration = 0
            self.opponent.next_move()


class Bite(MemeDogMove):
    """Class for representing the Bite move."""
    FORWARD_STEP = 24
    BACKWARD_STEP = 42

    def __init__(self):
        super().__init__(15)

        self.advancing = True
        self.start_x = 930
        self.sound_x = 330
        self.end_x = 90

    def run(self):
        self.opponent.display()
        if self.advancing:
            if self.user.x > self.end_x:
                self.user.dog_normal.display(self.user.x, self.user.y)
                self.user.x -= self.FORWARD_STEP
                if self.user.x == self.sound_x:
                    self.play_sound()
            else:
                self.opponent.damage(random.randint(10, 20))
                self.advancing = False

        if not self.advancing:
            self.user.dog_backwards.display(self.user.x, self.user.y)
            if self.user.x < self.start_x:
                self.user.x += self.BACKWARD_STEP
            else:   # Reset variables for next time
                self.advancing = True
                self.user.x = self.start_x
                self.opponent.next_move()


class Spin(MemeDogMove):
    """Class for representing the Spin move."""
    FORWARD_STEP = 25
    BACKWARD_STEP = 30

    def __init__(self):
        super().__init__(25)
        self.advancing = True
        self.start_x = 930
        self.end_x = 180

        self.spin_duration = 0
        self.total_spin_duration = self.game.fps
        self.facing_forwards = False

    def run(self):
        self.opponent.display()
        if self.advancing:
            self.user.dog_normal.display(self.user.x, self.user.y)
            if self.user.x == self.end_x:
                self.advancing = False
                self.play_sound()
            else:
                self.user.x -= self.FORWARD_STEP

        elif self.spin_duration < self.total_spin_duration:
            if self.spin_duration == self.total_spin_duration//2:
                self.opponent.damage(random.randint(10, 30))
            image = self.user.dog_normal if self.facing_forwards else self.user.dog_backwards
            image.display(self.user.x, self.user.y)
            self.facing_forwards = not self.facing_forwards
            self.spin_duration += 1

        elif self.user.x < self.start_x:
            self.user.dog_backwards.display(self.user.x, self.user.y)
            self.user.x += self.BACKWARD_STEP

        else:   # Reset variables for next time
            self.advancing = True
            self.spin_duration = 0
            self.opponent.next_move()
