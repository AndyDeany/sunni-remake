import random

import pygame

from lib.character import Character
from lib.image import Image


class MemeDog(Character):

    MOVE_BARK = "dog bark move"
    MOVE_BITE = "dog bite move"
    MOVE_SPIN = "dog spin move"
    MOVE_HEAL = "dog heal move"

    DEAD = "dog dead"

    MANA_COSTS = {
        MOVE_BARK: -10,
        MOVE_HEAL: 10,
        MOVE_BITE: 15,
        MOVE_SPIN: 25,
    }

    INFO_X = 1070

    def __init__(self, game, max_hp, max_mana, *, level=1):
        super().__init__(game, "Meme Dog", max_hp, max_mana, level=level, display_stat_x=1015, display_stat_y_start=420)
        self.bite_x = 930
        self.spin_x = 930
        self.spin_time = self.game.fps
        self.spin_direction = "backwards"
        self.heal_heart_y = 230
        self.display_stat_y_start = 420
        self.display_stat_y = self.display_stat_y_start

        self.dog_normal = Image("images/sunni_dog_normal.png")
        self.dog_dead = Image("images/sunni_dog_dead.png")
        self.dog_backwards = Image("images/sunni_dog_backwards.png")
        self.dog_bark_stance = Image("images/sunni_dog_bark_stance.png")

    def next_move(self):
        """Chooses and uses the dog's next move."""
        if self.current_hp == 0:
            self.game.current = self.DEAD
            return
        next_move = self.choose_move()
        self.change_mana(next_move)
        self.game.current = next_move

    # Defining a function to decide which move the dog is going to use
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

    def attack_sound(self):
        """Plays a sound for when the dog attacks."""
        pygame.mixer.music.load(self.game.file_directory + f"audio/sunni_dog_attack{random.randint(1, 3)}.ogg")
        pygame.mixer.music.set_volume(self.game.volume_multiplier)
        pygame.mixer.music.play(0)
