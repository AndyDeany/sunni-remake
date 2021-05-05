import random

from lib.opponent import Opponent
from lib.image import Image
from lib.music import Audio
from lib.move import OpponentHeal
from .moves import ConfuseMove, VenomMove, LaserMove


class KanyeSnake(Opponent):

    def __init__(self, game, max_hp=120, max_mana=120):
        super().__init__(game, "Kanye Snake", max_hp, max_mana, level=1, display_stat_x=1015, display_stat_y_start=420)
        self.x = 930
        self.y = 440

        self.SNAKE_NORMAL = Image("sunni_snake_normal.png", (self.x, self.y))
        self.SNAKE_DEAD = Image("sunni_snake_dead.png", (self.x, self.y))
        self.SNAKE_BACKWARDS = Image("sunni_snake_backwards.png")
        self.SNAKE_MOVING = Image("sunni_snake_moving.png")
        self.SNAKE_VENOM_STANCE = Image("sunni_snake_venom_stance.png", (self.x, self.y))
        self.SNAKE_LASER_STANCE = Image("sunni_snake_laser_stance.png", (self.x, self.y))

        self.MOVE_HEAL = OpponentHeal(1005, 230, 410)
        self.MOVE_CONFUSE = ConfuseMove()
        self.MOVE_VENOM = VenomMove()
        self.MOVE_LASER = LaserMove()

    def choose_move(self):
        """Return the move that the snake decides to use."""
        return self.MOVE_LASER

    def idle_display(self):
        self.SNAKE_NORMAL.display()

    def dead_display(self):
        self.SNAKE_DEAD.display()
