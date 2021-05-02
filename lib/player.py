import pygame

from lib.image import Image
from lib.music import Audio
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

    INFO_X = 10

    def __init__(self, game, name, character, *, level=1):
        super().__init__(game, name, level=level, display_stat_x=170, display_stat_y_start=360)
        self.calculate_stats()
        self.character = character

        # Heal move variables
        self.heal_heart_y = 170
        # Kick move variables
        self.kick_x = 150
        self.tilt_direction = "left"
        # Headbutt move variables
        self.headbutt_x = 150

        self.stage = 0
        self.num_idle_frames = 6
        self.idle_frames = [Image(f"images/sunni_{self.character}_normal{n}.png") for n in range(self.num_idle_frames)]

        self.character_normal = Image(f"images/sunni_{character}_normal1.png")
        self.character_backwards = Image(f"images/sunni_{character}_backwards.png")
        self.character_scared = Image(f"images/sunni_{character}_scared.png")
        self.character_scared_redflash = Image(f"images/sunni_{character}_scared_redflash.png")
        self.character_tilt_left = Image(f"images/sunni_{character}_tilt_left.png")
        self.character_tilt_right = Image(f"images/sunni_{character}_tilt_right.png")
        self.character_dead = Image(f"images/sunni_{character}_dead.png")
        self.character_headbutt_stance = Image(f"images/sunni_{character}_headbutt_stance.png")
        self.character_frostbeam_stance = Image(f"images/sunni_{character}_frostbeam_stance.png")

        self.heal_sound = Audio("sunni_heal_move.ogg", 0.1)
        self.basic_attack_sound = Audio("sunni_character_attack1.ogg")
        self.frostbeam_sound = Audio("sunni_frostbeam_move.ogg", 0.2)

    def level_up(self, levels=1):
        old_level = self.level
        self.level += levels
        if int(self.level) > int(old_level):    # i.e. if we actually levelled up
            self.calculate_stats()
            self.fully_restore()

    def calculate_stats(self):
        self.max_hp = 90 + 10*int(self.level)
        self.max_mana = 95 + 5*int(self.level)

    def idle_movement(self, x, y):
        character_image = self.idle_frames[int(self.stage)]
        character_image.display(x, y)
        self.stage = round((self.stage + 0.2) % self.num_idle_frames, 2)

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
        self.game.music.play_sound(self.heal_sound)

    # Defining a function to play a sound when the character attack (with kick or headbutt)
    def attack_sound(self):
        self.game.music.play_sound(self.basic_attack_sound)

    # Defining a function to play a sound when frostbeam is user
    def frostbeam_move_sound(self):
        self.game.music.play_sound(self.frostbeam_sound)
