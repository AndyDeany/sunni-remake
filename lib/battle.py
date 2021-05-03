from lib.image import Image, Text
from lib.font import Font
from lib.color import Color
from lib.sunni_keydown import Keys


class Battle:

    @classmethod
    def initialise(cls):
        cls.BATTLE_BACKGROUND_HALLWAY = Image("sunni_battle_background_hallway.png", (0, 0))

    def __init__(self, game):
        self.game = game

        self.not_enough_mana = Text("You don't have enough mana to use that", Font.OPENING, Color.MANA_BLUE, (300, 200))
        self.mana_notification_duration = 0
        self.mana_notification_total_duration = 2 * self.game.fps

    @property
    def player(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent

    @opponent.setter
    def opponent(self, value):
        self.game.opponent = value

    @property
    def current(self):
        return self.game.current

    @current.setter
    def current(self, value):
        self.game.current = value

    def run_all(self):
        """Runs the early_run(), run(), and late_run() methods."""
        self.run()
        self.late_run()

    def run(self):
        self.show_background()
        self.player.display_info()
        self.opponent.display_info()

        # Options button
        self.game.OPTIONS_BUTTON.display(10, 665)
        if (self.game.keys.escape or (self.game.mouse.is_in(10, 665, 100, 715) and self.game.mouse.left == 1))\
                and not self.game.display_options and self.game.current != "choose_character":   # Focus on choosing your character!
            self.game.display_options = True
            self.game.options_just_selected = True

    def late_run(self):
        self.mana_notification_display()

    def mana_notification_display(self):
        """Run the code for actually showing the mana notification when needed."""
        if self.mana_notification_duration > 0:
            self.not_enough_mana.display()
            self.mana_notification_duration -= 1

    def show_mana_notification(self):
        """Show the 'not enough mana' notification to the player."""
        self.mana_notification_duration = self.mana_notification_total_duration

    def hide_mana_notification(self):
        """Stop displaying the 'not enough mana' notification to the player, if it's showing."""
        self.mana_notification_duration = 0

    def show_background(self):
        self.BATTLE_BACKGROUND_HALLWAY.display()
