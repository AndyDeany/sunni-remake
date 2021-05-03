from lib.battle import Battle
from lib.meme_dog import MemeDog


class MemeDogBattle(Battle):
    def __init__(self, game):
        super().__init__(game)
        self.opponent = MemeDog(self.game, 100, 100)

    def run(self):
        super().run()
        # Default battle screen, where the player chooses which move to use
        if self.current == self.player.CHOOSE_ABILITY:
            self.player.idle_movement(150, 380)
            self.game.opponent.dog_normal.display(930, 440)

            if self.game.mouse.is_in(960, 430, 1100, 540):
                self.player.MOVE_KICK.icon_faded.display(960, 390)
                self.player.MOVE_HEADBUTT.icon_faded.display(1010, 390)
                self.player.MOVE_FROSTBEAM.icon_faded.display(1060, 390)

                if self.game.mouse.left and not self.game.display_options:
                    self.current = "aggressive moves"

            elif self.game.mouse.is_in(135, 380, 235, 520):
                self.player.MOVE_HEAL.icon_faded.display(165, 330)

                if self.game.mouse.left and not self.game.display_options:
                    self.current = "defensive moves"

        # Screen showing the player their aggressive move options
        elif self.current == "aggressive moves":
            self.player.idle_movement(150, 380)
            self.game.opponent.dog_normal.display(930, 440)

            self.player.MOVE_KICK.icon.display(960, 390)
            self.player.MOVE_HEADBUTT.icon.display(1010, 390)
            self.player.MOVE_FROSTBEAM.icon.display(1060, 390)

            if self.game.mouse.is_in(960, 390, 1000, 430):
                self.player.MOVE_KICK.info.display(930, 130)
            elif self.game.mouse.is_in(1010, 390, 1050, 430):
                self.player.MOVE_HEADBUTT.info.display(930, 130)
            elif self.game.mouse.is_in(1060, 390, 1100, 430):
                self.player.MOVE_FROSTBEAM.info.display(930, 130)

            if self.game.mouse.left and not self.game.display_options:
                if self.game.mouse.is_in(960, 390, 1000, 430):
                    self.player.use_move(self.player.MOVE_KICK)
                elif self.game.mouse.is_in(1010, 390, 1050, 430):
                    self.player.use_move(self.player.MOVE_HEADBUTT)
                elif self.game.mouse.is_in(1060, 390, 1100, 430):
                    self.player.use_move(self.player.MOVE_FROSTBEAM)
                elif not self.game.mouse.is_in(930, 380, 1130, 540):
                    self.current = self.player.CHOOSE_ABILITY

        # Screen showing the player their defensive move options
        elif self.current == "defensive moves":
            self.player.idle_movement(150, 380)
            self.game.opponent.dog_normal.display(930, 440)

            self.player.MOVE_HEAL.icon.display(165, 330)

            if self.game.mouse.is_in(165, 330, 205, 370):
                self.player.MOVE_HEAL.info.display(220, 130)

            if self.game.mouse.left and not self.game.display_options:
                if self.game.mouse.is_in(165, 330, 205, 370):
                    self.player.use_move(self.player.MOVE_HEAL)
                elif not self.game.mouse.is_in(150, 320, 220, 560):
                    self.current = self.player.CHOOSE_ABILITY

        # Dog dead/Victory screen
        elif self.current == self.game.opponent.DEAD:
            self.player.idle_movement(150, 380)
            self.game.opponent.dog_dead.display(930, 440)
            self.game.VICTORY_OVERLAY.display()
            self.game.CONTINUE_BUTTON.display()
            self.game.RETURN_TO_TITLE_BUTTON.display()

            if self.game.mouse.left and not self.game.display_options:
                if self.game.mouse.is_in(1000, 600, 1120, 650):
                    self.current = self.player.CHOOSE_ABILITY
                    self.player.level_up()
                    self.game.load_battle("Kanye Snake")
                    self.game.save()
                elif self.game.mouse.is_in(80, 600, 268, 650):
                    self.player.level_up()
                    self.game.load_battle("Kanye Snake")
                    self.game.save()
                    self.current = "title"

        # Character dead/Defeat screen
        elif self.current == self.player.DEAD:
            self.player.character_dead.display(150, 480)
            self.game.opponent.dog_normal.display(930, 440)
            self.game.DEFEAT_OVERLAY.display()
            self.game.TRY_AGAIN_BUTTON.display()
            self.game.RETURN_TO_TITLE_BUTTON.display()

            if self.game.mouse.left and not self.game.display_options:
                if self.game.mouse.is_in(1000, 600, 1200, 700):
                    self.current = self.player.CHOOSE_ABILITY
                    self.player.level_up(0.25)
                    self.player.fully_restore()
                    self.game.opponent.fully_restore()
                    self.game.save()
                elif self.game.mouse.is_in(80, 600, 268, 650):
                    self.game.save()
                    self.current = "title"

        else:  # Moves
            self.current.run()

        self.player.display_stat_change()
        self.game.opponent.display_stat_change()
