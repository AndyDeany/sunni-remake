from lib.pages.battle.states import BattleState


class Defeat(BattleState):
    """Class representing the state of the battle where the player has been defeated by their opponent."""

    def run(self):
        """Run the code for showing the defeat screen for when the player has been defeated by their opponent."""
        self.game.player.display()
        self.game.opponent.display()
        self.game.DEFEAT_OVERLAY.display()
        self.game.TRY_AGAIN_BUTTON.display()
        self.game.RETURN_TO_TITLE_BUTTON.display()

        if self.game.mouse.left:
            if self.game.mouse.is_in(1000, 600, 1200, 700):
                self.game.page.current = self.game.page.CHOOSE_ABILITY
                self.game.player.fully_restore()
                self.game.opponent.fully_restore()
            elif self.game.mouse.is_in(80, 600, 268, 650):
                self.game.go_to_main_menu()
