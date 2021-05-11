from lib.pages.battle.states.battle_over import BattleOver
from lib.button import Button
from lib.image import Image


class Victory(BattleOver):
    """Class representing the state of the battle where the player has defeated their opponent."""

    def __init__(self):
        super().__init__()
        self.buttons.append(ContinueButton(1000, 600, 1120, 650))
        self.overlay = Image("victory_overlay.png", (0, 0))

    def run(self):
        """Run the code for showing the victory screen for when the player has defeated their opponent."""
        if self.game.next_battle is None:
            self.game.player.level_up()
            self.game.load_next_battle()
            self.game.save()
        super().run()


class ContinueButton(Button):
    """Class for representing the "Continue" button for the player to progress to the next part of the game."""

    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__(start_x, start_y, end_x, end_y, image=Image("continue_button.png", (start_x, start_y)))

    def on_click(self):
        self.session.game.commence_next_battle()
