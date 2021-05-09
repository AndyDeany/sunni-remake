class BattleState:
    """Class for representing a state of a battle.

    Some examples include whether the player is currently choosing what move to use,
    what move they are using, and whether they have reached victory or defeat.
    """

    @classmethod
    def initialise(cls, game):
        cls.game = game

    def run(self):
        raise NotImplementedError
