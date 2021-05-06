"""Module containing the player's moves."""
import random

from lib.moves import Move
from lib.image import Image
from lib.music import Audio


class PlayerMove(Move):     # noqa pylint: disable=abstract-method
    """Class for representing one of the player's moves."""
    def __init__(self, mana_cost):
        super().__init__(mana_cost)
        self.icon = None
        self.icon_faded = None
        self.info = None

    @property
    def user(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent


class Kick(PlayerMove):
    """Class for representing the player's kick move."""
    def __init__(self):
        super().__init__(-10)
        self.icon = Image("sunni_kick_move_icon_solid.png")
        self.icon_faded = Image("sunni_kick_move_icon_faded.png")
        self.info = Image("sunni_kick_move_info.png")
        self.sound = Audio("sunni_character_attack1.ogg")

        self.advancing = True
        self.start_x = 150
        self.sound_x = 750
        self.end_x = 870
        self.forward_step = 24
        self.backward_step = 36
        self.tilted_left = True

    def run(self):
        self.opponent.display()
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
                self.user.idle_animation(self.user.x, self.user.y)
                self.user.x -= self.backward_step
            else:   # Reset variables for next time
                self.advancing = True
                self.opponent.next_move()


class Headbutt(PlayerMove):
    """Class for representing the player's headbutt move."""
    def __init__(self):
        super().__init__(20)
        self.icon = Image("sunni_headbutt_move_icon_solid.png")
        self.icon_faded = Image("sunni_headbutt_move_icon_faded.png")
        self.info = Image("sunni_headbutt_move_info.png")
        self.sound = Audio("sunni_character_attack1.ogg")

        self.advancing = True
        self.start_x = 150
        self.sound_x = 750
        self.end_x = 870
        self.forward_step = 24
        self.backward_step = 36

    def run(self):
        self.opponent.display()
        if self.advancing:
            if self.user.x < self.end_x:
                self.user.character_headbutt_stance.display(self.user.x, self.user.y)
                self.user.x += self.forward_step
                if self.user.x == self.sound_x:
                    self.play_sound()
            else:
                self.opponent.damage(random.randint(10, 20))
                self.advancing = False

        if not self.advancing:
            if self.user.x > self.start_x:
                self.user.idle_animation(self.user.x, self.user.y)
                self.user.x -= self.backward_step
            else:   # Reset variables for next time
                self.advancing = True
                self.opponent.next_move()


class Frostbeam(PlayerMove):
    """Class for representing the player's frostbeam move."""
    def __init__(self):
        super().__init__(30)
        self.icon = Image("sunni_frostbeam_move_icon_solid.png")
        self.icon_faded = Image("sunni_frostbeam_move_icon_faded.png")
        self.info = Image("sunni_frostbeam_move_info.png")
        self.sound = Audio("sunni_frostbeam_move.ogg", 0.2)

        self.frostbeam_start = Image("sunni_frostbeam_start.png", (215, 381))
        self.frostbeam_middle = Image("sunni_frostbeam_middle.png")
        self.frostbeam_end = Image("sunni_frostbeam_end.png")

        self.duration = 0
        self.total_duration = 2*self.game.fps

    def run(self):
        self.opponent.display()
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
    """Class for representing the player's heal move."""
    def __init__(self, heart_x, start_y, end_y):
        super().__init__(10)
        self.icon = Image("sunni_heal_move_icon_solid.png")
        self.icon_faded = Image("sunni_heal_move_icon_faded.png")
        self.info = Image("sunni_heal_move_info.png")
        self.sound = Audio("sunni_heal_move.ogg", 0.1)

        self.heart = Image("sunni_heal_heart.png")

        self.heart_x = heart_x
        self.start_y = start_y
        self.end_y = end_y
        self.heart_y = self.start_y
        self.delay_duration = 0

    @property
    def total_delay_duration(self):
        return self.user.display_stat_change_duration

    def run(self):
        self.user.display()
        self.opponent.display()
        if self.heart_y < self.end_y:
            if self.heart_y == self.start_y:
                self.play_sound()
            self.heart.display(self.heart_x, self.heart_y)
            self.heart_y += 5
        elif self.delay_duration < self.total_delay_duration:   # Allow time for stat change to show
            if self.delay_duration == 0:
                self.user.restore_hp(random.randint(5, 15))
            self.delay_duration += 1
        else:
            self.delay_duration = 0
            self.heart_y = self.start_y
            self.opponent.next_move()
