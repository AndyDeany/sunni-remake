"""Module containing the player's moves."""
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
            if not line:
                raise ValueError(f"'{next_word}' is too long to fit within {max_width}px in {font}.")
            lines.append(line)
            line = ""
    lines.append(line)
    return lines


class PlayerMove(Move):     # noqa pylint: disable=abstract-method
    """Class for representing one of the player's moves."""

    INFO_WIDTH = 200
    INFO_HEIGHT = 250
    INFO_TITLE_HEIGHT = 54
    X_BUFFER = 8

    NAME = "PlayerMove"
    DESCRIPTION = "PlayerMove description."
    NAME_COLOR = Color.MOVE_NAME_RED

    def __init__(self, mana_cost, *args, **kwargs):
        super().__init__(mana_cost, *args, **kwargs)
        self.icon = None
        self.icon_faded = None
        self.info = None
        self.generate_info()

    @property
    def user(self):
        return self.game.player

    @property
    def opponent(self):
        return self.game.opponent

    @property
    def description(self):
        description = self.DESCRIPTION
        description = description.replace("{min_damage}", str(self.min_damage))
        description = description.replace("{max_damage}", str(self.max_damage))
        description = description.replace("{min_healing}", str(self.min_healing))
        description = description.replace("{max_healing}", str(self.max_healing))
        description = description.replace("{mana_damage}", str(self.mana_damage))
        description = description.replace("{mana_healing}", str(self.mana_healing))
        return description

    def generate_info(self):
        """Generate the move's info in an Image instance and put it in self.info."""
        info = pygame.Surface((self.INFO_WIDTH, self.INFO_HEIGHT)).convert_alpha()

        info_desc_height = self.INFO_HEIGHT - self.INFO_TITLE_HEIGHT
        pygame.draw.rect(info, Color.LIGHT_GREY, [0, 0, self.INFO_WIDTH, self.INFO_TITLE_HEIGHT])
        pygame.draw.rect(info, Color.DARK_GREY, [0, self.INFO_TITLE_HEIGHT, self.INFO_WIDTH, info_desc_height])
        pygame.draw.rect(info, Color.BLACK, [0, 0, self.INFO_WIDTH, self.INFO_TITLE_HEIGHT], 1)
        pygame.draw.rect(info, Color.BLACK, [0, self.INFO_TITLE_HEIGHT, self.INFO_WIDTH, info_desc_height], 1)

        name_lines = wrap_text(self.NAME, Font.MOVE_INFO_BIG, self.INFO_WIDTH - 16)
        name_height = sum((Font.MOVE_INFO_BIG.size(line)[1] for line in name_lines))
        line_height = Font.MOVE_INFO_BIG.get_linesize()
        y = (self.INFO_TITLE_HEIGHT - name_height)//2
        for index, line in enumerate(name_lines):
            text = Text(line, Font.MOVE_INFO_BIG, self.NAME_COLOR, with_outline=True)
            x = (self.INFO_WIDTH - Font.MOVE_INFO_BIG.size(line)[0]) // 2
            text.display(x, y + index*line_height, screen=info)

        mana_cost_string = f"{self.mana_cost} Mana" if self.mana_cost > 0 else "No Cost"
        mana_cost_y = self.INFO_TITLE_HEIGHT + 3
        text = Text(mana_cost_string, Font.MOVE_INFO_BIG, Color.MANA_COST_BLUE, with_outline=True)
        text.display(8, mana_cost_y, screen=info)
        description_lines = wrap_text(self.description, Font.MOVE_INFO_SMALL, self.INFO_WIDTH - 2*self.X_BUFFER)
        line_height = Font.MOVE_INFO_SMALL.get_linesize()
        x = self.X_BUFFER
        y = mana_cost_y + Font.MOVE_INFO_BIG.get_height() + 11
        for index, line in enumerate(description_lines):
            text = Text(line, Font.MOVE_INFO_SMALL, Color.DESCRIPTION_ORANGE, with_outline=True)
            text.display(x, y + index*line_height, screen=info)
        self.info = Image(info)


