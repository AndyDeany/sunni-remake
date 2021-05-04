import pygame

from lib.image import Image, Text
from lib.color import Color
from lib.font import Font


class Options:

    @classmethod
    def initialise(cls):
        cls.RETURN_TO_GAME_BUTTON = Image("sunni_return_to_game_button.png")
        cls.RETURN_TO_TITLE_BUTTON = Image("sunni_return_to_title_button.png")

        cls.VOLUME_MINUS_BUTTON = Image("sunni_volume_minus_button.png")
        cls.VOLUME_PLUS_BUTTON = Image("sunni_volume_plus_button.png")
        cls.VOLUME_MUTE_BUTTON = Image("sunni_volume_mute_button.png")

        cls.WINDOWED_BUTTON = Image("sunni_windowed_button.png")
        cls.FULLSCREEN_BUTTON = Image("sunni_fullscreen_button.png")

        cls.BLANK_OVERLAY = Image("sunni_blank_overlay.png")

    def __init__(self, game):
        self.game = game
        self.just_selected = False
        self.is_showing = False

        self.fullscreen_enabled = False
        self.window_size = (1280, 720)

        self.frozen_game = None

    def show(self):
        self.just_selected = True
        self.is_showing = True
        self.game.music.pause()

    def hide(self):
        self.is_showing = False
        self.game.music.unpause()

    def display(self):
        if self.just_selected:
            self.just_selected = False
            self.frozen_game = pygame.display.get_surface().copy()
            return
        self.game.screen.blit(self.frozen_game, (0, 0))

        self.VOLUME_MINUS_BUTTON.display(430, 250)
        self.VOLUME_PLUS_BUTTON.display(490, 250)
        self.VOLUME_MUTE_BUTTON.display(570, 250)
        self.WINDOWED_BUTTON.display(80, 350)
        self.FULLSCREEN_BUTTON.display(250, 350)
        self.BLANK_OVERLAY.display(0, 0)  # Fade out the above buttons and the actual game behind the options

        self.RETURN_TO_GAME_BUTTON.display(10, 665)
        if self.game.keys.escape or (self.game.mouse.left and self.game.mouse.is_in(10, 665, 204, 715)):
            self.hide()

        if self.game.current not in ("choose character", "title"):
            self.RETURN_TO_TITLE_BUTTON.display(1082, 665)
            if self.game.mouse.left and self.game.mouse.is_in(1082, 665, 1270, 715):
                self.game.save()  # TODO: Ask the player which save file they want to use?
                self.game.current = "title"
                self.game.music.play_music(self.game.TITLE_SCREEN_MUSIC)
                self.hide()

        # Showing the buttons as solid only if they can be clicked
        Text(f"Volume Level: {self.game.music.volume}%", Font.OPENING, Color.MILD_BLUE).display(80, 250)
        if self.game.music.volume > 0:
            self.VOLUME_MINUS_BUTTON.display(430, 250)
            if self.game.mouse.left_held and self.game.mouse.is_in(430, 250, 480, 300):
                self.game.music.volume -= 1
        if self.game.music.volume < 100:
            self.VOLUME_PLUS_BUTTON.display(490, 250)
            if self.game.mouse.left_held and self.game.mouse.is_in(490, 250, 540, 300):
                self.game.music.volume += 1
        if self.game.music.is_muted:
            self.VOLUME_MUTE_BUTTON.display(570, 250)
        if self.game.mouse.left and self.game.mouse.is_in(570, 250, 620, 300):
            self.game.music.toggle_mute()

        if not self.fullscreen_enabled:
            self.WINDOWED_BUTTON.display(80, 350)
            if self.game.mouse.left and self.game.mouse.is_in(250, 350, 390, 400):
                pygame.display.toggle_fullscreen()
                self.fullscreen_enabled = True
        else:
            self.FULLSCREEN_BUTTON.display(250, 350)
            if self.game.mouse.left and self.game.mouse.is_in(80, 350, 220, 400):
                pygame.display.toggle_fullscreen()
                self.fullscreen_enabled = False
