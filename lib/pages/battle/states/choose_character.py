from lib.pages.battle.states.battle_state import BattleState
from lib.image import Image


class ChooseCharacter(BattleState):
    """Class representing the state of the battle where the player has to choose their character model.

    This should only really happen once - at the start of a playthrough.
    """

    CHARACTER_1 = "character1"
    CHARACTER_2 = "character2"

    @classmethod
    def initialise(cls, game):
        super().initialise(game)
        cls.CHOOSE_CHARACTER_OVERLAY = Image("choose_character_overlay.png")
        cls.CHARACTER_CHOICE1 = Image("player/character1_normal1.png")
        cls.CHARACTER_CHOICE2 = Image("player/character2_normal1.png")

    def run(self):
        """Run the code that asks the player to choose their character sprite."""
        self.CHOOSE_CHARACTER_OVERLAY.display(0, 0)
        self.CHARACTER_CHOICE1.display(400, 300)
        self.CHARACTER_CHOICE2.display(810, 300)

        if self.game.mouse.left:
            if self.game.mouse.is_in(400, 300, 470, 480):
                self.game.player.character = self.CHARACTER_1
            elif self.game.mouse.is_in(810, 300, 880, 480):
                self.game.player.character = self.CHARACTER_2

            if self.game.player.character is not None:
                self.game.page.current = self.game.page.CHOOSE_ABILITY
