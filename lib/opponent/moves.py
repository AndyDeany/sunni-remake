"""Module containing the base class for opponent moves and opponent versions of the player's moves."""
from lib.moves import opponent_move, Move
from lib.player.moves import Heal


OpponentMove = opponent_move(Move)

OpponentHeal = opponent_move(Heal)
