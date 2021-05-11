import pygame

from lib.image import Image
from lib.pages.main_menu import MainMenu


class Options:
    """Class for representing the options menu in the game (and storing the game's options)."""

    def __init__(self, session, window_size):
        self.session = session
        self.is_showing = False
        self.frozen_game = None

        self.fullscreen_enabled = False
        self.window_size = window_size

        self._return_to_game_button = Image("return_to_game_button.png", (11, 667))
        self._volume_minus_button = Image("volume_minus_button.png", (430, 250))
        self._volume_plus_button = Image("volume_plus_button.png", (490, 250))
        self._volume_mute_button = Image("volume_mute_button.png", (570, 250))
        self._windowed_button = Image("windowed_button.png", (84, 352))
        self._fullscreen_button = Image("fullscreen_button.png", (250, 352))
        self._blank_overlay = Image("blank_overlay.png", (0, 0))

    def show(self):
        """Show the options menu."""
        self.frozen_game = pygame.display.get_surface().copy()
        self.is_showing = True
        self.session.music.pause_sounds()

    def hide(self):
        """Hide the options menu."""
        self.is_showing = False
        self.session.music.unpause_sounds()

    def display(self):
        """Run the code for displaying the options menu on the screen."""
        self.session.screen.blit(self.frozen_game, (0, 0))

        self._volume_minus_button.display()
        self._volume_plus_button.display()
        self._volume_mute_button.display()
        self._windowed_button.display()
        self._fullscreen_button.display()
        self._blank_overlay.display()   # Fade out the above buttons and the actual game behind the options

        self._return_to_game_button.display()
        if self.session.keys.escape or (self.session.mouse.left and self.session.mouse.is_in(10, 665, 204, 715)):
            self.hide()

        if not isinstance(self.session.game.page, MainMenu):
            self.session.game.return_to_title_button.display()
            if self.session.game.return_to_title_button.is_clicked:
                if self.session.game.selected_save is not None:
                    self.session.game.save()
                self.session.game.return_to_title_button.on_click()
                self.hide()

        self._run_volume_change_logic()
        self._run_change_window_logic()

    def _run_volume_change_logic(self):
        """Run the logic allowing the player to change the volume (and showing those changes to them)."""
        self.session.music.volume_text.display(80, 250)
        if self.session.music.volume > 0:
            self._volume_minus_button.display()
            if self.session.mouse.left.is_pressed and self.session.mouse.is_in(430, 250, 480, 300):
                self.session.music.volume -= 1
        if self.session.music.volume < 100:
            self._volume_plus_button.display()
            if self.session.mouse.left.is_pressed and self.session.mouse.is_in(490, 250, 540, 300):
                self.session.music.volume += 1
        if self.session.music.is_muted:
            self._volume_mute_button.display()
        if self.session.mouse.left and self.session.mouse.is_in(570, 250, 620, 300):
            self.session.music.toggle_mute()

    def _run_change_window_logic(self):
        """Run the logic allowing the player to change the window between windowed and fullscreen."""
        if not self.fullscreen_enabled:
            self._windowed_button.display()
            if self.session.mouse.left and self.session.mouse.is_in(250, 350, 390, 400):
                self.toggle_fullscreen()
                self.fullscreen_enabled = True
        else:
            self._fullscreen_button.display()
            if self.session.mouse.left and self.session.mouse.is_in(80, 350, 220, 400):
                self.toggle_fullscreen()
                self.fullscreen_enabled = False

    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        pygame.display.toggle_fullscreen()
        pygame.mouse.set_pos((self.session.mouse.x, self.session.mouse.y))  # Put the mouse where it was
