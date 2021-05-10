"""Module containing Spook Dog's (unique) moves."""
import math

from lib.opponent.moves import OpponentMove
from lib.image import Image
from lib.music import Audio
from lib.color import Color


class SpookDogMove(OpponentMove):     # noqa pylint: disable=abstract-method
    """Class for representing one of Spook Dog's moves."""


class Teleport(SpookDogMove):
    """Class for representing the Teleport move."""

    def __init__(self):
        super().__init__(0, 10, 1, mana_damage=10, mana_healing=10)
        self.sound = Audio("spook_dog/ghost_dog_teleport.ogg")

        self.duration = 0
        self.damage_time = 2 * self.game.fps
        self.total_duration = 2.5 * self.game.fps

        self.glows = [Image(f"spook_dog/ghost_dog_glow{n}.png", (830, 290)) for n in range(5)]

    def run(self):
        self.opponent.display()
        if self.duration < self.damage_time:
            self.user.display()
            if self.duration == 0:
                self.play_sound()
            glow_phase = 5 - abs(5 - self.duration % 10)  # 0 1 2 3 4 5 4 3 2 1 0 1 2 3...
            if glow_phase != 0:  # 0 is no glow
                self.glows[glow_phase - 1].display()
        else:
            self.user.idle_animation(220, 380)
            if self.duration == self.damage_time:
                self.deal_damage()
                self.deal_mana_damage()

        if self.duration < self.total_duration:
            self.duration += 1
        else:
            self.duration = 0
            self.restore_mana()
            self.opponent.next_move()


class Glide(SpookDogMove):
    """Class for representing the Glide move."""

    START_X = 930
    SOUND_X = 570
    END_X = -366
    DAMAGE_X = 210
    FORWARD_STEP = 24

    AMPLITUDE = 200
    OSCILLATIONS = 1.5

    def __init__(self):
        super().__init__(10, 25, 0.2)
        self.sound = Audio("spook_dog/ghost_dog_glide.ogg")

        self.range = self.FORWARD_STEP * math.ceil(self.game.screen.get_width() / self.FORWARD_STEP)
        self.wavelength = self.range / self.OSCILLATIONS

    def run(self):
        self.opponent.display()
        y = self.user.y + int(self.AMPLITUDE * math.sin((2 * math.pi / self.wavelength) * (self.user.x - self.START_X)))
        self.user.idle_animation(self.user.x, y)
        if self.user.x == self.SOUND_X:
            self.play_sound()
        elif self.user.x == self.DAMAGE_X:
            self.deal_damage()
        elif self.user.x <= 0:
            self.user.idle_animation(self.user.x + self.range, y)

        if self.user.x == self.END_X:
            self.opponent.next_move()
            self.user.x = self.START_X
        else:
            self.user.x -= self.FORWARD_STEP


class Claw(SpookDogMove):
    """Class for representing the Claw move."""

    def __init__(self):
        super().__init__(50, 35, 0.71)
        self.sound = Audio("spook_dog/ghost_dog_claw.ogg")

        self.fade_overlays = [Image(f"fade_overlay{10*(n+1)}.png", (0, 0)) for n in range(10)]
        self.opacity = 0

        top_claw_swipes = [Image(f"spook_dog/ghost_dog_top_claw_swipe{n}.png", (145, 365)) for n in range(5)]
        top_claw_sizes = [Image(f"spook_dog/ghost_dog_top_claw_size{n}.png", (145, 365)) for n in range(8)]
        top_claw_fades = [Image(f"spook_dog/ghost_dog_top_claw_fade{20*(n+1)}.png", (145, 365)) for n in range(4)]
        self.top_claw_frames = top_claw_swipes + top_claw_sizes + list(reversed(top_claw_fades))

        side_claw_swipes = [Image(f"spook_dog/ghost_dog_side_claw_swipe{n}.png", (130, 420)) for n in range(5)]
        side_claw_sizes = [Image(f"spook_dog/ghost_dog_side_claw_size{n}.png", (130, 420)) for n in range(8)]
        side_claw_fades = [Image(f"spook_dog/ghost_dog_side_claw_fade{20*(n+1)}.png", (130, 420)) for n in range(4)]
        self.side_claw_frames = side_claw_swipes + side_claw_sizes + list(reversed(side_claw_fades))

        self.duration = 0
        self.total_duration = 2 * self.game.fps

    def run(self):
        self.user.display()

        if self.duration == 0 and self.opacity < 100:
            self.opacity += 10
            self.fade_overlays[int(self.opacity/10) - 1].display()
            self.opponent.display()

        elif self.duration < self.total_duration:
            self.game.screen.fill(Color.BLACK)
            if self.duration == self.total_duration//2:
                self.play_sound()
            if self.duration > self.total_duration//2:
                stage = self.duration - self.total_duration//2 - 1
                if 0 <= stage < 5 or 10 <= stage < 15:
                    self.opponent.character_scared_redflash.display()
                else:
                    self.opponent.character_scared.display()
                if stage < 17:
                    self.top_claw_frames[stage].display()
                if 10 <= stage < 27:
                    self.side_claw_frames[stage - 10].display()
            else:
                self.opponent.character_scared.display()
            self.duration += 1
            if self.duration == self.total_duration:
                self.deal_damage()

        elif self.opacity > 0:
            self.fade_overlays[int(self.opacity/10) - 1].display()
            self.opponent.character_scared.display()
            self.opacity -= 10
        else:
            self.opponent.character_scared.display()
            self.duration = 0
            self.opponent.next_move()
