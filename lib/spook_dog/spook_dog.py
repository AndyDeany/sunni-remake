import random

from lib.opponent import Opponent
from lib.image import Image
from lib.move import OpponentHeal
from .moves import Glide


class SpookDog(Opponent):
    """Class representing the Spook Dog opponent."""
    def __init__(self, game, max_hp=200, max_mana=150):
        super().__init__(game, "Spook Dog", max_hp, max_mana, level=1, display_stat_x=1015, display_stat_y_start=420)
        self.x = 930
        self.y = 440
        self.num_idle_frames = 20
        self.idle_fps = 20
        self.idle_frames = [Image(f"sunni_ghost_dog_normal{n}.png") for n in range(self.num_idle_frames)]

        self.GHOST_DOG_DEAD = Image("sunni_ghost_dog_dead.png", (self.x, self.y))

        self.MOVE_HEAL = OpponentHeal(1005, 230, 410)

        self.MOVE_GLIDE = Glide()

    def choose_move(self):
        """Return the move that the ghost dog decides to use."""
        return self.MOVE_GLIDE

    def _idle_display(self):
        self.idle_animation(self.x, self.y)

    def _dead_display(self):
        self.GHOST_DOG_DEAD.display()
