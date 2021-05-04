import pygame


def set_pygame_volume(volume):
    """Sets the pygame.mixer.music volume without letting it go to 0 unless it actually should be."""
    volume *= 0.01  # Adjusting from percentage
    if 0.0005 < volume < 0.0078125:
        print("hi")
        volume = 0.0078125
    pygame.mixer.music.set_volume(volume)


class Audio:
    def __init__(self, file_name, volume_multiplier=1.0):
        self.path = f"../audio/{file_name}"
        self.volume_multiplier = volume_multiplier  # Used for adjusting tracks that are naturally too loud/quiet

    def __play__(self, volume, *, loop):
        pygame.mixer.music.load(self.path)
        set_pygame_volume(volume * self.volume_multiplier)
        pygame.mixer.music.play(-1 if loop else 0)


class Music:
    def __init__(self, game):
        self.game = game
        self._volume = 100
        self.is_muted = False
        self.currently_playing = None

    def play_music(self, audio: Audio):
        self.stop()
        self.play(audio, loop=True)
        self.currently_playing = audio

    def play_sound(self, audio: Audio):
        self.play(audio, loop=False)

    def play(self, audio: Audio, *, loop: bool):
        audio.__play__(self.volume, loop=loop)

    @staticmethod
    def stop():
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self.set_unmuted_pygame_volume()

    def set_unmuted_pygame_volume(self):
        self.is_muted = False
        volume = self.volume
        if self.currently_playing is not None:
            volume *= self.currently_playing.volume_multiplier
        set_pygame_volume(volume)

    def mute(self):
        pygame.mixer.music.set_volume(0)
        self.is_muted = True

    def unmute(self):
        self.set_unmuted_pygame_volume()

    def toggle_mute(self):
        """Enables mute if it's off, disables it if it's on."""
        if self.is_muted:
            self.unmute()
        else:
            self.mute()
