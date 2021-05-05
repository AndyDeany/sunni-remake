from lib.page import Page
from lib.image import Image
from lib.music import Audio


class MainMenu(Page):

    @classmethod
    def initialise(cls):
        cls.MAIN_MENU = Image("sunni_main_menu.png", (0, 0))
        cls.PLAY_BUTTON_FLARED = Image("sunni_menu_play_flared.png", (79, 0))
        cls.LOAD_BUTTON_FLARED = Image("sunni_menu_load_flared.png", (82, 106))
        cls.OPTIONS_BUTTON_FLARED = Image("sunni_menu_options_flared.png", (82, 212))
        cls.EXIT_BUTTON_FLARED = Image("sunni_menu_exit_flared.png", (166, 476))

        cls.MUSIC = Audio("sunni_title_screen_music.ogg", 0.1)

    def run(self):
        self.MAIN_MENU.display()
        if self.game.mouse.is_in(535, 269, 744, 345):       # Play button
            self.PLAY_BUTTON_FLARED.display()
            if self.game.mouse.left:
                self.game.new_game_page.visit()
        elif self.game.mouse.is_in(406, 375, 877, 451):     # Load button
            self.LOAD_BUTTON_FLARED.display()
            if self.game.mouse.left:
                self.game.load_game_page.visit()
        elif self.game.mouse.is_in(461, 481, 817, 557):     # Options button
            self.OPTIONS_BUTTON_FLARED.display()
            if self.game.mouse.left:
                self.game.options.show()
        elif self.game.mouse.is_in(547, 585, 734, 661):     # Exit button
            self.EXIT_BUTTON_FLARED.display()
            if self.game.mouse.left:
                self.game.is_running = False
        if self.game.keys.escape:
            self.game.options.show()

    def visit(self):
        """Go to the main menu."""
        super().visit()
        self.game.music.stop_sounds()
        if self.game.music.current_music != self.MUSIC:
            self.game.music.play_music(self.MUSIC)
        self.game.select_save(None)
        self.game.next_battle = None
