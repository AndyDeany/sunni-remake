import random

from lib.image import Image
from lib.music import Audio


class Move:

    game = None

    @classmethod
    def initialise(cls, game):
        cls.game = game

    def __init__(self, mana_cost):
        self.icon = None
        self.icon_faded = None
        self.info = None
        self._sound = None

        self.mana_cost = mana_cost

    def play_sound(self):
        self.game.music.play_sound(self.sound)

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, value):
        self._sound = value


class Kick(Move):
    def __init__(self):
        super().__init__(-10)
        self.icon = Image("images/sunni_kick_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_kick_move_icon_faded.png")
        self.info = Image("images/sunni_kick_move_info.png")
        self.sound = Audio("sunni_character_attack1.ogg")


class Headbutt(Move):
    def __init__(self):
        super().__init__(20)
        self.icon = Image("images/sunni_headbutt_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_headbutt_move_icon_faded.png")
        self.info = Image("images/sunni_headbutt_move_info.png")
        self.sound = Audio("sunni_character_attack1.ogg")


class Frostbeam(Move):
    def __init__(self):
        super().__init__(30)
        self.icon = Image("images/sunni_frostbeam_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_frostbeam_move_icon_faded.png")
        self.info = Image("images/sunni_frostbeam_move_info.png")
        self.sound = Audio("sunni_frostbeam_move.ogg", 0.2)


class Heal(Move):
    def __init__(self):
        super().__init__(10)
        self.icon = Image("images/sunni_heal_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_heal_move_icon_faded.png")
        self.info = Image("images/sunni_heal_move_info.png")
        self.sound = Audio("sunni_heal_move.ogg", 0.1)


class MemeDogMove(Move):
    def __init__(self, mana_cost):
        super().__init__(mana_cost)
        self.sounds = [Audio(f"sunni_dog_attack{n}.ogg") for n in range(1, 4)]

    @property
    def sound(self):
        return random.choice(self.sounds)


class Bark(MemeDogMove):
    def __init__(self):
        super().__init__(-10)


class Bite(MemeDogMove):
    def __init__(self):
        super().__init__(15)


class Spin(MemeDogMove):
    def __init__(self):
        super().__init__(25)

