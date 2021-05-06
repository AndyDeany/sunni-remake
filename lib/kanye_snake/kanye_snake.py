import random
from collections import namedtuple

from lib.opponent import Opponent
from lib.image import Image
from lib.moves import OpponentHeal
from .moves import Confuse, Venom, Laser


class KanyeSnake(Opponent):
    """Class representing the Kanye Snake opponent."""
    def __init__(self, game, max_hp=120, max_mana=120):
        super().__init__(game, "Kanye Snake", max_hp, max_mana)
        self.x = 930
        self.y = 440

        self.snake_normal = Image("sunni_snake_normal.png", (self.x, self.y))
        self.snake_dead = Image("sunni_snake_dead.png", (self.x, self.y))
        self.snake_backwards = Image("sunni_snake_backwards.png")
        self.snake_moving = Image("sunni_snake_moving.png")
        self.snake_venom_stance = Image("sunni_snake_venom_stance.png", (self.x, self.y))
        self.snake_laser_stance = Image("sunni_snake_laser_stance.png", (self.x, self.y))

        Moves = namedtuple("Moves", "heal confuse venom laser")
        self.moves = Moves(OpponentHeal(1005, 230, 410), Confuse(), Venom(), Laser())

    def choose_move(self):
        """Return the move that the snake decides to use."""
        if self.current_mana < 10:  # Only usable move
            return self.moves.confuse

        if self.game.player.current_hp < 20:
            return random.choice(self.attack_options(favour_damage=True))

        if self.current_hp < self.max_hp / 5:
            if random.randint(1, 10) == 1:
                return random.choice(self.attack_options())
            return self.moves.heal

        options = self.attack_options()
        if self.current_hp <= 3 * (self.max_hp / 4):
            options.append(self.moves.heal)
        return random.choice(options)

    def attack_options(self, *, favour_damage=False):   # pylint: disable=arguments-differ
        """Return the options the snake can/would choose from for attacking based on his mana."""
        moves = super().attack_options()
        if len(moves) > 1 and favour_damage:
            moves.remove(self.moves.confuse)
        return moves

    def _idle_display(self):
        self.snake_normal.display()

    def _dead_display(self):
        self.snake_dead.display()
