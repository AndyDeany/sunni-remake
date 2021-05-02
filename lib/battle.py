from lib.image import Image
from lib.sunni_keydown import Keys


class Battle:

    @classmethod
    def initialise(cls):
        cls.BATTLE_BACKGROUND_HALLWAY = Image("images/sunni_battle_background_hallway.png", (0, 0))

    def __init__(self, game):
        self.game = game

    @property
    def player(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent

    @opponent.setter
    def opponent(self, value):
        self.game.opponent = value

    def run(self):
        self.BATTLE_BACKGROUND_HALLWAY.display()
        self.player.display_info()
        self.opponent.display_info()

        # Options button
        self.game.OPTIONS_BUTTON.display(10, 665)
        if (Keys.escape or (self.game.mouse.is_in(10, 665, 100, 715) and self.game.mouse.left == 1))\
                and not self.game.display_options and self.game.current != "choose_character":   # Focus on choosing your character!
            self.game.display_options = True
            self.game.options_just_selected = True


