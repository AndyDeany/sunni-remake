import os
import time

import pygame

from lib.character import Character
from lib.mouse import Mouse
from lib.keys import Keys
from lib.music import Music
from lib.image import Image
from lib.options import Options
from lib.save import Save
from lib.player import Player
from lib.opening_sequence import OpeningSequence
from lib.main_menu import MainMenu
from lib.new_game_page import NewGamePage
from lib.load_game_page import LoadGamePage
from lib.battle import Battle
from lib.meme_dog import MemeDog


class Game:

    @classmethod
    def initialise(cls):
        cls.OPTIONS_BUTTON = Image("sunni_options_button.png", (10, 665))
        cls.VICTORY_OVERLAY = Image("sunni_victory_overlay.png", (0, 0))
        cls.DEFEAT_OVERLAY = Image("sunni_defeat_overlay.png", (0, 0))
        cls.CONTINUE_BUTTON = Image("sunni_continue_button.png", (1000, 600))
        cls.TRY_AGAIN_BUTTON = Image("sunni_try_again_button.png", (1000, 600))
        cls.RETURN_TO_TITLE_BUTTON = Image("sunni_return_to_title_button.png", (80, 600))

    def __init__(self):
        self.options = Options(self)
        self.screen = pygame.display.set_mode(self.options.window_size)
        self.icon = Image("sunni_game_icon.png")
        self.keys = Keys(self)
        self.current = None
        self.file_directory = os.getcwd()[:-3]
        self.mouse = Mouse()
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.start_time = time.time()
        self.current_time = 0   # The amount of time the program as been running
        self.music = Music(self)
        self.saves = [Save(n) for n in range(4)]
        self.selected_save = None
        self.display_sure = False
        self.is_running = True
        self.battle = None
        self.main_menu = MainMenu(self)
        OpeningSequence.initialise()
        NewGamePage.initialise()
        LoadGamePage.initialise()
        self.opening_sequence = OpeningSequence(self)
        self.opening_sequence.visit()
        self.new_game_page = NewGamePage(self)
        self.load_game_page = LoadGamePage(self)
        self.player = None
        self.opponent = Character(self, None, 100, 100)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon: Image):
        self._icon = icon
        pygame.display.set_icon(icon.image)

    def save(self):
        self.selected_save.save(self.player.name, self.player.level, self.opponent.name, self.player.character)

    def select_save(self, save):
        """Sets the save with the given number as the selected save."""
        self.selected_save = save

    def display_save_names(self):
        """Displays all save names (for showing on the saves page)."""
        for save in self.saves:
            save.display_name()

    def load(self):
        """Load the game state represented by self.selected_save."""
        self.load_battle(self.selected_save.opponent_name)
        self.music.stop_music()
        self.player = self.selected_save.create_player(self)
        self.current = Player.CHOOSE_ABILITY

    def load_battle(self, name):
        if name == "Meme Dog":
            self.opponent = MemeDog(self)
        elif name == "Kanye Snake":
            opponent = Character(self, name, 120, 120)
            opponent.snake_confuse_x = 930
            opponent.snake_position = "normal"
            opponent.snake_confuse_direction = "backwards"
        elif name == "Spook Dog":
            opponent = Character(self, name, 200, 150)
            opponent.ghost_dog_stage = 1     # Variable showing which frame of idle movement the ghost dog is in
            opponent.ghost_dog_glide_x = 930
            opponent.started_glowing = False
            opponent.ghost_dog_attack_time = self.fps/2
            opponent.already_clawed = False
        else:
            raise ValueError(f"Unknown opponent: '{name}'")

        self.battle = Battle(self, self.opponent)

    def run_options_and_return_to_title_logic(self):
        self.RETURN_TO_TITLE_BUTTON.display(1082, 665)
        self.OPTIONS_BUTTON.display(10, 665)
        if self.keys.escape or (self.mouse.is_in(10, 665, 100, 715) and self.mouse.left):
            self.options.show()
        elif self.mouse.is_in(1082, 665, 1270, 715) and self.mouse.left:
            self.main_menu.visit()

    def run(self):
        self.current_time = time.time() - self.start_time
        self.mouse.reset_buttons()
        self.mouse.update_coordinates()
        self.keys.reset()
