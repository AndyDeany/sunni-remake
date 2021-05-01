from lib.color import Color


class Character:
    def __init__(self, game, name, max_hp, max_mana, *, level=1, display_stat_x=600, display_stat_y_start=600):
        self.game = game
        self.name = name
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

    def display_stat_change(self):
        print(self.display_stat_y)
        self.game.screen.blit(self.stat_change_text, (self.display_stat_x, self.display_stat_y))
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
        self.stat_change_text = self.game.font.render(f"-{amount}", True, Color.DAMAGE_RED)
        self.trigger_stat_change_text()

    def heal(self, amount):
        """Heals the character for the given amount."""
        amount = min(self.max_hp - self.current_hp, amount)
        self.current_hp += amount
        self.stat_change_text = self.game.font.render(f"+{amount}", True, Color.HEAL_GREEN)
        self.trigger_stat_change_text()


class NotEnoughManaError(Exception):
    """Exception to be raised when the player attempts to use a move they don't have enough mana for."""
    def __init__(self, move=None):
        super().__init__(f"Not enough mana to use '{move}'.")