class Kick(PlayerMove):
    """Class for representing the player's kick move."""

    NAME = "Courageous Kick"
    DESCRIPTION = ("Sunni darts forward, kicking his opponent courageously "
                   "for {min_damage}-{max_damage} damage.\n\nRestores {mana_healing} mana.")

    START_X = 150
    SOUND_X = 750
    END_X = 870
    FORWARD_STEP = 24
    BACKWARD_STEP = 36

    def __init__(self):
        super().__init__(0, 10, 0.2, mana_healing=10)
        self.icon = Image("player/kick_move_icon_solid.png")
        self.icon_faded = Image("player/kick_move_icon_faded.png")
        self.sound = Audio("player/character_attack1.ogg")

        self.advancing = True
        self.tilted_left = True

    def run(self):
        self.opponent.display()
        if self.advancing:
            if self.user.x <= self.END_X:
                image = self.user.character_tilt_left if self.tilted_left else self.user.character_tilt_right
                self.tilted_left = not self.tilted_left
                image.display(self.user.x, self.user.y)
                self.user.x += self.FORWARD_STEP
                if self.user.x == self.SOUND_X:
                    self.play_sound()
                if self.user.x == self.END_X:
                    self.deal_damage()
                    self.user.x -= self.BACKWARD_STEP
                    self.advancing = False
        else:
            self.user.idle_animation(self.user.x, self.user.y)
            if self.user.x > self.START_X:
                self.user.x -= self.BACKWARD_STEP
            else:   # Reset variables for next time
                self.restore_mana()
                self.advancing = True
                self.opponent.next_move()


class Headbutt(PlayerMove):
    """Class for representing the player's headbutt move."""

    NAME = "Heroic Headbutt"
    DESCRIPTION = ("Sunni charges forward, heroically headbutting his opponent "
                   "for {min_damage}-{max_damage} damage.")

    START_X = 150
    SOUND_X = 750
    END_X = 870
    FORWARD_STEP = 24
    BACKWARD_STEP = 36

    def __init__(self):
        super().__init__(20, 15, 0.33)
        self.icon = Image("player/headbutt_move_icon_solid.png")
        self.icon_faded = Image("player/headbutt_move_icon_faded.png")
        self.sound = Audio("player/character_attack1.ogg")

        self.advancing = True

    def run(self):
        self.opponent.display()
        if self.advancing:
            if self.user.x < self.END_X:
                self.user.character_headbutt_stance.display(self.user.x, self.user.y)
                self.user.x += self.FORWARD_STEP
                if self.user.x == self.SOUND_X:
                    self.play_sound()
            else:
                self.deal_damage()
                self.advancing = False

        if not self.advancing:
            self.user.idle_animation(self.user.x, self.user.y)
            if self.user.x > self.START_X:
                self.user.x -= self.BACKWARD_STEP
            else:   # Reset variables for next time
                self.advancing = True
                self.opponent.next_move()


class Frostbeam(PlayerMove):
    """Class for representing the player's frostbeam move."""

    NAME = "Frostbeam"
    DESCRIPTION = ("Sunni calls upon the power of ice, summoning a beam of frozen energy and "
                   "firing it directly at his opponent, dealing {min_damage}-{max_damage} damage.")

    def __init__(self):
        super().__init__(30, 22.5, 0.33)
        self.icon = Image("player/frostbeam_move_icon_solid.png")
        self.icon_faded = Image("player/frostbeam_move_icon_faded.png")
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
                self.deal_damage()
            self.frostbeam_start.display()
            for x in range(14):
                self.frostbeam_middle.display(265+50*x, 383+2*x)
            self.duration += 1
        else:   # Resetting variables for next time
            self.duration = 0
            self.opponent.next_move()


class Heal(PlayerMove):
    """Class for representing the player's heal move."""

    NAME = "Harmonious Healing"
    DESCRIPTION = "Sunni calls forth nature's heart, healing {min_healing}-{max_healing} hit points."
    NAME_COLOR = Color.MOVE_NAME_GREEN

    def __init__(self, heart_x, start_y, end_y):
        super().__init__(10, base_healing=10, healing_variance=0.5)
        self.icon = Image("player/heal_move_icon_solid.png")
        self.icon_faded = Image("player/heal_move_icon_faded.png")
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
                self.restore_hp()
            self.delay_duration += 1
        else:
            self.delay_duration = 0
            self.heart_y = self.start_y
            self.opponent.next_move()
