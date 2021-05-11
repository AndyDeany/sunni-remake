from lib.pages.battle.states.battle_state import BattleState
from lib.image import Image
from lib.button import Button


class ChooseCharacter(BattleState):
    """Class representing the state of the battle where the player has to choose their character model.

    This should only really happen once - at the start of a playthrough.
    """

    CHARACTER_1 = "character1"
    CHARACTER_2 = "character2"

    def __init__(self):
        self.choose_character_overlay = Image("choose_character_overlay.png", (0, 0))
        self.character1_button = CharacterButton(400, 300, 470, 480, self.CHARACTER_1)
        self.character2_button = CharacterButton(810, 300, 880, 480, self.CHARACTER_2)
        self.character_buttons = (self.character1_button, self.character2_button)

    def run(self):
        """Run the code that asks the player to choose their character sprite."""
        self.choose_character_overlay.display()
        for button in self.character_buttons:
            button.display()

        if self.game.mouse.left:
            for button in self.character_buttons:
                if button.is_hovered:
                    button.on_click()
                    break
            else:
                return
            self.game.page.current = self.game.page.CHOOSE_ABILITY


class CharacterButton(Button):
    """Class representing a button for selecting a certain character on the choose character screen."""

    def __init__(self, start_x, start_y, end_x, end_y, character_name):
        image = Image(f"player/{character_name}_normal1.png", (start_x, start_y))
        super().__init__(start_x, start_y, end_x, end_y, image=image)
        self.character_name = character_name

    def on_click(self):
        self.session.game.player.character = self.character_name
