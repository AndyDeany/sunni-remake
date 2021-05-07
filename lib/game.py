import os
import time
from collections import OrderedDict

import pygame

from lib.mouse import Mouse
from lib.keys import Keys
from lib.music import Music
from lib.image import Image, Surface
from lib.options import Options
from lib.save import Save

from lib.pages.opening_sequence import OpeningSequence
from lib.pages.main_menu import MainMenu
from lib.pages.new_game_page import NewGamePage
from lib.pages.load_game_page import LoadGamePage

from lib.character import Character
from lib.pages.battle import Battle
from lib.player import Player
from lib.meme_dog import MemeDog
from lib.kanye_snake import KanyeSnake
from lib.spook_dog import SpookDog
from lib.evil_cloud import EvilCloud
from lib.moves import Move


class Game:

    @classmethod
    def initialise(cls):
        cls.OPTIONS_BUTTON = Image("options_button.png", (10, 665))
        cls.VICTORY_OVERLAY = Image("victory_overlay.png", (0, 0))
        cls.DEFEAT_OVERLAY = Image("defeat_overlay.png", (0, 0))
        cls.CONTINUE_BUTTON = Image("continue_button.png", (1000, 600))
        cls.TRY_AGAIN_BUTTON = Image("try_again_button.png", (1000, 600))
        cls.RETURN_TO_TITLE_BUTTON = Image("return_to_title_button.png", (80, 600))

    def __init__(self):
        pygame.init()
        self.options = Options(self)
        self.screen = pygame.display.set_mode(self.options.window_size)
        self.icon = Image("game_icon.png")
        self.caption = "Sunni (Alpha 3.0.0)"
        self.keys = Keys(self)
        self.page = None
        self.file_directory = os.getcwd()[:-3]
        self.mouse = Mouse()
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.start_time = time.time()
        self.current_time = 0   # The amount of time the program as been running
        self.music = Music(self)
        self.saves = [Save(n) for n in range(4)]
        self.selected_save = None
        self.is_running = True
        self.next_battle = None

        self.main_menu = MainMenu(self)
        self.opening_sequence = OpeningSequence(self)
        self.opening_sequence.visit()
        self.new_game_page = NewGamePage(self)
        self.load_game_page = LoadGamePage(self)

        self.player = None
        self.opponent = None

        self.initialise()
        OpeningSequence.initialise()
        NewGamePage.initialise()
        LoadGamePage.initialise()
        Surface.initialise(self)
        Options.initialise()
        Move.initialise(self)
        Character.initialise()
        Player.initialise()
        MainMenu.initialise()
        MemeDog.initialise()
        Battle.initialise()

        self.opponents = OrderedDict()
        self.opponents["Meme Dog"] = MemeDog
        self.opponents["Kanye Snake"] = KanyeSnake
        self.opponents["Spook Dog"] = SpookDog
        self.opponents["Evil Cloud"] = EvilCloud

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

    def save(self):
        """Save the current game state to the currently selected save."""
        opponent = self.opponent
        if self.next_battle is not None:
            opponent = self.next_battle.opponent
        self.selected_save.save(self.player.name, self.player.level, opponent.name, self.player.character)

    def select_save(self, save):
        """Sets the save with the given number as the selected save."""
        self.selected_save = save

    def display_save_names(self):
        """Displays all save names (for showing on the saves page)."""
        for save in self.saves:
            save.display_name()

    def load(self):
        """Load the game state represented by self.selected_save."""
        self.player = self.selected_save.create_player(self)
        self.load_next_battle(self.selected_save.opponent_name)
        self.commence_next_battle()

    def load_next_battle(self, name=None):
        if name is None:
            opponent_names = list(self.opponents.keys())
            name = opponent_names[opponent_names.index(self.opponent.name) + 1]

        self.next_battle = Battle(self, self.opponents[name](self))
        if name == "Spook Dog":
            opponent = Character(self, name, 200, 150)
            opponent.ghost_dog_stage = 1     # Variable showing which frame of idle movement the ghost dog is in
            opponent.ghost_dog_glide_x = 930
            opponent.started_glowing = False
            opponent.ghost_dog_attack_time = self.fps/2
            opponent.already_clawed = False

    def commence_next_battle(self):
        """Commence the previously loaded next_battle."""
        self.music.stop_music()
        if isinstance(self.next_battle.opponent, EvilCloud):
            self.main_menu.visit()
            return
        self.page = self.next_battle
        self.opponent = self.next_battle.opponent
        self.next_battle = None

    def run_options_and_return_to_title_logic(self):
        self.RETURN_TO_TITLE_BUTTON.display(1082, 665)
        self.OPTIONS_BUTTON.display(10, 665)
        if self.keys.escape or (self.mouse.is_in(10, 665, 100, 715) and self.mouse.left):
            self.options.show()
        elif self.mouse.is_in(1082, 665, 1270, 715) and self.mouse.left:
            self.main_menu.visit()

    def event_handling(self):
        """Run the code for the main event loop to deal with user inputs/actions."""
        for event in pygame.event.get():    # "For each thing the user does"
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.TEXTINPUT:
                self.keys.process_text_input(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.process_button_down()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse.process_button_up()
            elif event.type == pygame.KEYDOWN:
                self.keys.process_key_down(event)
                self.keys.process_text_input_special_keys()
            elif event.type == pygame.KEYUP:
                self.keys.process_key_up(event)

    def loop(self):
        """Run the main program loop."""
        while self.is_running:
            self.run()

        # Closing the program
        try:
            self.save()
        except (NameError, AttributeError, ValueError):  # in case saving is not yet possible
            pass

        pygame.quit()

    def run(self):
        """Code that is executed once per frame - the body of the main program loop."""
        self.current_time = time.time() - self.start_time
        self.mouse.reset_buttons()
        self.mouse.update_coordinates()
        self.keys.reset()
        self.event_handling()

        if self.options.is_showing and self.page != self.opening_sequence:
            self.options.display()
        else:
            self.page.run()

        pygame.display.flip()       # Updating the screen at the end of drawing
        self.clock.tick(self.fps)   # Setting fps limit
