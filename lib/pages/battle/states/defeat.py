from lib.pages.battle.states.battle_state import BattleState
from lib.button import Button
from lib.image import Image


class Defeat(BattleState):
    """Class representing the state of the battle where the player has been defeated by their opponent."""

    def __init__(self):
        self.overlay = Image("defeat_overlay.png", (0, 0))
        self.try_again_button = TryAgainButton(1000, 600, 1200, 700)

    def run(self):
        """Run the code for showing the defeat screen for when the player has been defeated by their opponent."""
        self.game.player.display()
        self.game.opponent.display()
        self.overlay.display()
        self.try_again_button.display()
        self.game.RETURN_TO_TITLE_BUTTON.display()

        if self.game.mouse.left:
            if self.try_again_button.is_hovered:
                self.try_again_button.on_click()
            elif self.game.mouse.is_in(80, 600, 268, 650):
                self.game.go_to_main_menu()


class TryAgainButton(Button):
    """Class representing the "Try Again" button for after the player has been defeated."""

    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__(start_x, start_y, end_x, end_y, image=Image("try_again_button.png", (start_x, start_y)))

    def on_click(self):
        """Run the code for when the button is clicked."""
        self.session.game.page.current = self.session.game.page.CHOOSE_ABILITY
        self.session.game.player.fully_restore()
        self.session.game.opponent.fully_restore()
