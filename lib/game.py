from lib.image import Image
from lib.save import Save

from lib.pages.opening_sequence import OpeningSequence
from lib.pages.main_menu import MainMenu
from lib.pages.new_game_page import NewGamePage
from lib.pages.load_game_page import LoadGamePage

from lib.character import Character
from lib.pages.battle import Battle
from lib.meme_dog import MemeDog
from lib.kanye_snake import KanyeSnake
from lib.spook_dog import SpookDog
from lib.evil_cloud import EvilCloud
from lib.pages.battle.states.battle_state import BattleState


class Game:
    """Class representing the main game - everything to do with the functionality of the game."""

    OPPONENT_CLASSES = (MemeDog, KanyeSnake, SpookDog, EvilCloud)
    OPPONENTS = {Opponent.NAME: Opponent for Opponent in OPPONENT_CLASSES}

    @classmethod
    def initialise(cls):
        cls._OPTIONS_BUTTON = Image("options_button.png", (10, 665))
        cls.RETURN_TO_TITLE_BUTTON = Image("return_to_title_button.png", (80, 600))

    def __init__(self, session):
        self.session = session
        self.page = None
        self.saves = [Save(n) for n in range(4)]
        self.selected_save = None
        self.next_battle = None

        self.visit(OpeningSequence)

        self.player = None
        self.opponent = None

        self.initialise()
        NewGamePage.initialise()
        LoadGamePage.initialise()
        BattleState.initialise(self)
        Character.initialise()
        MainMenu.initialise()
        Battle.initialise()

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

    def visit(self, page_class):
        """Go to the page represented by the given class."""
        self.page = page_class(self)

    def go_to_main_menu(self):
        """Go to the main menu."""
        self.visit(MainMenu)

    def save(self):
        """Save the current game state to the currently selected save."""
        opponent = self.opponent
        if self.next_battle is not None:
            opponent = self.next_battle.opponent
        self.selected_save.save(self.player.name, self.player.level, opponent.name, self.player.character)

    def select_save(self, save):
        """Set the save with the given number as the selected save."""
        self.selected_save = save

    def display_save_names(self):
        """Display all save names (for showing on the saves page)."""
        for save in self.saves:
            save.display_name()

    def load(self):
        """Load the game state represented by self.selected_save."""
        self.player = self.selected_save.create_player(self)
        self.load_next_battle(self.OPPONENTS[self.selected_save.opponent_name])
        self.commence_next_battle()

    def load_next_battle(self, opponent_class=None):
        """Load the next battle (it will not actually begin until you call commence_next_battle())."""
        if opponent_class is None:
            opponent_class = self.OPPONENT_CLASSES[self.OPPONENT_CLASSES.index(type(self.opponent)) + 1]
        self.next_battle = Battle(self, opponent_class(self))

    def commence_next_battle(self):
        """Commence the previously loaded next_battle."""
        self.music.stop_music()
        # self.music.play_music(random.choice(self.battle_music))
        if isinstance(self.next_battle.opponent, EvilCloud):
            self.go_to_main_menu()
            return
        self.page = self.next_battle
        self.opponent = self.next_battle.opponent
        self.next_battle = None

    def run_options_button(self):
        """Run the logic to show the "Options" button and act upon it being clicked."""
        self._OPTIONS_BUTTON.display()
        if self.keys.escape or (self.mouse.left and self.mouse.is_in(10, 665, 100, 715)):
            self.options.show()

    def run(self):
        """Code that is executed once per frame - the body of the main program loop."""
        self.page.run()
