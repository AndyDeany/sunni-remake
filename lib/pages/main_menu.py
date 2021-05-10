from lib.pages import Page
from lib.button import Button
from lib.pages.new_game_page import NewGamePage
from lib.pages.load_game_page import LoadGamePage
from lib.image import Image
from lib.music import Audio


class MainMenu(Page):
    """Class for representing the main menu of the game."""

    @classmethod
    def initialise(cls):
        cls.MUSIC = Audio("title_screen_music.ogg", 0.1)
        cls.MAIN_MENU = Image("main_menu.png", (0, 0))
        cls.buttons = (PlayButton(), LoadButton(), OptionsButton(), ExitButton())

    def __init__(self, game):
        super().__init__(game)
        self.game.music.stop_sounds()
        if self.game.music.current_music != self.MUSIC:
            self.game.music.play_music(self.MUSIC)
        self.game.select_save(None)
        self.game.next_battle = None

    def run(self):
        self.MAIN_MENU.display()
        for button in self.buttons:
            if button.is_hovered:
                button.on_hover()
                break   # Can't be hovering more than one button at the same time.
        if self.game.keys.escape:
            self.game.options.show()


class PlayButton(Button):
    """Class representing the "PLAY" button on the main menu."""

    def __init__(self):
        super().__init__(535, 269, 744, 345)
        self.hover_image = Image("menu_play_flared.png", (79, 0))

    def on_click(self):
        """Run the code for what happens when the button is clicked."""
        self.session.game.visit(NewGamePage)


class LoadButton(Button):
    """Class representing the "LOAD" button on the main menu."""

    def __init__(self):
        super().__init__(406, 375, 877, 451)
        self.hover_image = Image("menu_load_flared.png", (82, 106))

    def on_click(self):
        """Run the code for what happens when the button is clicked."""
        self.session.game.visit(LoadGamePage)


class OptionsButton(Button):
    """Class representing the "OPTIONS" button on the main menu."""

    def __init__(self):
        super().__init__(461, 481, 817, 557)
        self.hover_image = Image("menu_options_flared.png", (82, 212))

    def on_click(self):
        """Run the code for what happens when the button is clicked."""
        self.session.game.options.show()


class ExitButton(Button):
    """Class representing the "EXIT" button on the main menu."""

    def __init__(self):
        super().__init__(547, 585, 734, 661)
        self.hover_image = Image("menu_exit_flared.png", (166, 476))

    def on_click(self):
        """Run the code for what happens when the button is clicked."""
        self.session.is_running = False
