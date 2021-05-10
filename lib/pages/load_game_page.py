from lib.pages.save_page import SavePage


class LoadGamePage(SavePage):
    """Class for representing the page for loading a previous save."""

    def run(self):
        super().run()
        self.show_saves_for_selection()
        if self.game.selected_save is not None:
            if self.game.selected_save.is_empty:
                self.game.select_save(None)  # Don't let the player select an empty save
            else:
                self.game.load()
        self.game.run_options_button()
        self.game.run_return_to_title_button()
