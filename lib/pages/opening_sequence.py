import time


from lib.pages import Page
from lib.color import Color
from lib.font import Font
from lib.image import Image, Text


class OpeningSequence(Page):
    """Class the manages the opening sequence of the game."""

    @classmethod
    def initialise(cls):
        cls.WELCOME_L1 = Text("Welcome to Sunni!", Font.OPENING, Color.BLACK)
        cls.WELCOME_L2 = Text("This is coded entirely with Python and the pygame module!", Font.OPENING, Color.BLACK)
        cls.WELCOME_L3 = Text("created by Andrew and co.", Font.OPENING, Color.BLACK)
        cls.WELCOME_L4 = Text("Enjoy!", Font.OPENING, Color.BLACK)

        cls.TITLE_SCREEN = Image("title_screen.png", (0, 0))
        cls.GAME_TITLE = Text("SUNNI", Font.TITLE, Color.MURKY_YELLOW)

    def run(self):
        if self.game.session.uptime < 5:
            self.game.screen.fill(Color.MILD_BLUE)
            self.WELCOME_L1.display(480, 100)
            if self.game.mouse.left and self.game.session.uptime <= 2:  # Enables skipping by clicking
                self.game.session.start_time = time.time() - 0.5
            if self.game.session.uptime > 0.5:
                self.WELCOME_L2.display(150, 140)
                if self.game.mouse.left and self.game.session.uptime <= 2:
                    self.game.session.start_time = time.time() - 2
            if self.game.session.uptime > 2:
                self.WELCOME_L3.display(690, 500)
                if self.game.mouse.left and self.game.session.uptime <= 3:
                    self.game.session.start_time = time.time() - 3
            if self.game.session.uptime > 3:
                self.WELCOME_L4.display(590, 300)
                if self.game.mouse.left and self.game.session.uptime <= 5:
                    self.game.session.start_time = time.time() - 5
        elif self.game.session.uptime < 8:
            self.TITLE_SCREEN.display()
            if self.game.mouse.left and self.game.session.uptime <= 6:
                self.game.session.start_time = time.time() - 6

            if self.game.session.uptime > 6:
                self.GAME_TITLE.display(555, 100)
                if self.game.mouse.left:
                    self.game.session.start_time = time.time() - 8
        else:
            self.game.main_menu.visit()
