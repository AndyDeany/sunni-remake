import random
from collections import namedtuple

from lib.opponent import Opponent
from lib.image import Image
from lib.moves import OpponentHeal
from .moves import Teleport, Glide, Claw


class SpookDog(Opponent):
    """Class representing the Spook Dog opponent."""
    def __init__(self, game, max_hp=200, max_mana=150):
        super().__init__(game, "Spook Dog", max_hp, max_mana)
        self.x = 930
        self.y = 440
        self.num_idle_frames = 20
        self.idle_fps = 20
        self.idle_frames = [Image(f"sunni_ghost_dog_normal{n}.png") for n in range(self.num_idle_frames)]

        self.ghost_dog_dead = Image("sunni_ghost_dog_dead.png", (self.x, self.y))

        Moves = namedtuple("Moves", "heal teleport glide claw")
        self.moves = Moves(OpponentHeal(1005, 230, 410), Teleport(), Glide(), Claw())

    def choose_move(self):  # pylint: disable=too-many-branches,too-many-return-statements
        """Return the move that the ghost dog decides to use."""
        if self.current_mana < 10:  # Only usable move
            return self.moves.teleport

        if self.game.player.current_hp <= 10 and self.current_mana >= self.moves.claw.mana_cost:
            return self.moves.claw
        if self.game.player.current_hp <= 20:
            return self.moves.glide
        if self.game.player.current_hp <= 30:
            if self.current_mana < 50:
                options = {self.moves.teleport: 3, self.moves.glide: 6}
            elif self.current_mana <= 140:
                options = {self.moves.teleport: 1, self.moves.glide: 2, self.moves.claw: 6}
            else:
                options = {self.moves.glide: 2.3333333333, self.moves.claw: 6.6666666667}
            if self.current_hp <= 180:
                options[self.moves.heal] = 1
            return self.random_weighted(options)

        if self.current_hp < 25:
            if self.current_mana < 50:
                return self.random_weighted({self.moves.teleport: 0.1, self.moves.glide: 0.1, self.moves.heal: 0.8})
            if self.game.player.current_hp <= 40:
                return random.choice([self.moves.claw, self.moves.heal])

            if random.random() < 0.1:
                return random.choice(self.attack_options())
            return self.moves.heal

        options = self.attack_options()
        if self.current_hp <= 0.9*self.max_hp:
            options.append(self.moves.heal)
        return random.choice(options)

    def _idle_display(self):
        self.idle_animation(self.x, self.y)

    def _dead_display(self):
        self.ghost_dog_dead.display()
