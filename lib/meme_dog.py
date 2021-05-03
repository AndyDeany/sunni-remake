import random

from lib.character import Character
from lib.image import Image
from lib.music import Audio
from lib.move import Bark, Bite, Spin, OpponentHeal


class MemeDog(Character):

    DEAD = "dog dead"

    INFO_X = 1070

    @classmethod
    def initialise(cls):
        cls.MOVE_BARK = Bark()
        cls.MOVE_BITE = Bite()
        cls.MOVE_SPIN = Spin()
        cls.MOVE_HEAL = OpponentHeal(1005, 230, 410)

    def __init__(self, game, max_hp, max_mana, *, level=1):
        super().__init__(game, "Meme Dog", max_hp, max_mana, level=level, display_stat_x=1015, display_stat_y_start=420)
        self.x = 930
        self.y = 440

        self.dog_normal = Image("sunni_dog_normal.png", (930, 440))
        self.dog_dead = Image("sunni_dog_dead.png")
        self.dog_backwards = Image("sunni_dog_backwards.png")
        self.dog_bark_stance = Image("sunni_dog_bark_stance.png")

        self.basic_attack_sounds = [Audio(f"sunni_dog_attack{n}.ogg") for n in range(1, 4)]

    def next_move(self):
        """Chooses and uses the dog's next move."""
        if self.current_hp == 0:
            self.game.current = self.DEAD
            return
        next_move = self.choose_move()
        self.change_mana(next_move)
        self.game.current = next_move

    def choose_move(self):
        """Return the name of the next move that the dog decides to use."""
        def attack_options():
            """Return the options the dog can/would choose from for attacking based on his mana."""
            if self.current_mana < 15:
                return [self.MOVE_BARK]
            if self.current_mana < 25:
                return [self.MOVE_BARK, self.MOVE_BITE]
            if self.current_mana > 90:
                return [self.MOVE_BITE, self.MOVE_SPIN]
            return [self.MOVE_BITE, self.MOVE_BARK, self.MOVE_SPIN]

        if self.current_mana < 10:  # Only usable move
            return self.MOVE_BARK

        if self.game.player.current_hp < 15:    # Try to finish the player off
            return random.choice(attack_options())

        if self.current_hp < self.max_hp / 4:   # Low - prefer to heal but chance of attacking
            if random.randint(1, 10) == 1:
                return random.choice(attack_options())
            return self.MOVE_HEAL

        if self.current_hp > 3 * (self.max_hp / 4):  # Don't heal at high HP.
            return random.choice(attack_options())

        return random.choice([*attack_options(), self.MOVE_HEAL])

    def idle_display(self):
        self.dog_normal.display()
