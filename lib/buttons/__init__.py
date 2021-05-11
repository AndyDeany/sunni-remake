from lib.button import Button


class ReturnToTitleButton(Button):
    """Class representing the "Return to Title" button for returning to the main menu."""

    _image_path = "return_to_title_button.png"

    def _on_click(self):
        self.session.game.go_to_main_menu()
