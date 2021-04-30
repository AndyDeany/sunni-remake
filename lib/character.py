class Character:
    def __init__(self, game, name, max_hp, max_mana, *, level=1):
        self.game = game
        self.name = name
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mana = max_mana
        self.current_mana = self.max_mana
        self.level = level
