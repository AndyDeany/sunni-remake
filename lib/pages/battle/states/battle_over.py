from lib.pages.battle.states.battle_state import BattleState
from lib.buttons import ReturnToTitleButton
from lib.button import Button


class BattleOver(BattleState):
    """Class for representing a state when the battle is over, like victory/defeat."""

    def __init__(self):
        self.buttons = [ReturnToTitleButton(80, 600)]
        self.overlay = None

    def run(self):
        """Run the logic for this battle state."""
        self.game.player.display()
        self.game.opponent.display()
        self.overlay.display()
        Button.run_buttons(self.buttons)
