"""Module containing the player's moves."""
import random
import re

import pygame

from lib.moves import Move
from lib.image import Image, Text
from lib.music import Audio
from lib.color import Color
from lib.font import Font


def wrap_text(text, font, max_width):
    lines = []
    if not text:
        return lines
    words = re.findall(r"\S+|\n", text)
    line = ""
    while words:
        next_word = words[0]
        if next_word == "\n":
            words.pop(0)
            lines.append(line)
            line = ""
            continue
        width = font.size(" ".join((line, next_word)))[0]
        if width <= max_width:
            if line:
                line += " "
            line += words.pop(0)
        else:
            lines.append(line)
            line = ""
    lines.append(line)
    return lines


class PlayerMove(Move):     # noqa pylint: disable=abstract-method
    """Class for representing one of the player's moves."""

    INFO_WIDTH = 200
    INFO_HEIGHT = 250
    INFO_TITLE_HEIGHT = 54

    MOVE_NAME = "PlayerMove"
    MOVE_DESCRIPTION = "PlayerMove description."
    MOVE_NAME_COLOR = Color.MOVE_NAME_RED

    def __init__(self, mana_cost):
        super().__init__(mana_cost)
        self.icon = None
        self.icon_faded = None
        self._info = pygame.Surface((self.INFO_WIDTH, self.INFO_HEIGHT)).convert_alpha()

        pygame.draw.rect(self._info, Color.LIGHT_GREY, [0, 0, self.INFO_WIDTH, self.INFO_TITLE_HEIGHT])
        pygame.draw.rect(self._info, Color.DARK_GREY, [0, self.INFO_TITLE_HEIGHT, self.INFO_WIDTH, self.INFO_HEIGHT - self.INFO_TITLE_HEIGHT])
        pygame.draw.rect(self._info, Color.BLACK, [0, 0, self.INFO_WIDTH, self.INFO_TITLE_HEIGHT], 1)
        pygame.draw.rect(self._info, Color.BLACK, [0, self.INFO_TITLE_HEIGHT, self.INFO_WIDTH, self.INFO_HEIGHT - self.INFO_TITLE_HEIGHT], 1)

        name_lines = wrap_text(self.MOVE_NAME, Font.MOVE_INFO_BIG, self.INFO_WIDTH - 16)
        name_height = sum((Font.MOVE_INFO_BIG.size(line)[1] for line in name_lines))
        line_height = Font.MOVE_INFO_BIG.get_height()
        y = (self.INFO_TITLE_HEIGHT - name_height)//2
        for index, line in enumerate(name_lines):
            text = Text(line, Font.MOVE_INFO_BIG, self.MOVE_NAME_COLOR, with_outline=True)
            text.display((self.INFO_WIDTH - Font.MOVE_INFO_BIG.size(line)[0])//2, y + index*line_height, screen=self._info)

        mana_cost_string = f"{self.mana_cost} Mana" if self.mana_cost > 0 else "No Cost"
        text = Text(mana_cost_string, Font.MOVE_INFO_BIG, Color.MANA_COST_BLUE, with_outline=True)
        text.display(8, self.INFO_TITLE_HEIGHT + 8, screen=self._info)

        description_lines = wrap_text(self.MOVE_DESCRIPTION, Font.MOVE_INFO_SMALL, self.INFO_WIDTH - 16)
        line_height = Font.MOVE_INFO_SMALL.get_height()
        x = 8
        y = self.INFO_TITLE_HEIGHT + 8 + Font.MOVE_INFO_BIG.get_height() + 10
        for index, line in enumerate(description_lines):
            text = Text(line, Font.MOVE_INFO_SMALL, Color.DESCRIPTION_ORANGE, with_outline=True)
            text.display(x, y + index*line_height, screen=self._info)

    @property
    def user(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent

    def display_info(self, x, y):
        self.game.screen.blit(self._info, (x, y))


class Kick(PlayerMove):
    """Class for representing the player's kick move."""

    MOVE_NAME = "Courageous Kick"
    MOVE_DESCRIPTION = "Sunni darts forward, kicking his opponent courageously for 8-12 damage.\n\nRestores 10 mana."

    def __init__(self):
        super().__init__(-10)
        self.icon = Image("player/kick_move_icon_solid.png")
        self.icon_faded = Image("player/kick_move_icon_faded.png")
        self.info = Image("player/kick_move_info.png")
        self.sound = Audio("player/character_attack1.ogg")

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
            self.user.idle_animation(self.user.x, self.user.y)
            if self.user.x > self.start_x:
                self.user.x -= self.backward_step
            else:   # Reset variables for next time
                self.advancing = True
                self.opponent.next_move()


class Headbutt(PlayerMove):
    """Class for representing the player's headbutt move."""

    MOVE_NAME = "Heroic Headbutt"
    MOVE_DESCRIPTION = "Sunni charges forward, heroically headbutting his opponent for 10-20 damage."

    def __init__(self):
        super().__init__(20)
        self.icon = Image("player/headbutt_move_icon_solid.png")
        self.icon_faded = Image("player/headbutt_move_icon_faded.png")
        self.info = Image("player/headbutt_move_info.png")
        self.sound = Audio("player/character_attack1.ogg")

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
            self.user.idle_animation(self.user.x, self.user.y)
            if self.user.x > self.start_x:
                self.user.x -= self.backward_step
            else:   # Reset variables for next time
                self.advancing = True
                self.opponent.next_move()


class Frostbeam(PlayerMove):
    """Class for representing the player's frostbeam move."""

    MOVE_NAME = "Frostbeam"
    MOVE_DESCRIPTION = ("Sunni calls upon the power of ice, summoning a beam of frozen energy and "
                        "firing it directly at his opponent, dealing 15-30 damage.")

    def __init__(self):
        super().__init__(30)
        self.icon = Image("player/frostbeam_move_icon_solid.png")
        self.icon_faded = Image("player/frostbeam_move_icon_faded.png")
        self.info = Image("player/frostbeam_move_info.png")
        self.sound = Audio("player/frostbeam_move.ogg", 0.2)

        self.frostbeam_start = Image("player/frostbeam_start.png", (215, 381))
        self.frostbeam_middle = Image("player/frostbeam_middle.png")
        self.frostbeam_end = Image("player/frostbeam_end.png")

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

    MOVE_NAME = "Harmonious Healing"
    MOVE_DESCRIPTION = "Sunni calls forth nature's heart, healing 5-15 hit points."
    MOVE_NAME_COLOR = Color.MOVE_NAME_GREEN

    def __init__(self, heart_x, start_y, end_y):
        super().__init__(10)
        self.icon = Image("player/heal_move_icon_solid.png")
        self.icon_faded = Image("player/heal_move_icon_faded.png")
        self.info = Image("player/heal_move_info.png")
        self.sound = Audio("player/heal_move.ogg", 0.1)

        self.heart = Image("player/heal_heart.png")

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
