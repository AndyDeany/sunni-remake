from lib.image import Image, Text
from lib.font import Font
from lib.color import Color
from lib.player import Player
from lib.move import Move


class Battle:

    @classmethod
    def initialise(cls):
        cls.BATTLE_BACKGROUND_HALLWAY = Image("sunni_battle_background_hallway.png", (0, 0))
        cls.CHOOSE_CHARACTER_OVERLAY = Image("sunni_choose_character_overlay.png")
        cls.CHARACTER_CHOICE1 = Image("sunni_character1_normal1.png")
        cls.CHARACTER_CHOICE2 = Image("sunni_character2_normal1.png")

    def __init__(self, game, opponent):
        self.game = game
        self.opponent = opponent

        self.not_enough_mana = Text("You don't have enough mana to use that", Font.OPENING, Color.MANA_BLUE, (300, 200))
        self.mana_notification_duration = 0
        self.mana_notification_total_duration = 2 * self.game.fps

    @property
    def player(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent

    @opponent.setter
    def opponent(self, value):
        self.game.opponent = value

    @property
    def current(self):
        return self.game.current

    @current.setter
    def current(self, value):
        self.game.current = value

    def run_all(self):
        """Runs the early_run(), run(), and late_run() methods."""
        self.show_background()
        if self.game.current == Player.CHOOSE_CHARACTER:
            self.run_choose_character()
            return
        self.run()
        self.late_run()

    def run(self):
        self.player.display_info()
        self.opponent.display_info()

        # Options button
        self.game.OPTIONS_BUTTON.display(10, 665)
        if self.game.keys.escape or (self.game.mouse.left and self.game.mouse.is_in(10, 665, 100, 715)):
            self.game.options.show()

        # Default battle screen, where the player chooses which move to use
        if self.current == self.player.CHOOSE_ABILITY:
            self.player.idle_display()
            self.opponent.idle_display()

            offensive_first_icon_x = 960
            offensive_icon_y = 390
            offensive_info_x = 930
            defensive_first_icon_x = 165
            defensive_icon_y = 330
            defensive_info_x = 220
            icon_width = 40
            icon_height = 40
            icon_offset = icon_width + 10

            if self.player.selected_moves is None:
                if self.game.mouse.is_in(960, 430, 1100, 540):
                    for index, move in enumerate(self.player.offensive_moves):
                        icon_x = offensive_first_icon_x + icon_offset*index
                        move.icon_faded.display(icon_x, offensive_icon_y)

                    if self.game.mouse.left:
                        self.player.selected_moves = self.player.offensive_moves

                elif self.game.mouse.is_in(135, 380, 235, 520):
                    for index, move in enumerate(self.player.defensive_moves):
                        icon_x = defensive_first_icon_x + icon_offset*index
                        move.icon_faded.display(icon_x, defensive_icon_y)

                    if self.game.mouse.left:
                        self.player.selected_moves = self.player.defensive_moves
            else:
                if self.player.selected_moves == self.player.offensive_moves:
                    first_icon_x = offensive_first_icon_x
                    icon_y = offensive_icon_y
                    info_x = offensive_info_x
                    character_boundaries = (930, 380, 1130, 540)
                else:
                    first_icon_x = defensive_first_icon_x
                    icon_y = defensive_icon_y
                    info_x = defensive_info_x
                    character_boundaries = (150, 320, 220, 560)

                for index, move in enumerate(self.player.selected_moves):
                    icon_x = first_icon_x + icon_offset*index
                    move.icon.display(icon_x, icon_y)
                    if self.game.mouse.is_in(icon_x, icon_y, icon_x + icon_width, icon_y + icon_height):
                        move.info.display(info_x, 130)
                        if self.game.mouse.left:
                            self.player.use_move(move)

                if self.game.mouse.left and not self.game.mouse.is_in(*character_boundaries):
                    self.player.selected_moves = None

        # Opponent dead/Victory screen
        elif self.current == self.opponent.DEAD:
            self.player.idle_display()
            self.opponent.dead_display()
            self.game.VICTORY_OVERLAY.display()
            self.game.CONTINUE_BUTTON.display()
            self.game.RETURN_TO_TITLE_BUTTON.display()

            # levelup, changing battle to kanye snake, saving, should all really be done here
            # but need to find a way to do that whilst still running the code for this battle

            if self.game.mouse.left:
                if self.game.mouse.is_in(1000, 600, 1120, 650):
                    self.player.level_up()
                    self.game.load_battle("Kanye Snake")
                    self.game.save()
                    self.current = self.player.CHOOSE_ABILITY
                elif self.game.mouse.is_in(80, 600, 268, 650):
                    self.player.level_up()
                    self.game.load_battle("Kanye Snake")
                    self.game.save()
                    self.game.main_menu.visit()

        # Player dead/Defeat screen
        elif self.current == self.player.DEAD:
            self.player.dead_display()
            self.opponent.idle_display()
            self.game.DEFEAT_OVERLAY.display()
            self.game.TRY_AGAIN_BUTTON.display()
            self.game.RETURN_TO_TITLE_BUTTON.display()

            # Repeated code from below need moving here, similar to above victory screen code.

            if self.game.mouse.left:
                if self.game.mouse.is_in(1000, 600, 1200, 700):
                    self.player.level_up(0.25)
                    self.game.save()
                    self.current = self.player.CHOOSE_ABILITY
                    self.player.fully_restore()
                    self.game.opponent.fully_restore()
                elif self.game.mouse.is_in(80, 600, 268, 650):
                    self.player.level_up(0.25)
                    self.game.save()
                    self.game.main_menu.visit()

        elif isinstance(self.current, Move):  # Moves
            self.current.run()

        self.player.display_stat_change()
        self.game.opponent.display_stat_change()

    def late_run(self):
        self.mana_notification_display()

    def mana_notification_display(self):
        """Run the code for actually showing the mana notification when needed."""
        if self.mana_notification_duration > 0:
            self.not_enough_mana.display()
            self.mana_notification_duration -= 1

    def show_mana_notification(self):
        """Show the 'not enough mana' notification to the player."""
        self.mana_notification_duration = self.mana_notification_total_duration

    def hide_mana_notification(self):
        """Stop displaying the 'not enough mana' notification to the player, if it's showing."""
        self.mana_notification_duration = 0

    def show_background(self):
        self.BATTLE_BACKGROUND_HALLWAY.display()

    def run_choose_character(self):
        self.CHOOSE_CHARACTER_OVERLAY.display(0, 0)
        self.CHARACTER_CHOICE1.display(400, 300)
        self.CHARACTER_CHOICE2.display(810, 300)

        if self.game.mouse.left:
            if self.game.mouse.is_in(400, 300, 470, 480):
                self.player.character = Player.CHARACTER_1
            elif self.game.mouse.is_in(810, 300, 880, 480):
                self.player.character = Player.CHARACTER_2

            if self.player.character is not None:
                self.game.current = Player.CHOOSE_ABILITY
