import random
from collections import namedtuple

from lib.opponent import Opponent
from lib.image import Image
from lib.music import Audio
from lib.move import OpponentHeal
from .moves import Bark, Bite, Spin


class MemeDog(Opponent):
    """Class representing the Meme Dog opponent."""
    def __init__(self, game, max_hp=100, max_mana=100):
        super().__init__(game, "Meme Dog", max_hp, max_mana)
        self.x = 930
        self.y = 440

        self.dog_normal = Image("sunni_dog_normal.png", (self.x, self.y))
        self.dog_dead = Image("sunni_dog_dead.png", (self.x, self.y))
        self.dog_backwards = Image("sunni_dog_backwards.png")
        self.dog_bark_stance = Image("sunni_dog_bark_stance.png", (self.x, self.y))

        self.basic_attack_sounds = [Audio(f"sunni_dog_attack{n}.ogg") for n in range(1, 4)]

        Moves = namedtuple("Moves", "heal bark bite spin")
        self.moves = Moves(OpponentHeal(1005, 230, 410), Bark(), Bite(), Spin())

    def choose_move(self):
        """Return the name of the next move that the dog decides to use."""
        if self.current_mana < 10:  # Only usable move
            return self.moves.bark

        if self.game.player.current_hp < 15:    # Try to finish the player off
            return random.choice(self.attack_options())

        if self.current_hp < self.max_hp / 4:   # Low - prefer to heal but chance of attacking
            if random.randint(1, 10) == 1:
                return random.choice(self.attack_options())
            return self.moves.heal

        options = self.attack_options()
        if self.current_hp <= 3 * (self.max_hp / 4):
            options.append(self.moves.heal)
        return random.choice(options)

    def _idle_display(self):
        self.dog_normal.display()

    def _dead_display(self):
        self.dog_dead.display()
