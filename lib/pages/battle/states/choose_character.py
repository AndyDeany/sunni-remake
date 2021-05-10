from lib.pages.battle.states.battle_state import BattleState
from lib.image import Image


class ChooseCharacter(BattleState):
    """Class representing the state of the battle where the player has to choose their character model.

    This should only really happen once - at the start of a playthrough.
    """

    CHARACTER_1 = "character1"
    CHARACTER_2 = "character2"

    def __init__(self):
        self.choose_character_overlay = Image("choose_character_overlay.png", (0, 0))
        self.character_choice1 = Image("player/character1_normal1.png", (400, 300))
        self.character_choice2 = Image("player/character2_normal1.png", (810, 300))

    def run(self):
        """Run the code that asks the player to choose their character sprite."""
        self.choose_character_overlay.display()
        self.character_choice1.display()
        self.character_choice2.display()

        if self.game.mouse.left:
            if self.game.mouse.is_in(400, 300, 470, 480):
                self.game.player.character = self.CHARACTER_1
            elif self.game.mouse.is_in(810, 300, 880, 480):
                self.game.player.character = self.CHARACTER_2

            if self.game.player.character is not None:
                self.game.page.current = self.game.page.CHOOSE_ABILITY
