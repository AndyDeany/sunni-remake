import random

from lib.character import Character


class Opponent(Character):  # noqa pylint: disable=abstract-methods
    """Class for representing an opponent."""

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

    def attack_options(self):
        """Return the options the opponent can/would choose from for attacking based on their mana."""
        moves = [move for move in self.moves if move is not self.moves.heal]
        moves = [move for move in moves if 0 <= self.current_mana - move.mana_cost <= self.max_mana]
        return moves

    @staticmethod
    def random_weighted(moves_with_weights):
        r = random.random()
        upper_limit = 0
        weight_sum = sum(moves_with_weights.values())
        move = None
        for move, weight in moves_with_weights.items():
            upper_limit += weight / weight_sum
            if r < upper_limit:
                return move
        return move  # Off chance that weights don't sum perfectly to 1 due to computer rounding errors.
