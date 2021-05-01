import random

import pygame

from lib.character import Character


class MemeDog(Character):

    MOVE_BARK = "dog bark move"
    MOVE_BITE = "dog bite move"
    MOVE_SPIN = "dog spin move"
    MOVE_HEAL = "dog heal move"

    def __init__(self, game, max_hp, max_mana, *, level=1):
        super().__init__(game, "Meme Dog", max_hp, max_mana, level=level, display_stat_x=1015, display_stat_y_start=420)
        self.bite_x = 930
        self.spin_x = 930
        self.spin_time = self.game.fps
        self.spin_direction = "backwards"
        self.heal_heart_y = 230
        self.healed_already = False
        self.display_stat_y_start = 420
        self.display_stat_y = self.display_stat_y_start

        self.dog_normal = pygame.image.load(self.game.file_directory + "images/sunni_dog_normal.png").convert_alpha()
        self.dog_dead = pygame.image.load(self.game.file_directory + "images/sunni_dog_dead.png").convert_alpha()
        self.dog_backwards = pygame.image.load(self.game.file_directory + "images/sunni_dog_backwards.png").convert_alpha()
        self.dog_bark_stance = pygame.image.load(self.game.file_directory + "images/sunni_dog_bark_stance.png").convert_alpha()

    def next_move(self):
        """Chooses and uses the dog's next move."""
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

    def change_mana(self, next_move):
        """Change the dog's mana based on the given move to be used."""
        self.current_mana -= {
            "dog bark move": 10,
            "dog heal move": 10,
            "dog bite move": 15,
            "dog spin move": 25,
        }[next_move]

    def attack_sound(self):
        """Plays a sound for when the dog attacks."""
        pygame.mixer.music.load(self.game.file_directory + f"audio/sunni_dog_attack{random.randint(1, 3)}.ogg")
        pygame.mixer.music.set_volume(self.game.volume_multiplier)
        pygame.mixer.music.play(0)
