import pygame

from lib.character import Character, NotEnoughManaError


class Player(Character):

    MOVE_KICK = "kick move"
    MOVE_HEADBUTT = "headbutt move"
    MOVE_FROSTBEAM = "frostbeam move"
    MOVE_HEAL = "heal move"

    DEAD = "player dead"
    CHOOSE_ABILITY = "choose ability"

    MANA_COSTS = {
        MOVE_KICK: -10,
        MOVE_HEADBUTT: 20,
        MOVE_FROSTBEAM: 30,
        MOVE_HEAL: 10,
    }

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

    def level_up(self, levels=1):
        old_level = self.level
        self.level += levels
        if int(self.level) > int(old_level):    # i.e. if we actually levelled up
            self.max_hp = 90 + 10*int(self.level)
            self.max_mana = 95 + 5*int(self.level)
            self.fully_restore()

    def use_move(self, move):
        try:
            self.change_mana(move)
        except NotEnoughManaError:
            self.game.show_mana_notification()
        else:
            self.game.hide_mana_notification()
            self.game.current = move

    def next_move(self):
        """Continues to find out the player's next move."""
        if self.current_hp == 0:
            self.game.current = self.DEAD
            return
        self.game.current = self.CHOOSE_ABILITY

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
