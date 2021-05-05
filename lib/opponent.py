from lib.character import Character


class Opponent(Character):

    def next_move(self):
        """Chooses and uses the dog's next move."""
        if self.is_dead:
            return
        next_move = self.choose_move()
        self.change_mana(next_move)
        self.game.page.current = next_move

    def choose_move(self):
        raise NotImplementedError
