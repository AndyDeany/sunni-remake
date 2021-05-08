from collections import OrderedDict

from lib.image import Image
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

    def __init__(self, session):
        self.session = session
        self.page = None
        self.saves = [Save(n) for n in range(4)]
        self.selected_save = None
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

        # self.battle_music = [Audio(f"battle{n}.ogg", 0.2) for n in range(8)]

    @property
    def screen(self):
        return self.session.screen

    @property
    def keys(self):
        return self.session.keys

    @property
    def mouse(self):
        return self.session.mouse

    @property
    def fps(self):
        return self.session.fps

    @property
    def options(self):
        return self.session.options

    @property
    def music(self):
        return self.session.music

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
        """Load the next battle (it will not actually begin until you call commence_next_battle().)"""
        if name is None:
            opponent_names = list(self.opponents.keys())
            name = opponent_names[opponent_names.index(self.opponent.name) + 1]
        self.next_battle = Battle(self, self.opponents[name](self))

    def commence_next_battle(self):
        """Commence the previously loaded next_battle."""
        self.music.stop_music()
        # self.music.play_music(random.choice(self.battle_music))
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

    def run(self):
        """Code that is executed once per frame - the body of the main program loop."""
        self.page.run()
