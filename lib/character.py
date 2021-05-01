class Character:
    def __init__(self, game, name, max_hp, max_mana, *, level=1, display_stat_x=600, display_stat_y_start=600):
        self.game = game
        self.name = name
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mana = max_mana
        self.current_mana = self.max_mana
        self.level = level

        self.display_stat_x = display_stat_x
        self.display_stat_y_start = display_stat_y_start
        self.display_stat_y = self.display_stat_y_start
        self.display_stat_change_time = 0

    def display_stat_change(self):
        self.game.screen.blit(self.stat_change_text, (self.display_stat_x, self.display_stat_y))
        self.display_stat_y -= 3

    def reset_display_stat_y(self):
        """Reset the display_stat_y attribute to its starting value."""
        self.display_stat_y = self.display_stat_y_start

    def trigger_stat_change_text(self):
        self.display_stat_change_time = self.game.fps/2
