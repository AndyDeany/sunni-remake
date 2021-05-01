from lib.color import Color
from lib.font import Font
from lib.image import Text


class Character:
    def __init__(self, game, name, max_hp, max_mana, *, level=1, display_stat_x=600, display_stat_y_start=600):
        self.game = game
        self.name = name
        self.name_display = Text(self.name, Font.DEFAULT, Color.BLACK)

        self.current_hp_display = None
        self.current_mana_display = None
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mana = max_mana
        self.current_mana = self.max_mana
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
        mana_cost = self.MANA_COSTS[move]
        if self.current_mana - mana_cost < 0:
            raise NotEnoughManaError(move)
        self.current_mana -= mana_cost
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


class NotEnoughManaError(Exception):
    """Exception to be raised when the player attempts to use a move they don't have enough mana for."""
    def __init__(self, move=None):
        super().__init__(f"Not enough mana to use '{move}'.")
