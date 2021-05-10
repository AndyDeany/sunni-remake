from lib.pages.battle.states.battle_state import BattleState
from lib.image import Image


class Defeat(BattleState):
    """Class representing the state of the battle where the player has been defeated by their opponent."""

    def __init__(self):
        self.overlay = Image("defeat_overlay.png", (0, 0))
        self.try_again_button = Image("try_again_button.png", (1000, 600))

    def run(self):
        """Run the code for showing the defeat screen for when the player has been defeated by their opponent."""
        self.game.player.display()
        self.game.opponent.display()
        self.overlay.display()
        self.try_again_button.display()
        self.game.RETURN_TO_TITLE_BUTTON.display()

        if self.game.mouse.left:
            if self.game.mouse.is_in(1000, 600, 1200, 700):
                self.game.page.current = self.game.page.CHOOSE_ABILITY
                self.game.player.fully_restore()
                self.game.opponent.fully_restore()
            elif self.game.mouse.is_in(80, 600, 268, 650):
                self.game.go_to_main_menu()
