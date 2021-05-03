from lib.image import Image
from lib.move import Kick, Headbutt, Frostbeam, Heal
from lib.character import Character, NotEnoughManaError


class Player(Character):
    DEAD = "player dead"
    CHOOSE_ABILITY = "choose ability"

    INFO_X = 10

    @classmethod
    def initialise(cls):
        cls.MOVE_KICK = Kick()
        cls.MOVE_HEADBUTT = Headbutt()
        cls.MOVE_FROSTBEAM = Frostbeam()
        cls.MOVE_HEAL = Heal(160, 170, 350)

    def __init__(self, game, name, character, *, level=1):
        super().__init__(game, name, level=level, display_stat_x=170, display_stat_y_start=360)
        self.calculate_stats()
        self.character = character

        self.x = 150
        self.y = 380

        self.stage = 0
        self.num_idle_frames = 6
        self.idle_frames = [Image(f"sunni_{self.character}_normal{n}.png") for n in range(self.num_idle_frames)]

        self.character_normal = Image(f"sunni_{character}_normal1.png")
        self.character_backwards = Image(f"sunni_{character}_backwards.png")
        self.character_scared = Image(f"sunni_{character}_scared.png")
        self.character_scared_redflash = Image(f"sunni_{character}_scared_redflash.png")
        self.character_tilt_left = Image(f"sunni_{character}_tilt_left.png")
        self.character_tilt_right = Image(f"sunni_{character}_tilt_right.png")
        self.character_dead = Image(f"sunni_{character}_dead.png")
        self.character_headbutt_stance = Image(f"sunni_{character}_headbutt_stance.png")
        self.character_frostbeam_stance = Image(f"sunni_{character}_frostbeam_stance.png", (self.x, self.y))

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
            self.game.battle.show_mana_notification()
        else:
            self.game.battle.hide_mana_notification()
            self.game.current = move

    def next_move(self):
        """Continues to find out the player's next move."""
        if self.current_hp == 0:
            self.game.current = self.DEAD
            return
        self.game.current = self.CHOOSE_ABILITY

    def idle_display(self):
        self.idle_movement(self.x, self.y)
