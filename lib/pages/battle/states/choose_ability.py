from lib.pages.battle.states.battle_state import BattleState
from lib.button import Button


class ChooseAbility(BattleState):
    """Class representing the state of the battle where the player has to choose what move they want ot use."""

    def __init__(self):
        self.moves_buttons = None

    def _initialise_buttons(self):
        self.moves_buttons = (CharacterMovesButton(960, 430, 140, 110, self.game.player.offensive_moves, 960, 390, 930),
                              CharacterMovesButton(135, 380, 100, 140, self.game.player.defensive_moves, 165, 330, 220))

    def run(self):
        """Run the code for allowing the player to choose which move they want to use."""
        if self.moves_buttons is None:
            self._initialise_buttons()  # May need re-calling if moves/order change in runtime (at least move_buttons)

        self.game.player.display()
        self.game.opponent.display()
        for button in self.moves_buttons:
            button.run()


class CharacterMovesButton(Button):
    """Class representing a character as a button to be clicked on to show the moves that can be used on it."""

    ICON_WIDTH = 40
    BUFFER = 10
    ICON_OFFSET = ICON_WIDTH + BUFFER

    def __init__(self, x, y, width, height, moves, first_icon_x, icon_y, info_x):
        super().__init__(x, y, width, height)
        self.moves = moves
        self.first_icon_x = first_icon_x
        self.icon_y = icon_y
        self.move_buttons = []
        icon_x = self.first_icon_x
        for index, move in enumerate(self.moves):
            icon_x = self.first_icon_x + self.ICON_OFFSET * index
            self.move_buttons.append(MoveButton(icon_x, self.icon_y, move, info_x=info_x))
        self.click_off_boundaries = (min(first_icon_x - self.BUFFER, x), icon_y - self.BUFFER,
                                     max(icon_x + self.ICON_WIDTH + self.BUFFER, x + width), y + height)

    def _on_hover(self):
        for move_button in self.move_buttons:
            move_button.display_faded()
        if self.session.mouse.left:
            self.on_click()

    def _on_click(self):
        self.session.game.player.selected_moves = self.moves

    def run(self):
        if self.session.game.player.selected_moves is None:
            if self.is_hovered:
                self.on_hover()
        elif self.session.game.player.selected_moves is self.moves:
            for move_button in self.move_buttons:
                move_button.run()
            if self.session.mouse.left and not self.session.mouse.is_in(*self.click_off_boundaries):
                self.session.game.player.selected_moves = None


class MoveButton(Button):
    """Class representing a button to use a move."""

    INFO_Y = 130

    def __init__(self, x, y, move, info_x):
        move.info.default_x = info_x
        move.info.default_y = self.INFO_Y
        super().__init__(x, y, image=move.icon, hover_image=move.info)
        self.move = move

    def _on_click(self):
        self.session.game.player.use_move(self.move)

    def display_faded(self):
        """Display the move's icon faded out."""
        self.move.icon_faded.display(*self.boundaries[:2])
