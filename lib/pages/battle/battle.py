from lib.pages import Page
from lib.image import Image, Text
from lib.font import Font
from lib.color import Color
from lib.pages.battle.states import ChooseCharacter, ChooseAbility, Victory, Defeat


class Battle(Page):
    """Class for representing a battle between the player and a given opponent."""

    @classmethod
    def initialise(cls):
        cls.BATTLE_BACKGROUND_HALLWAY = Image("battle_background_hallway.png", (0, 0))
        cls.CHOOSE_CHARACTER = ChooseCharacter()
        cls.CHOOSE_ABILITY = ChooseAbility()
        cls.VICTORY = Victory()
        cls.DEFEAT = Defeat()

    def __init__(self, game, opponent):
        super().__init__(game)
        self.opponent = opponent
        self.player = self.game.player

        self.not_enough_mana = Text("You don't have enough mana to use that", Font.OPENING, Color.MANA_BLUE, (300, 200))
        self.mana_notification_duration = 0
        self.mana_notification_total_duration = 2 * self.game.fps

        if self.game.player.character is None:
            self.current = self.CHOOSE_CHARACTER
        else:
            self.current = self.CHOOSE_ABILITY

    def run(self):
        """Run the code for execution of the battle with the opponent."""
        self._show_background()
        if self.current == self.CHOOSE_CHARACTER:
            self.current.run()
            return

        self.player.display_info()
        self.opponent.display_info()
        self.game.options_button.run()

        self.current.run()

        self.player.display_stat_change()
        self.opponent.display_stat_change()
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

    def _show_background(self):
        self.BATTLE_BACKGROUND_HALLWAY.display()
