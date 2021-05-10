import time

import pygame

from lib.game import Game
from lib.image import Image
from lib.keys import Keys
from lib.mouse import Mouse
from lib.options import Options
from lib.music import Music

from lib.image import Surface


class Session:
    """Class for representing a game session and related variables.

    Contains metadata about the game like it's screen, window size, etc.
    Does not contain anything about the actual gameplay within the game.
    """

    def __init__(self):
        pygame.init()
        window_size = (1280, 720)
        self.screen = pygame.display.set_mode(window_size, flags=pygame.SCALED)
        self.icon = Image("game_icon.png")
        self.caption = "Sunni (Alpha 3.0.0)"
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.uptime = 0     # The amount of time the program has been running
        self.is_running = True

        self.keys = Keys(self)
        self.mouse = Mouse()
        self.options = Options(self, window_size)
        self.music = Music()

        self.game = Game(self)

        Surface.initialise(self)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon: Image):
        self._icon = icon
        pygame.display.set_icon(icon.image)

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, caption: str):
        self._caption = caption
        pygame.display.set_caption(caption)

    def event_handling(self):
        """Run the code for the main event loop to deal with user inputs/actions."""
        for event in pygame.event.get():    # "For each thing the user does"
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.TEXTINPUT:
                self.keys.process_text_input(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.process_button_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse.process_button_up(event)
            elif event.type == pygame.KEYDOWN:
                self.keys.process_key_down(event)
                self.keys.process_text_input_special_keys()
            elif event.type == pygame.KEYUP:
                self.keys.process_key_up(event)

    def loop(self):
        """Run the main program loop."""
        while self.is_running:
            self.uptime = time.time() - self.start_time
            self.mouse.reset_buttons()
            self.mouse.update_coordinates()
            self.keys.reset()
            self.event_handling()

            if self.options.is_showing:
                self.options.display()
            else:
                self.game.run()

            pygame.display.flip()
            self.clock.tick(self.fps)

        self.quit()

    def quit(self):
        """Close the program cleanly and safely."""
        try:
            self.game.save()
        except (NameError, AttributeError, ValueError):  # in case saving is not yet possible
            pass

        pygame.quit()
