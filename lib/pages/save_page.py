from lib.pages import Page
from lib.image import Image


class SavePage(Page):   # noqa pylint: disable=abstract-method

    @classmethod
    def initialise(cls):
        cls.LOAD_GAME_SCREEN = Image("sunni_load_game_screen.png", (0, 0))

    def run(self):
        self.LOAD_GAME_SCREEN.display()
        self.game.display_save_names()

    def show_saves_for_selection(self):
        for save in self.game.saves:
            if self.game.mouse.is_in(*save.button_boundaries):
                save.button_flared.display()
                save.display_name()
                if self.game.mouse.left:
                    self.game.select_save(save)
