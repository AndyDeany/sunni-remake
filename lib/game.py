import os


from lib.character import Character
from lib.color import Color
from lib.player import Player
from lib.meme_dog import MemeDog


class Game:
    def __init__(self):
        self.current = "title"
        self.file_directory = os.getcwd()[:-3]
        self.screen = None
        self.music_playing = False
        self.fps = 30  # Setting fps
        self.fullscreen_enabled = False
        self.display_options = False
        self.options_just_selected = False
        self.display_sure = False
        self.player = Player(self, None, 100, 100)
        self.opponent = Character(self, None, 100, 100)
        self.character_number = None
        self.duration_time = 0          # Variable to show how long something has been occuring (will be changed by other parts of the program)
        self.damage_decided = False     # Variable to show whether or not the damage that will be done has been calculated already, so it is not done multiple times in loops
        self.advancing = True
        self.retreating = False
        self.display_damage_time = self.fps
        self.volume_multiplier = 1

    def get_save_path(self, save_number):
        """Return the path to the save file of the given save number."""
        return f"{self.file_directory}saves/save{save_number}.txt"

    def save(self):
        with open(self.get_save_path(self.save_number), "w") as save_file:
            save_file.write(self.player.name + "\n")
            save_file.write(str(self.player.level) + "\n")
            save_file.write(self.opponent.name + "\n")
            save_file.write(self.character_number + "\n")

    def display_save_name(self, save_number, coords):
        with open(self.get_save_path(save_number), "r") as save_file:
            save_name = save_file.readline()
            save_name_text = self.font.render(save_name[:-1], True, Color.BLACK)
            self.screen.blit(save_name_text, coords)
            return save_name

    def assign_enemy_stats(self, opponent_name):
        if opponent_name == "Meme Dog":
            opponent = MemeDog(self, 100, 100)
        elif opponent_name == "Kanye Snake":
            opponent = Character(self, opponent_name, 120, 120)
            opponent.snake_confuse_x = 930
            opponent.snake_position = "normal"
            opponent.snake_confuse_direction = "backwards"
        elif opponent_name == "Spook Dog":
            opponent = Character(self, opponent_name, 200, 150)
            opponent.ghost_dog_stage = 1     # Variable showing which frame of idle movement the ghost dog is in
            opponent.ghost_dog_glide_x = 930
            opponent.started_glowing = False
            opponent.ghost_dog_attack_time = self.fps/2
            opponent.already_clawed = False
        else:
            raise ValueError(f"Unknown opponent: '{opponent_name}'")

        return opponent

    def display_stat_change(self, display_x):
        self.screen.blit(self.display_damage, (display_x, self.player.display_damage_y))
        self.player.display_damage_y -= 3
