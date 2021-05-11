from lib.button import Button
from lib.image import Image


class ReturnToTitleButton(Button):
    """Class representing the "Return to Title" button for returning to the main menu."""

    _button_image = None

    @classmethod
    def _get_image(cls):    # Caching the image since it's used throughout the game and in multiple instances
        if cls._button_image is None:
            cls._button_image = Image("return_to_title_button.png")
        return cls._button_image

    def _on_click(self):
        self.session.game.go_to_main_menu()
