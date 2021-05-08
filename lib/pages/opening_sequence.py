import time


from lib.pages import Page
from lib.color import Color
from lib.font import Font
from lib.image import Image, Text


class OpeningSequence(Page):
    """Class that manages the opening sequence of the game."""

    def __init__(self, game):
        super().__init__(game)
        self.welcome_l1 = Text("Welcome to Sunni!", Font.OPENING, Color.BLACK)
        self.welcome_l2 = Text("This is coded entirely with Python and the pygame module!", Font.OPENING, Color.BLACK)
        self.welcome_l3 = Text("created by Andrew and co.", Font.OPENING, Color.BLACK)
        self.welcome_l4 = Text("Enjoy!", Font.OPENING, Color.BLACK)

        self.title_screen = Image("title_screen.png", (0, 0))
        self.game_title = Text("SUNNI", Font.TITLE, Color.MURKY_YELLOW)

        self.start_time = self.game.session.uptime

    @property
    def time_elapsed(self):
        return self.game.session.uptime - self.start_time

    def run(self):
        if self.time_elapsed < 5:
            self.game.screen.fill(Color.MILD_BLUE)
            self.welcome_l1.display(480, 100)
            if self.game.mouse.left and self.time_elapsed <= 0.5:  # Enables skipping by clicking
                self.start_time = self.game.session.uptime - 0.5
            if self.time_elapsed > 0.5:
                self.welcome_l2.display(150, 140)
                if self.game.mouse.left and self.time_elapsed <= 2:
                    self.start_time = self.game.session.uptime - 2
            if self.time_elapsed > 2:
                self.welcome_l3.display(690, 500)
                if self.game.mouse.left and self.time_elapsed <= 3:
                    self.start_time = self.game.session.uptime - 3
            if self.time_elapsed > 3:
                self.welcome_l4.display(590, 300)
                if self.game.mouse.left and self.time_elapsed <= 5:
                    self.start_time = self.game.session.uptime - 5
        elif self.time_elapsed < 8:
            self.title_screen.display()
            if self.game.mouse.left and self.time_elapsed <= 6:
                self.start_time = self.game.session.uptime - 6

            if self.time_elapsed > 6:
                self.game_title.display(555, 100)
                if self.game.mouse.left:
                    self.start_time = self.game.session.uptime - 8
        else:
            self.game.go_to_main_menu()
