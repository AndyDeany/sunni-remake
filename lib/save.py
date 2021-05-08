from lib.image import Text, Image
from lib.font import Font
from lib.color import Color
from lib.player import Player


class Save:

    EMPTY_SAVE_NAME = "No save data"

    def __init__(self, number):
        self.number = number
        self.file_name = f"../saves/save{self.number+1}.txt"

        y_offset = 119*self.number
        self._display_x = 450
        self._display_y = 230 + y_offset
        self.button_flared = Image(f"load{self.number+1}_flared.png", (0, 0))

        self.button_boundaries = (355, 225+y_offset, 925, 338+y_offset)

        with open(self.file_name, "r") as save_file:
            save_lines = save_file.read().splitlines()
        self.player_name = save_lines[0]
        self.player_level = None
        self.opponent_name = None
        self.player_character = None
        if self.player_name != self.EMPTY_SAVE_NAME:
            self.player_level = float(save_lines[1])
            self.opponent_name = save_lines[2]
            self.player_character = save_lines[3]

    @property
    def player_name(self):
        return self._playername

    @player_name.setter
    def player_name(self, value):
        self._playername = value
        self.player_name_text = Text(value, Font.DEFAULT, Color.BLACK, (self._display_x, self._display_y))
        self.is_empty = value == self.EMPTY_SAVE_NAME

    def save(self, player_name, player_level, opponent_name, player_character):
        """Save the given data to this save, overwriting any currently stored save data."""
        with open(self.file_name, "w", newline="") as save_file:
            save_file.write(f"{player_name}\n")
            save_file.write(f"{player_level}\n")
            save_file.write(f"{opponent_name}\n")
            save_file.write(f"{player_character}\n")
        self.player_name = player_name
        self.player_level = player_level
        self.opponent_name = opponent_name
        self.player_character = player_character

    def display_name(self):
        """Display the name of the save in it's correct spot on the saves screen."""
        self.player_name_text.display()

    def create_player(self, game) -> Player:
        """Create and return a Player() instance based on this save."""
        return Player(game, self.player_name, self.player_character, level=self.player_level)
