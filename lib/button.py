from lib.image import Image


class Button:

    _image_path = None

    @classmethod
    def initialise(cls, session):
        cls.session = session

    def __init__(self, x, y, width=None, height=None, *, image=None, hover_image=None):
        self.image = image or self._get_image()
        self.hover_image = hover_image
        if None in (width, height):
            width, height = self.image.image.get_size()
        self.boundaries = (x, y, x + width, y + height)

        self.display_coords = (x, y)
        if self.image and None not in (self.image.default_x, self.image.default_y):
            self.display_coords = (self.image.default_x, self.image.default_y)

        self.hover_display_coords = (x, y)
        if self.hover_image and None not in (self.hover_image.default_x, self.hover_image.default_y):
            self.hover_display_coords = (self.hover_image.default_x, self.hover_image.default_y)

    def _get_image(self):
        """Return an Image() instance for this class using cls.image_path if set by subclasses."""
        if self._image_path is None:
            return None
        return Image(self._image_path)

    @property
    def is_hovered(self):
        """Return whether or not the button is being hovered over by the user's mouse."""
        return self.session.mouse.is_in(*self.boundaries)

    @property
    def is_clicked(self):
        """Return whether or not the button is being clicked on by the user."""
        return self.session.mouse.left and self.is_hovered

    @property
    def is_held(self):
        """Return whether or not the button is being held down by the user."""
        return self.session.mouse.left.is_pressed and self.is_hovered

    def display(self):
        """Run the code for displaying the button in it's default state."""
        if self.image is not None:
            self.image.display(*self.display_coords)

    def on_hover(self):
        """Run the code for when the button is being hovered over."""
        self._on_hover()

    def _on_hover(self):
        if self.hover_image is not None:
            self.hover_image.display(*self.hover_display_coords)
        if self.session.mouse.left:
            self.on_click()

    def on_click(self):
        """Run the code for when the button is clicked."""
        self._on_click()

    def _on_click(self):
        raise NotImplementedError

    def run(self):
        """Run all the code for display the button and it's hover/click logic."""
        self.display()
        if self.is_hovered:
            self.on_hover()

    @staticmethod
    def run_buttons(list_of_buttons):
        """Run multiple buttons simultaneously, stopping after a hovered button is found for optimisation purposes."""
        for button in list_of_buttons:
            button.display()
        for button in list_of_buttons:
            if button.is_hovered:
                button.on_hover()
                break
