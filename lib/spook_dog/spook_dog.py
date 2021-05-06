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

        def random_weighted(moves_with_weights):
            r = random.random()
            upper_limit = 0
            weight_sum = sum(moves_with_weights.values())
            move = None
            for move, weight in moves_with_weights.items():
                upper_limit += weight/weight_sum
                if r < upper_limit:
                    return move
            return move     # Off chance that weights don't sum perfectly to 1 due to computer rounding errors.

        if self.current_mana < 10:  # Only usable move
            return self.MOVE_TELEPORT

        if self.game.player.current_hp <= 10 and self.current_mana >= self.MOVE_CLAW.mana_cost:
            return self.MOVE_CLAW
        if self.game.player.current_hp <= 20:
            return self.MOVE_GLIDE
        if self.game.player.current_hp <= 30:
            if self.current_mana < 50:
                options = {self.MOVE_TELEPORT: 3, self.MOVE_GLIDE: 6}
                if self.current_hp <= 180:
                    options[self.MOVE_HEAL] = 1
                return random_weighted(options)

            if self.current_mana <= 140:
                if self.current_hp <= 180:
                    return random_weighted({self.MOVE_HEAL: 0.05, self.MOVE_TELEPORT: 0.1,
                                            self.MOVE_GLIDE: 0.2, self.MOVE_CLAW: 0.65})
                return random_weighted({self.MOVE_TELEPORT: 0.2, self.MOVE_GLIDE: 0.2, self.MOVE_CLAW: 0.6})

            if self.current_hp <= 180:
                return random_weighted({self.MOVE_HEAL: 1/15, self.MOVE_GLIDE: 4/15, self.MOVE_CLAW: 10/15})
            return random_weighted({self.MOVE_GLIDE: 0.25, self.MOVE_CLAW: 0.75})

        if self.current_hp < 25:
            if self.current_mana < 50:
                return random_weighted({self.MOVE_TELEPORT: 0.1, self.MOVE_GLIDE: 0.1, self.MOVE_HEAL: 0.8})
            if self.current_mana <= 140:
                if self.game.player.current_hp <= 40:
                    return random.choice([self.MOVE_HEAL, self.MOVE_CLAW])
                return random_weighted({self.MOVE_HEAL: 0.85, self.MOVE_TELEPORT: 0.05,
                                        self.MOVE_GLIDE: 0.05, self.MOVE_CLAW: 0.05})
            if self.game.player.current_hp <= 40:
                return random.choice([self.MOVE_CLAW, self.MOVE_HEAL])
            return random_weighted({self.MOVE_HEAL: 0.9, self.MOVE_GLIDE: 0.05, self.MOVE_CLAW: 0.05})

        options = attack_options()
        if self.current_hp <= 0.9*self.max_hp:
            options.append(self.MOVE_HEAL)
        return random.choice(options)

    def _idle_display(self):
        self.idle_animation(self.x, self.y)

    def _dead_display(self):
        self.ghost_dog_dead.display()
