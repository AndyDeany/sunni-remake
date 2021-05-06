from lib.image import Image
from lib.move import Kick, Headbutt, Frostbeam, Heal
from lib.character import Character, NotEnoughManaError


class Player(Character):

    CHARACTER_1 = "character1"
    CHARACTER_2 = "character2"

    CHOOSE_CHARACTER = "choose character"
    CHOOSE_ABILITY = "choose ability"
    DEAD = "player dead"

    INFO_X = 10

    @classmethod
    def initialise(cls):
        cls.MOVE_KICK = Kick()
        cls.MOVE_HEADBUTT = Headbutt()
        cls.MOVE_FROSTBEAM = Frostbeam()
        cls.MOVE_HEAL = Heal(160, 170, 350)

    def __init__(self, game, name="Sunni", character=None, *, level=1):
        super().__init__(game, name, level=level, display_stat_x=170, display_stat_y_start=360)
        self.calculate_stats()
        self.x = 150
        self.y = 380
        self.num_idle_frames = 4
        self.idle_fps = 6

        self.character = character
        self.offensive_moves = [self.MOVE_KICK, self.MOVE_HEADBUTT, self.MOVE_FROSTBEAM]
        self.defensive_moves = [self.MOVE_HEAL]
        self.selected_moves = None

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        self._character = character
        if character is None:
            return
        self.idle_frames = [Image(f"sunni_{character}_normal{n}.png") for n in range(self.num_idle_frames)]
        self.character_normal = Image(f"sunni_{character}_normal1.png")
        self.character_backwards = Image(f"sunni_{character}_backwards.png")
        self.character_scared = Image(f"sunni_{character}_scared.png", (self.x, self.y))
        self.character_scared_redflash = Image(f"sunni_{character}_scared_redflash.png", (self.x, self.y))
        self.character_tilt_left = Image(f"sunni_{character}_tilt_left.png")
        self.character_tilt_right = Image(f"sunni_{character}_tilt_right.png")
        self.character_dead = Image(f"sunni_{character}_dead.png")
        self.character_headbutt_stance = Image(f"sunni_{character}_headbutt_stance.png")
        self.character_frostbeam_stance = Image(f"sunni_{character}_frostbeam_stance.png", (self.x, self.y))

    def level_up(self, levels=1.0, restore=True):
        """Level the player up by the given number of levels (default 1).
        Restores the player to full if they pass an integer level and `restore==True` (default).
        """
        old_level = self.level
        self.level += levels
        if int(self.level) > int(old_level):    # i.e. if we actually levelled up
            self.calculate_stats()
            if restore:
                self.fully_restore()

    def calculate_stats(self):
        self.max_hp = 90 + 10*int(self.level)
        self.max_mana = 95 + 5*int(self.level)

    def use_move(self, move):
        try:
            self.change_mana(move)
        except NotEnoughManaError:
            self.game.page.show_mana_notification()
        else:
            self.selected_moves = None
            self.game.page.hide_mana_notification()
            self.game.page.current = move

    def next_move(self):
        """Continues to find out the player's next move."""
        if self.is_dead:
            self.game.page.current = self.DEAD
            self.level_up(0.25, restore=False)
            self.game.save()
            return
        self.game.page.current = self.CHOOSE_ABILITY

    def _idle_display(self):
        self.idle_animation(self.x, self.y)

    def _dead_display(self):
        self.character_dead.display(150, 480)
