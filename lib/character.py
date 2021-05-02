import math

import pygame

from lib.color import Color
from lib.image import Image
from lib.font import Font
from lib.image import Text


class Character:

    INFO_X = None

    @classmethod
    def initialise(cls):
        """Initialises class variables. Can only be called after a screen has been created."""
        cls.HEALTH_ICON = Image("images/sunni_health_icon.png")
        cls.MANA_ICON = Image("images/sunni_mana_icon.png")

    def __init__(self, game, name, max_hp=100, max_mana=100, *, level=1, display_stat_x=600, display_stat_y_start=600):
        self.game = game
        self.name = name
        self.name_display = Text(self.name, Font.DEFAULT, Color.BLACK)

        self.current_hp_display = None
        self.current_mana_display = None
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._max_mana = max_mana
        self._current_mana = max_mana
        self.render_mana()
        self.render_hp()
        self.level = level

        self.stat_change_text = None
        self.display_stat_x = display_stat_x
        self.display_stat_y_start = display_stat_y_start
        self.display_stat_y = self.display_stat_y_start
        self.display_stat_change_time = -1
        self.display_stat_change_duration = int(self.game.fps/2)

        self.is_advancing = True
        self.is_retreating = False

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

        icon_x = self.INFO_X + math.copysign(200, self.game.screen.get_width() - self.INFO_X)
        self.HEALTH_ICON.display(icon_x, 20)
        self.MANA_ICON.display(icon_x, 50)

    def render_hp(self):
        """Re-renders the HP display of the character. Used when an hp value (current or max) has been changed."""
        self.current_hp_display = Text(f"Health: {self.current_hp}/{self.max_hp}", Font.DEFAULT, Color.BLACK)

    def render_mana(self):
        """Re-renders the mana display of the character. Used when a mana value (current or max) has been changed."""
        self.current_mana_display = Text(f"Mana: {self.current_mana}/{self.max_mana}", Font.DEFAULT, Color.BLACK)

    def display_stat_change(self):
        self.stat_change_text.display(self.display_stat_x, self.display_stat_y)
        self.display_stat_y -= 3

    def reset_display_stat_y(self):
        """Reset the display_stat_y attribute to its starting value."""
        self.display_stat_y = self.display_stat_y_start

    def trigger_stat_change_text(self):
        self.display_stat_change_time = self.display_stat_change_duration

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
        """Damages the character by the given amount."""
        amount = min(self.current_hp, amount)   # Don't overkill
        self.current_hp -= amount
        self.stat_change_text = Text(f"-{amount}", Font.DEFAULT, Color.DAMAGE_RED)
        self.trigger_stat_change_text()

    def heal(self, amount):
        """Heals the character for the given amount."""
        amount = min(self.max_hp - self.current_hp, amount)
        self.current_hp += amount
        self.stat_change_text = Text(f"+{amount}", Font.DEFAULT, Color.HEAL_GREEN)
        self.trigger_stat_change_text()

    def idle_display(self):
        raise NotImplementedError(f"{type(self)}.idle_display() is not implemented.")


class NotEnoughManaError(Exception):
    """Exception to be raised when the player attempts to use a move they don't have enough mana for."""
    def __init__(self, move=None):
        super().__init__(f"Not enough mana to use '{move}'.")
