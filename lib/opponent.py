from lib.character import Character


class Opponent(Character):

    INFO_X = 1070

    DEAD = "opponent dead"

    def __init__(self, game, name, max_hp, max_mana, *, level=1, display_stat_x=1015, display_stat_y_start=420):
        super().__init__(game, name, max_hp, max_mana, level=level,
                         display_stat_x=display_stat_x, display_stat_y_start=display_stat_y_start)

    def next_move(self):
        """Chooses and uses the dog's next move."""
        if self.is_dead:
            self.game.page.current = self.DEAD
            return
        next_move = self.choose_move()
        self.change_mana(next_move)
        self.game.page.current = next_move

    def choose_move(self):
        raise NotImplementedError
