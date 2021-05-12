from lib.pages.battle.states.battle_over import BattleOver
from lib.button import Button
from lib.image import Image


class Defeat(BattleOver):
    """Class representing the state of the battle where the player has been defeated by their opponent."""

    def __init__(self):
        super().__init__()
        self.buttons.append(TryAgainButton(1000, 600))
        self.overlay = Image("defeat_overlay.png", (0, 0))


class TryAgainButton(Button):
    """Class representing the "Try Again" button for after the player has been defeated."""

    _image_path = "try_again_button.png"

    def _on_click(self):
        self.session.game.page.current = self.session.game.page.CHOOSE_ABILITY
        self.session.game.player.fully_restore()
        self.session.game.opponent.fully_restore()
