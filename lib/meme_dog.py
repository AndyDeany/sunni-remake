import random

import pygame

from lib.character import Character


class MemeDog(Character):
    def __init__(self, game, max_hp, max_mana, *, level=1):
        super().__init__(game, "Meme Dog", max_hp, max_mana, level=level)
        self.bite_x = 930
        self.spin_x = 930
        self.spin_time = self.game.fps
        self.spin_direction = "backwards"
        self.heal_heart_y = 230

        self.dog_normal = pygame.image.load(self.game.file_directory + "images\sunni_dog_normal.png").convert_alpha()
        self.dog_dead = pygame.image.load(self.game.file_directory + "images\sunni_dog_dead.png").convert_alpha()
        self.dog_backwards = pygame.image.load(self.game.file_directory + "images\sunni_dog_backwards.png").convert_alpha()
        self.dog_bark_stance = pygame.image.load(self.game.file_directory + "images\sunni_dog_bark_stance.png").convert_alpha()

    # Defining a function to decide which move the dog is going to use
    def choose_move(self):
        if self.game.player.current_hp < 15:
            if self.current_mana < 15:
                return "dog bark move"

            elif self.current_mana < 25:
                r = random.randint(1, 2)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog bite move"

            elif self.current_mana > 90:
                r = random.randint(1, 2)
                if r == 1:
                    return "dog bite move"
                elif r == 2:
                    return "dog spin move"

            else:
                r = random.randint(1, 3)
                if r == 1:
                    return "dog bite move"
                elif r == 2:
                    return "dog spin move"
                elif r == 3:
                    return "dog bark move"

        elif self.current_hp < self.max_hp / 4:
            if self.current_mana < 10:
                return "dog bark move"

            elif self.current_mana > 90:
                r = random.randint(1, 20)
                if r == 1:
                    return "dog bite move"
                elif r == 2:
                    return "dog spin move"
                else:
                    return "dog heal move"

            elif self.current_mana < 15:
                r = random.randint(1, 10)
                if r == 1:
                    return "dog bark move"
                else:
                    return "dog heal move"

            elif self.current_mana < 25:
                r = random.randint(1, 20)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog bite move"
                else:
                    return "dog heal move"

            else:
                r = random.randint(1, 30)
                if r == 1:
                    return "dog bite move"
                elif r == 2:
                    return "dog spin move"
                elif r == 3:
                    return "dog bark move"
                else:
                    return "dog heal move"

        elif self.current_hp > 3 * (self.max_hp / 4):
            if self.current_mana < 10:
                return "dog bark move"

            elif self.current_mana < 25:
                r = random.randint(1, 2)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog bite move"

            elif self.current_mana > 90:
                r = random.randint(1, 2)
                if r == 1:
                    return "dog bite move"
                elif r == 2:
                    return "dog spin move"

            else:
                r = random.randint(1, 3)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog bite move"
                elif r == 3:
                    return "dog spin move"

        else:
            if self.current_mana < 10:
                return "dog bark move"

            elif self.current_mana < 15:
                r = random.randint(1, 2)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog heal move"

            elif self.current_mana < 25:
                r = random.randint(1, 3)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog heal move"
                elif r == 3:
                    return "dog bite move"

            elif self.current_mana > 90:
                r = random.randint(1, 3)
                if r == 1:
                    return "dog heal move"
                elif r == 2:
                    return "dog bite move"
                elif r == 3:
                    return "dog spin move"

            else:
                r = random.randint(1, 4)
                if r == 1:
                    return "dog bark move"
                elif r == 2:
                    return "dog heal move"
                elif r == 3:
                    return "dog bite move"
                elif r == 4:
                    return "dog spin move"

    # Defining a function to change the dog's mana
    def change_mana(self, next_move):
        if next_move == "dog bark move":
            return self.current_mana + 10
        elif next_move == "dog heal move":
            return self.current_mana - 10
        elif next_move == "dog bite move":
            return self.current_mana - 15
        elif next_move == "dog spin move":
            return self.current_mana - 25

    # Defining a function to play a sound when the dog attacks
    def attack_sound(self):
        r = random.randint(1, 3)
        if r == 1:
            pygame.mixer.music.load(self.game.file_directory + "audio/sunni_dog_attack1.ogg")
            pygame.mixer.music.set_volume(self.game.volume_multiplier)
            pygame.mixer.music.play(0)
        elif r == 2:
            pygame.mixer.music.load(self.game.file_directory + "audio/sunni_dog_attack2.ogg")
            pygame.mixer.music.set_volume(self.game.volume_multiplier)
            pygame.mixer.music.play(0)
        elif r == 3:
            pygame.mixer.music.load(self.game.file_directory + "audio/sunni_dog_attack3.ogg")
            pygame.mixer.music.set_volume(self.game.volume_multiplier)
            pygame.mixer.music.play(0)
