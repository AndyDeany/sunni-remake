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
        if self.current_mana < 10:  # Only usable move
            return self.MOVE_TELEPORT

        if self.game.player.current_hp <= 10 and self.current_mana >= self.MOVE_CLAW.mana_cost:
            return self.MOVE_CLAW

        if self.game.player.current_hp <= 20:
            return self.MOVE_GLIDE

        if self.current_mana < 50:
            if self.game.player.current_hp <= 30:
                if self.current_hp <= 180 and random.randint(1, 10) == 1:
                    return self.MOVE_HEAL
                if random.randint(1, 3) == 1:
                    return self.MOVE_TELEPORT
                return self.MOVE_GLIDE

            if self.current_hp < 25:
                if random.randint(1, 5) == 1:
                    return random.choice([self.MOVE_TELEPORT, self.MOVE_GLIDE])
                return self.MOVE_HEAL

            options = [self.MOVE_TELEPORT, self.MOVE_GLIDE]
            if self.current_hp <= 180:
                options.append(self.MOVE_HEAL)
            return random.choice(options)

        if self.current_mana <= 140:
            if self.current_hp <= 180:
                if self.game.player.current_hp <= 30:
                    r = random.random()
                    if r < 0.05:
                        return self.MOVE_HEAL
                    if r < 0.15:
                        return self.MOVE_TELEPORT
                    if r < 0.35:
                        return self.MOVE_GLIDE
                    return self.MOVE_CLAW

                if self.current_hp < 25:
                    if self.game.player.current_hp <= 40:
                        return random.choice([self.MOVE_HEAL, self.MOVE_CLAW])
                    if random.random() < 0.15:
                        return random.choice([self.MOVE_TELEPORT, self.MOVE_GLIDE, self.MOVE_CLAW])
                    return self.MOVE_HEAL
                return random.choice([self.MOVE_HEAL, self.MOVE_TELEPORT, self.MOVE_GLIDE, self.MOVE_CLAW])

            if self.game.player.current_hp <= 30:
                if random.random() < 0.4:
                    return random.choice([self.MOVE_TELEPORT, self.MOVE_GLIDE])
                return self.MOVE_CLAW
            return random.choice([self.MOVE_TELEPORT, self.MOVE_GLIDE, self.MOVE_CLAW])

        if self.current_hp <= 180:
            if self.game.player.current_hp <= 30:
                r = random.randint(1, 15)
                if r == 1:
                    return self.MOVE_HEAL
                if r < 6:
                    return self.MOVE_GLIDE
                return self.MOVE_CLAW

            if self.current_hp < 25:
                if self.game.player.current_hp <= 40:
                    return random.choice([self.MOVE_CLAW, self.MOVE_HEAL])
                if random.random() < 0.1:
                    return random.choice([self.MOVE_GLIDE, self.MOVE_CLAW])
                return self.MOVE_HEAL
            return random.choice([self.MOVE_HEAL, self.MOVE_GLIDE, self.MOVE_CLAW])

        if self.game.player.current_hp <= 30:
            if random.randint(1, 4) == 1:
                return self.MOVE_GLIDE
            return self.MOVE_CLAW
        return random.choice([self.MOVE_GLIDE, self.MOVE_CLAW])

    def _idle_display(self):
        self.idle_animation(self.x, self.y)

    def _dead_display(self):
        self.ghost_dog_dead.display()
