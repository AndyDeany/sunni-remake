from lib.pages.battle.states.battle_state import BattleState
from lib.button import Button
from lib.image import Image


class Victory(BattleState):
    """Class representing the state of the battle where the player has defeated their opponent."""

    def __init__(self):
        self.overlay = Image("victory_overlay.png", (0, 0))
        self.continue_button = ContinueButton(1000, 600, 1120, 650)

    def run(self):
        """Run the code for showing the victory screen for when the player has defeated their opponent."""
        self.game.player.display()
        self.game.opponent.display()
        self.overlay.display()
        self.continue_button.display()
        self.game.RETURN_TO_TITLE_BUTTON.display()

        if self.game.next_battle is None:
            self.game.player.level_up()
            self.game.load_next_battle()
            self.game.save()

        if self.game.mouse.left:
            if self.continue_button.is_hovered:
                self.continue_button.on_click()
            elif self.game.mouse.is_in(80, 600, 268, 650):
                self.game.go_to_main_menu()


class ContinueButton(Button):
    """Class for representing the "Continue" button for the player to progress to the next part of the game."""

    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__(start_x, start_y, end_x, end_y, image=Image("continue_button.png", (start_x, start_y)))

    def on_click(self):
        self.session.game.commence_next_battle()
