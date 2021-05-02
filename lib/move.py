import random

from lib.image import Image
from lib.music import Audio


class Move:

    game = None

    @classmethod
    def initialise(cls, game):
        cls.game = game

    def __init__(self, mana_cost):
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

    def run(self):
        raise NotImplementedError(f"{type(self)}.run() not implemented.")


class PlayerMove(Move):
    def __init__(self, mana_cost):
        super().__init__(mana_cost)
        self.icon = None
        self.icon_faded = None
        self.info = None

        self.advancing = True
        self.start_x = 150
        self.sound_x = 750
        self.end_x = 870
        self.forward_step = 24
        self.backward_step = 36

    @property
    def user(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent

    def run(self):
        super().run()


class Kick(PlayerMove):
    def __init__(self):
        super().__init__(-10)
        self.icon = Image("images/sunni_kick_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_kick_move_icon_faded.png")
        self.info = Image("images/sunni_kick_move_info.png")
        self.sound = Audio("sunni_character_attack1.ogg")

        self.tilted_left = True

    def run(self):
        self.opponent.idle_display()
        if self.advancing:
            if self.user.x <= self.end_x:
                image = self.user.character_tilt_left if self.tilted_left else self.user.character_tilt_right
                self.tilted_left = not self.tilted_left
                image.display(self.user.x, self.user.y)
                self.user.x += self.forward_step
                if self.user.x == self.sound_x:
                    self.play_sound()
                if self.user.x == self.end_x:
                    self.opponent.damage(random.randint(8, 12))
                    self.user.x -= self.backward_step
                    self.advancing = False
        else:
            if self.user.x > self.start_x:
                self.user.idle_movement(self.user.x, self.user.y)
                self.user.x -= self.backward_step
            else:   # Reset variables for next time
                self.advancing = True
                self.opponent.next_move()


class Headbutt(PlayerMove):
    def __init__(self):
        super().__init__(20)
        self.icon = Image("images/sunni_headbutt_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_headbutt_move_icon_faded.png")
        self.info = Image("images/sunni_headbutt_move_info.png")
        self.sound = Audio("sunni_character_attack1.ogg")

        self.advancing = True
        self.tilted_left = True

    def run(self):
        self.opponent.idle_display()
        if self.advancing:
            if self.user.x <= self.end_x:
                self.user.character_headbutt_stance.display(self.user.x, self.user.y)
                self.user.x += self.forward_step
                if self.user.x == self.sound_x:
                    self.user.play_sound()
                if self.user.x == self.end_x:
                    self.opponent.damage(random.randint(10, 20))
                    self.user.x -= self.backward_step
                    self.advancing = False

        elif not self.advancing:
            if self.user.x > self.start_x:
                self.user.idle_movement(self.user.x, self.user.y)
                self.user.x -= 36
            else:
                # Resetting variables for next time
                self.advancing = True
                self.opponent.next_move()


class Frostbeam(PlayerMove):
    def __init__(self):
        super().__init__(30)
        self.icon = Image("images/sunni_frostbeam_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_frostbeam_move_icon_faded.png")
        self.info = Image("images/sunni_frostbeam_move_info.png")
        self.sound = Audio("sunni_frostbeam_move.ogg", 0.2)

        self.frostbeam_start = Image("images/sunni_frostbeam_start.png", (215, 381))
        self.frostbeam_middle = Image("images/sunni_frostbeam_middle.png")
        self.frostbeam_end = Image("images/sunni_frostbeam_end.png")

        self.duration = 0
        self.total_duration = 2*self.game.fps

    def run(self):
        self.opponent.idle_display()
        self.user.character_frostbeam_stance.display()
        if self.duration < self.total_duration:
            if self.duration == 0:
                self.play_sound()
            elif self.duration == self.total_duration//2:
                self.opponent.damage(random.randint(15, 30))
            self.frostbeam_start.display()
            for x in range(14):
                self.frostbeam_middle.display(265+50*x, 383+2*x)
            self.duration += 1
        else:   # Resetting variables for next time
            self.duration = 0
            self.opponent.next_move()


class Heal(PlayerMove):
    def __init__(self, heart_x, start_y, end_y):
        super().__init__(10)
        self.icon = Image("images/sunni_heal_move_icon_solid.png")
        self.icon_faded = Image("images/sunni_heal_move_icon_faded.png")
        self.info = Image("images/sunni_heal_move_info.png")
        self.sound = Audio("sunni_heal_move.ogg", 0.1)

        self.heart = Image("images/sunni_heal_heart.png")

        self.heart_x = heart_x
        self.start_y = start_y
        self.end_y = end_y
        self.heart_y = self.start_y

    def run(self):
        self.user.idle_display()
        self.opponent.idle_display()
        if self.heart_y < self.end_y:
            if self.heart_y == self.start_y:
                self.play_sound()
            self.heart.display(self.heart_x, self.heart_y)
            self.heart_y += 5
        else:
            self.user.heal(random.randint(5, 15))
            self.heart_y = self.start_y
            self.opponent.next_move()


def opponent_move(player_move_subclass):
    """Convert the given player's move (a PlayerMove subclass) into a version that can be used by opponents."""
    class OpponentMove(player_move_subclass):
        @property
        def user(self):
            return self.game.opponent

        @property
        def opponent(self):
            return self.game.player

    return OpponentMove


OpponentHeal = opponent_move(Heal)


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

