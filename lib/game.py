import os

from lib.character import Character
from lib.color import Color
from lib.font import Font
from lib.mouse import Mouse
from lib.music import Music
from lib.image import Image, Text
from lib.player import Player
from lib.meme_dog_battle import MemeDogBattle


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
        self.current = "opening sequence"
        self.file_directory = os.getcwd()[:-3]
        self.screen = None
        self.mouse = Mouse()
        self.fps = 30  # Setting fps
        self.music = Music(self)
        self.save_number = None
        self.fullscreen_enabled = False
        self.display_options = False
        self.options_just_selected = False
        self.display_sure = False
        self.battle = None
        self.player = None
        self.opponent = Character(self, None, 100, 100)

    def get_save_path(self, save_number=None):
        """Return the path to the save file of the given save number."""
        save_number = save_number or self.save_number
        if save_number is None:
            raise ValueError("'get_save_path()' requires a 'save_number' that is not 'None'")
        return f"{self.file_directory}saves/save{save_number}.txt"

    def save(self):
        with open(self.get_save_path(), "w") as save_file:
            save_file.write(self.player.name + "\n")
            save_file.write(str(self.player.level) + "\n")
            save_file.write(self.opponent.name + "\n")
            save_file.write(self.player.character + "\n")

    def display_save_name(self, save_number, coords):
        with open(self.get_save_path(save_number), "r") as save_file:
            save_name = save_file.readline().strip()
            save_name_text = Text(save_name, Font.DEFAULT, Color.BLACK)
            save_name_text.display(*coords)
            return save_name

    def load_save(self):
        with open(self.get_save_path(), "r") as save_file:
            save_lines = save_file.read().splitlines()
        character_name = save_lines[0]
        character_level = int(save_lines[1])
        self.load_battle(save_lines[2])
        character = save_lines[3]

        self.music.stop()
        self.player = Player(self, character_name, character, level=character_level)
        self.current = "choose ability"

    def load_battle(self, name):
        if name == "Meme Dog":
            Battle = MemeDogBattle
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

        self.battle = Battle(self)
        self.opponent = self.battle.opponent
