from lib.pages.save_page import SavePage
from lib.image import Image, Text
from lib.color import Color
from lib.font import Font
from lib.button import Button
from lib.player import Player
from lib.meme_dog import MemeDog


class NewGamePage(SavePage):
    """Class representing the New Game page for starting a new game."""

    @classmethod
    def initialise(cls):
        super().initialise()
        cls.ENTER_CHARACTER_NAME = Image("enter_character_name.png", (0, 0))
        cls.continue_button = ContinueButton(553, 404, 174, 38, hover_image=Image("continue_button_flared.png", (0, 0)))
        cls.ARE_YOU_SURE = Image("are_you_sure.png", (0, 0))
        cls.yes_button = YesButton(555, 398, 75, 39, hover_image=Image("sure_yes_flared.png", (0, 0)))
        cls.no_button = NoButton(648, 398, 75, 39, hover_image=Image("sure_no_flared.png", (0, 0)))

    def __init__(self, game):
        super().__init__(game)
        self.player_name_text = None
        self.display_sure = False
        self.game.keys.start_text_input(16, default_text="Sunni")
        self.save_confirmed = False

    def run(self):
        super().run()
        if self.game.keys.receiving_text_input:
            self._get_name_from_user()
        else:
            self._get_save_selection_from_user()
        self.game.options_button.run()
        self.game.return_to_title_button.run()

    def _get_name_from_user(self):
        """Run the code to get the user's desired character/save name."""
        self.ENTER_CHARACTER_NAME.display()
        if self.game.keys.text_input:    # Only allow the user to continue with a name entered.
            if self.game.keys.enter or self.game.keys.numpad_enter:
                self.game.keys.stop_text_input()
            self.continue_button.run()
        Text(self.game.keys.text_input, Font.SUNNI, Color.BLACK, (370, 338)).display()
        if not self.game.keys.receiving_text_input:
            self.game.player = Player(self.game, self.game.keys.text_input)
            character_name_text = f"Character name: {self.game.player.name}"
            self.player_name_text = Text(character_name_text, Font.DEFAULT, Color.MILD_BLUE, (10, 10))

    def _get_save_selection_from_user(self):
        self.player_name_text.display()
        self.save_confirmed = False
        if self.display_sure:
            self.ARE_YOU_SURE.display()
            for button in (self.yes_button, self.no_button):
                if button.is_hovered:
                    button.on_hover()
                    break
        else:
            self.show_saves_for_selection()

        if self.game.selected_save is not None:
            if self.game.selected_save.is_empty or self.save_confirmed:
                self.game.load_next_battle(MemeDog)
                self.game.commence_next_battle()
            else:
                self.display_sure = True


class ContinueButton(Button):
    """Class representing the "CONTINUE" button on the new game page, which is pressed after entering your name."""

    def _on_click(self):
        self.session.keys.stop_text_input()


class YesButton(Button):
    """Class representing the "Yes" button on the new game page, to confirm that you wish to overwrite a save."""

    def _on_click(self):
        self.session.game.page.save_confirmed = True
        self.session.game.page.display_sure = False


class NoButton(Button):
    """Class representing the "No" button on the new game page, to cancel overwriting a save."""

    def _on_click(self):
        self.session.game.select_save(None)
        self.session.game.page.display_sure = False
