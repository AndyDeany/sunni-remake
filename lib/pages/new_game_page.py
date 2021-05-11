from lib.pages.save_page import SavePage
from lib.image import Image, Text
from lib.color import Color
from lib.font import Font
from lib.player import Player
from lib.meme_dog import MemeDog


class NewGamePage(SavePage):
    """Class representing the New Game page for starting a new game."""

    @classmethod
    def initialise(cls):
        super().initialise()
        cls.ENTER_CHARACTER_NAME = Image("enter_character_name.png", (0, 0))
        cls.CONTINUE_BUTTON_FLARED = Image("continue_button_flared.png", (0, 0))
        cls.ARE_YOU_SURE = Image("are_you_sure.png", (0, 0))
        cls.SURE_YES_FLARED = Image("sure_yes_flared.png", (0, 0))
        cls.SURE_NO_FLARED = Image("sure_no_flared.png", (0, 0))

    def __init__(self, game):
        super().__init__(game)
        self.player_name_text = None
        self.display_sure = False
        self.game.keys.start_text_input(16, default_text="Sunni")

    def run(self):
        super().run()
        if self.game.keys.receiving_text_input:
            self._get_name_from_user()
        else:
            self._get_save_selection_from_user()
        self.game.run_options_button()
        self.game.return_to_title_button.run()

    def _get_name_from_user(self):
        """Run the code to get the user's desired character/save name."""
        self.ENTER_CHARACTER_NAME.display()
        if self.game.keys.text_input:    # Only allow the user to continue with a name entered.
            if self.game.keys.enter or self.game.keys.numpad_enter:
                self.game.keys.stop_text_input()
            if self.game.mouse.is_in(553, 404, 727, 442):
                self.CONTINUE_BUTTON_FLARED.display()
                if self.game.mouse.left:
                    self.game.keys.stop_text_input()
        Text(self.game.keys.text_input, Font.SUNNI, Color.BLACK, (370, 338)).display()
        if not self.game.keys.receiving_text_input:
            self.game.player = Player(self.game, self.game.keys.text_input)
            character_name_text = f"Character name: {self.game.player.name}"
            self.player_name_text = Text(character_name_text, Font.DEFAULT, Color.MILD_BLUE, (10, 10))

    def _get_save_selection_from_user(self):
        self.player_name_text.display()
        save_confirmed = False
        if self.display_sure:
            self.ARE_YOU_SURE.display()
            if self.game.mouse.is_in(555, 398, 630, 437):
                self.SURE_YES_FLARED.display()
                if self.game.mouse.left:
                    save_confirmed = True
                    self.display_sure = False
            elif self.game.mouse.is_in(648, 398, 723, 437):
                self.SURE_NO_FLARED.display()
                if self.game.mouse.left:
                    self.game.select_save(None)
                    self.display_sure = False
        else:
            self.show_saves_for_selection()

        if self.game.selected_save is not None:
            if self.game.selected_save.is_empty or save_confirmed:
                self.game.load_next_battle(MemeDog)
                self.game.commence_next_battle()
            else:
                self.display_sure = True
