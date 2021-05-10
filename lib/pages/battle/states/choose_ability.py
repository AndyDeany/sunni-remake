from lib.pages.battle.states.battle_state import BattleState


class ChooseAbility(BattleState):
    """Class representing the state of the battle where the player has to choose what move they want ot use."""

    OFFENSIVE_FIRST_ICON_X = 960
    OFFENSIVE_ICON_Y = 390
    OFFENSIVE_INFO_X = 930
    DEFENSIVE_FIRST_ICON_X = 165
    DEFENSIVE_ICON_Y = 330
    DEFENSIVE_INFO_X = 220
    ICON_WIDTH = 40
    ICON_HEIGHT = 40
    ICON_OFFSET = ICON_WIDTH + 10

    def run(self):
        """Run the code for allowing the player to choose which move they want to use."""
        self.game.player.display()
        self.game.opponent.display()

        if self.game.player.selected_moves is None:
            if self.game.mouse.is_in(960, 430, 1100, 540):
                for index, move in enumerate(self.game.player.offensive_moves):
                    icon_x = self.OFFENSIVE_FIRST_ICON_X + self.ICON_OFFSET * index
                    move.icon_faded.display(icon_x, self.OFFENSIVE_ICON_Y)

                if self.game.mouse.left:
                    self.game.player.selected_moves = self.game.player.offensive_moves

            elif self.game.mouse.is_in(135, 380, 235, 520):
                for index, move in enumerate(self.game.player.defensive_moves):
                    icon_x = self.DEFENSIVE_FIRST_ICON_X + self.ICON_OFFSET * index
                    move.icon_faded.display(icon_x, self.DEFENSIVE_ICON_Y)

                if self.game.mouse.left:
                    self.game.player.selected_moves = self.game.player.defensive_moves
        else:
            if self.game.player.selected_moves == self.game.player.offensive_moves:
                first_icon_x = self.OFFENSIVE_FIRST_ICON_X
                icon_y = self.OFFENSIVE_ICON_Y
                info_x = self.OFFENSIVE_INFO_X
                character_boundaries = (930, 380, 1130, 540)
            else:
                first_icon_x = self.DEFENSIVE_FIRST_ICON_X
                icon_y = self.DEFENSIVE_ICON_Y
                info_x = self.DEFENSIVE_INFO_X
                character_boundaries = (150, 320, 220, 560)

            for index, move in enumerate(self.game.player.selected_moves):
                icon_x = first_icon_x + self.ICON_OFFSET * index
                move.icon.display(icon_x, icon_y)
                if self.game.mouse.is_in(icon_x, icon_y, icon_x + self.ICON_WIDTH, icon_y + self.ICON_HEIGHT):
                    move.info.display(info_x, 130)
                    if self.game.mouse.left:
                        self.game.player.use_move(move)

            if self.game.mouse.left and not self.game.mouse.is_in(*character_boundaries):
                self.game.player.selected_moves = None
