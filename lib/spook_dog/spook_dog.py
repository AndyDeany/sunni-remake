import random

from lib.opponent import Opponent
from lib.image import Image
from lib.move import OpponentHeal
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

        self.MOVE_HEAL = OpponentHeal(1005, 230, 410)
        self.MOVE_TELEPORT = Teleport()
        self.MOVE_GLIDE = Glide()
        self.MOVE_CLAW = Claw()

    def choose_move(self):
        """Return the move that the ghost dog decides to use."""
        def attack_options():
            """Return the options the dog can/would choose from for attacking based on his mana."""
            moves = [self.MOVE_TELEPORT, self.MOVE_GLIDE, self.MOVE_CLAW]
            moves = [move for move in moves if 0 <= self.current_mana - move.mana_cost <= self.max_mana]
            return moves

        if self.current_mana < 10:  # Only usable move
            return self.MOVE_TELEPORT

        if self.game.player.current_hp <= 10 and self.current_mana >= self.MOVE_CLAW.mana_cost:
            return self.MOVE_CLAW
        if self.game.player.current_hp <= 20:
            return self.MOVE_GLIDE
        if self.game.player.current_hp <= 30:
            if self.current_mana < 50:
                options = {self.MOVE_TELEPORT: 3, self.MOVE_GLIDE: 6}
            elif self.current_mana <= 140:
                options = {self.MOVE_TELEPORT: 1, self.MOVE_GLIDE: 2, self.MOVE_CLAW: 6}
            else:
                options = {self.MOVE_GLIDE: 2.3333333333, self.MOVE_CLAW: 6.6666666667}
            if self.current_hp <= 180:
                options[self.MOVE_HEAL] = 1
            return self.random_weighted(options)

        if self.current_hp < 25:
            if self.current_mana < 50:
                return self.random_weighted({self.MOVE_TELEPORT: 0.1, self.MOVE_GLIDE: 0.1, self.MOVE_HEAL: 0.8})
            if self.game.player.current_hp <= 40:
                return random.choice([self.MOVE_CLAW, self.MOVE_HEAL])

            if random.random() < 0.1:
                return random.choice(attack_options())
            return self.MOVE_HEAL

        options = attack_options()
        if self.current_hp <= 0.9*self.max_hp:
            options.append(self.MOVE_HEAL)
        return random.choice(options)

    def _idle_display(self):
        self.idle_animation(self.x, self.y)

    def _dead_display(self):
        self.ghost_dog_dead.display()
