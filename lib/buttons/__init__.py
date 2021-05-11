from lib.button import Button
from lib.image import Image


class ReturnToTitleButton(Button):
    """Class representing the "Return to Title" button for returning to the main menu."""

    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__(start_x, start_y, end_x, end_y, image=Image("return_to_title_button.png", (start_x, start_y)))

    def on_click(self):
        self.session.game.go_to_main_menu()
