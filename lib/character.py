import pygame

from lib.color import Color
from lib.image import Image
from lib.font import Font
from lib.image import Text


class Character:
    """Class representing a character in the game - player, opponent, other NPCs, etc."""

    INFO_X = None

    @classmethod
    def initialise(cls):
        """Initialises class variables. Can only be called after a screen has been created."""
        cls.HEALTH_ICON = Image("health_icon.png")
        cls.MANA_ICON = Image("mana_icon.png")

    def __init__(self, game, name, max_hp=100, max_mana=100, *, level=1, display_stat_x=600, display_stat_y_start=600):
        self.game = game
        self.name = name
        self.name_display = Text(self.name, Font.DEFAULT, Color.BLACK)

        self.num_idle_frames = None
        self.idle_frames = None
        self.idle_fps = None
        self.stage = 0

        self.current_hp_display = None
        self.current_mana_display = None
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._max_mana = max_mana
        self._current_mana = max_mana
        self.render_mana()
        self.render_hp()
        self.level = level
        self.moves = None

        self.display_stat_x = display_stat_x
        self.display_stat_y_start = display_stat_y_start
        self.display_stat_y = None
        self.stat_change_texts = None
        self.reset_stat_change_text_variables()
        self.display_stat_change_time = -1
        self.display_stat_change_duration = int(self.game.fps/2)

        if self.INFO_X < self.game.screen.get_width()//2:
            self.icon_x = self.INFO_X + 200
        else:
            self.icon_x = self.INFO_X - self.HEALTH_ICON.image.get_width()

    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = value
        self.render_hp()

    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = value
        self.render_hp()

    @property
    def current_mana(self):
        return self._current_mana

    @current_mana.setter
    def current_mana(self, value):
        self._current_mana = value
        self.render_mana()

    @property
    def max_mana(self):
        return self._max_mana

    @max_mana.setter
    def max_mana(self, value):
        self._max_mana = value
        self.render_mana()

    @property
    def is_dead(self):
        return self.current_hp == 0

    def display_info(self):
        def draw_resource_bar(coords, resource_percentage, empty_color, full_color):
            pygame.draw.rect(self.game.screen, empty_color, [*coords, 200, 30])
            pygame.draw.rect(self.game.screen, full_color, [*coords, 200*resource_percentage, 30])
            pygame.draw.rect(self.game.screen, Color.BLACK, [*coords, 200, 30], 1)

        draw_resource_bar((self.INFO_X, 30), self.current_hp/self.max_hp, Color.EMPTY_RED, Color.HEALTH_RED)
        draw_resource_bar((self.INFO_X, 60), self.current_mana/self.max_mana, Color.EMPTY_BLUE, Color.MANA_BLUE)

        self.name_display.display(self.INFO_X+5, 2)
        self.current_hp_display.display(self.INFO_X+5, 32)
        self.current_mana_display.display(self.INFO_X+5, 62)
        self.HEALTH_ICON.display(self.icon_x, 20)
        self.MANA_ICON.display(self.icon_x, 50)

    def render_hp(self):
        """Re-renders the HP display of the character. Used when an hp value (current or max) has been changed."""
        self.current_hp_display = Text(f"Health: {self.current_hp}/{self.max_hp}", Font.DEFAULT, Color.BLACK)

    def render_mana(self):
        """Re-renders the mana display of the character. Used when a mana value (current or max) has been changed."""
        self.current_mana_display = Text(f"Mana: {self.current_mana}/{self.max_mana}", Font.DEFAULT, Color.BLACK)

    def display_stat_change(self):
        """Run code for display the stat change number when the character's stats have been changed."""
        if self.display_stat_change_time > 0:
            for index, text in enumerate(self.stat_change_texts):
                text.display(self.display_stat_x, self.display_stat_y+20*index)
            self.display_stat_y -= 3
            self.display_stat_change_time -= 1
        elif self.display_stat_change_time == 0:
            self.reset_stat_change_text_variables()
            self.display_stat_change_time -= 1

    def trigger_stat_change_texts(self):
        """Trigger the display of a recent stat change (or changes)."""
        self.display_stat_change_time = self.display_stat_change_duration

    def reset_stat_change_text_variables(self):
        """Reset the variables used in display stat change texts to their initial values."""
        self.stat_change_texts = []
        self.display_stat_y = self.display_stat_y_start

    def fully_restore(self):
        """Restores the character to full hp and mana."""
        self.current_hp = self.max_hp
        self.current_mana = self.max_mana

    def change_mana(self, move):
        """Change the character's mana based on the given move to be used."""
        if self.current_mana - move.mana_cost < 0:
            raise NotEnoughManaError(move)
        self.current_mana -= move.mana_cost
        self.current_mana = min(self.max_mana, self.current_mana)   # Don't let current mana go over max mana

    def damage(self, amount):
        """Damage the character by the given amount."""
        amount = min(self.current_hp, amount)   # Don't overkill
        self.current_hp -= amount
        self.stat_change_texts.append(Text(f"-{amount}", Font.DEFAULT, Color.DAMAGE_RED))
        self.trigger_stat_change_texts()

    def restore_hp(self, amount):
        """Heal the character for the given amount."""
        amount = min(self.max_hp - self.current_hp, amount)     # Don't overheal
        self.current_hp += amount
        self.stat_change_texts.append(Text(f"+{amount}", Font.DEFAULT, Color.HEAL_GREEN))
        self.trigger_stat_change_texts()

    def damage_mana(self, amount):
        """Remove the given amount of mana from the character (usually because of a mana-drain ability)."""
        amount = min(self.current_mana, amount)     # Don't take mana the character doesn't have
        self.current_mana -= amount
        self.stat_change_texts.append(Text(f"-{amount}", Font.DEFAULT, Color.MANA_BLUE))
        self.trigger_stat_change_texts()

    def restore_mana(self, amount):
        """Restore the given amount of mana to the character."""
        amount = min(self.max_mana - self.current_mana, amount)     # Don't restore over max mana
        self.current_mana += amount
        self.stat_change_texts.append(Text(f"+{amount}", Font.DEFAULT, Color.MANA_BLUE))
        self.trigger_stat_change_texts()

    def idle_animation(self, x, y):
        index = int(self.stage)
        if index >= self.num_idle_frames:
            index = self.num_idle_frames - (index+2)
        character_image = self.idle_frames[index]
        character_image.display(x, y)
        self.stage = round((self.stage + self.idle_fps/self.game.fps) % (2*self.num_idle_frames - 2), 2)

    def display(self):
        """Display the character in it's default state (stationary)."""
        if self.is_dead:
            self._dead_display()
        else:
            self._idle_display()

    def _idle_display(self):
        raise NotImplementedError(f"{type(self)}._idle_display() is not implemented.")

    def _dead_display(self):
        raise NotImplementedError(f"{type(self)}._dead_display() is not implemented.")


class NotEnoughManaError(Exception):
    """Exception to be raised when the player attempts to use a move they don't have enough mana for."""
    def __init__(self, move=None):
        super().__init__(f"Not enough mana to use '{move}'.")
