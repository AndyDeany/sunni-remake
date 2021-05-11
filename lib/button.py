class Button:

    @classmethod
    def initialise(cls, session):
        cls.session = session

    def __init__(self, start_x, start_y, end_x, end_y, *, image=None, hover_image=None):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.image = image
        self.hover_image = hover_image

    @property
    def is_hovered(self):
        """Return whether or not the button is being hovered over by the user's mouse."""
        return self.session.mouse.is_in(self.start_x, self.start_y, self.end_x, self.end_y)

    def display(self):
        """Run the code for displaying the button in it's default state."""
        if self.image is not None:
            self.image.display()

    def on_hover(self):
        """Run the code for when the button is being hovered over."""
        if self.hover_image is not None:
            self.hover_image.display()
        if self.session.mouse.left:
            self.on_click()

    def on_click(self):
        """Run code for when the button is clicked."""
        raise NotImplementedError

    def run(self):
        """Run all the code for display the button and it's hover/click logic."""
        self.display()
        if self.is_hovered:
            self.on_hover()
