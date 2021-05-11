from lib.pages.battle.states.battle_state import BattleState
from lib.button import Button


class ChooseAbility(BattleState):
    """Class representing the state of the battle where the player has to choose what move they want ot use."""

    OFFENSIVE_FIRST_ICON_X = 960
    OFFENSIVE_ICON_Y = 390
    DEFENSIVE_FIRST_ICON_X = 165
    DEFENSIVE_ICON_Y = 330
    ICON_WIDTH = 40
    ICON_OFFSET = ICON_WIDTH + 10

    def __init__(self):
        self.moves_buttons = None
        self.offensive_move_buttons = None
        self.defensive_move_buttons = None
        self.selected_move_buttons = None

    def _initialise_buttons(self):
        self.moves_buttons = (CharacterMovesButton(960, 430, 140, 110, self.game.player.offensive_moves,
                                                   self.OFFENSIVE_FIRST_ICON_X, self.OFFENSIVE_ICON_Y),
                              CharacterMovesButton(135, 380, 100, 140, self.game.player.defensive_moves,
                                                   self.DEFENSIVE_FIRST_ICON_X, self.DEFENSIVE_ICON_Y))
        self.offensive_move_buttons = []
        for index, move in enumerate(self.game.player.offensive_moves):
            icon_x = self.OFFENSIVE_FIRST_ICON_X + self.ICON_OFFSET * index
            self.offensive_move_buttons.append(MoveButton(icon_x, self.OFFENSIVE_ICON_Y, move, info_x=930))
        self.defensive_move_buttons = []
        for index, move in enumerate(self.game.player.defensive_moves):
            icon_x = self.DEFENSIVE_FIRST_ICON_X + self.ICON_OFFSET * index
            self.defensive_move_buttons.append(MoveButton(icon_x, self.DEFENSIVE_ICON_Y, move, info_x=220))

    def run(self):
        """Run the code for allowing the player to choose which move they want to use."""
        self.game.player.display()
        self.game.opponent.display()

        if self.moves_buttons is None:
            self._initialise_buttons()  # May need re-calling if moves/order change in runtime (at least move_buttons)

        if self.game.player.selected_moves is None:
            for button in self.moves_buttons:
                if button.is_hovered:
                    button.on_hover()
        else:
            if self.game.player.selected_moves == self.game.player.offensive_moves:
                move_buttons = self.offensive_move_buttons
                character_boundaries = (930, 380, 1130, 540)
            else:
                move_buttons = self.defensive_move_buttons
                character_boundaries = (150, 320, 220, 560)

            for move_button in move_buttons:
                move_button.run()

            if self.game.mouse.left and not self.game.mouse.is_in(*character_boundaries):
                self.game.player.selected_moves = None


class CharacterMovesButton(Button):
    """Class representing a character as a button to be clicked on to show the moves that can be used on it."""

    def __init__(self, x, y, width, height, moves, first_icon_x, icon_y):
        super().__init__(x, y, width, height)
        self.moves = moves
        self.first_icon_x = first_icon_x
        self.icon_y = icon_y

    def _on_hover(self):
        for index, move in enumerate(self.moves):
            icon_x = self.first_icon_x + ChooseAbility.ICON_OFFSET * index
            move.icon_faded.display(icon_x, self.icon_y)
            if self.session.mouse.left:
                self.on_click()

    def _on_click(self):
        self.session.game.player.selected_moves = self.moves


class MoveButton(Button):
    """Class representing a button to use a move."""

    INFO_Y = 130

    def __init__(self, x, y, move, info_x):
        super().__init__(x, y, image=move.icon)
        self.move = move
        self.info_x = info_x

    def _on_hover(self):
        self.move.info.display(self.info_x, self.INFO_Y)
        if self.session.mouse.left:
            self.on_click()

    def _on_click(self):
        self.session.game.player.use_move(self.move)
