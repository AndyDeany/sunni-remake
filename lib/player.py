import pygame

from lib.character import Character


class Player(Character):
    def __init__(self, game, name, max_hp, max_mana, *, level=1):
        super().__init__(game, name, max_hp, max_mana, level=level, display_stat_x=170, display_stat_y_start=360)
        # Heal move variables
        self.heal_heart_y = 170
        self.healed_already = False
        # Kick move variables
        self.kick_x = 150
        self.tilt_direction = "left"
        # Headbutt move variables
        self.headbutt_x = 150
        # Other
        self.stage = 1

    def level_up(self, *, levels=1):
        self.level += 1
        self.fully_restore()

    def fully_restore(self):
        self.max_hp = 90 + 10 * int(self.level)
        self.current_hp = 90 + 10 * int(self.level)
        self.max_mana = 95 + 5 * int(self.level)
        self.current_mana = 95 + 5 * int(self.level)

    # Defining a function to play a sound when heal heart is used
    def heal_move_sound(self):
        pygame.mixer.music.load(self.game.file_directory + "audio/sunni_heal_move.ogg")
        pygame.mixer.music.set_volume(0.1 * self.game.volume_multiplier)
        pygame.mixer.music.play(0)

    # Defining a function to play a sound when the character attack (with kick or headbutt)
    def attack_sound(self):
        pygame.mixer.music.load(self.game.file_directory + "audio/sunni_character_attack1.ogg")
        pygame.mixer.music.set_volume(self.game.volume_multiplier)
        pygame.mixer.music.play(0)

    # Defining a function to play a sound when frostbeam is user
    def frostbeam_move_sound(self):
        pygame.mixer.music.load(self.game.file_directory + "audio/sunni_frostbeam_move.ogg")
        pygame.mixer.music.set_volume(0.2 * self.game.volume_multiplier)
        pygame.mixer.music.play(0)
