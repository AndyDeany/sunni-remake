from lib.pages.battle.states import BattleState


class Victory(BattleState):
    """Class representing the state of the battle where the player has defeated their opponent."""

    def run(self):
        """Run the code for showing the victory screen for when the player has defeated their opponent."""
        self.game.player.display()
        self.game.opponent.display()
        self.game.VICTORY_OVERLAY.display()
        self.game.CONTINUE_BUTTON.display()
        self.game.RETURN_TO_TITLE_BUTTON.display()

        if self.game.next_battle is None:
            self.game.player.level_up()
            self.game.load_next_battle()
            self.game.save()

        if self.game.mouse.left:
            if self.game.mouse.is_in(1000, 600, 1120, 650):
                self.game.commence_next_battle()
            elif self.game.mouse.is_in(80, 600, 268, 650):
                self.game.go_to_main_menu()
