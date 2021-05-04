import pygame


class Audio:
    def __init__(self, file_name, volume_multiplier=1.0):
        self.path = f"../audio/{file_name}"
        self.sound = pygame.mixer.Sound(self.path)
        self.volume_multiplier = volume_multiplier  # Used for adjusting tracks that are naturally too loud/quiet

    def play(self, channel, *, loop):
        channel.play(self.sound, -1 if loop else 0)


class Music:
    def __init__(self, game):
        self.game = game
        self._volume = 100
        self.is_muted = False
        self.current_music = None
        self.current_sound = None

        self.music_channel = pygame.mixer.Channel(0)
        self.sound_channel = pygame.mixer.Channel(1)    # Can add more if multiple sounds need to play simultaneously

    def play_music(self, audio: Audio):
        self.stop_music()
        audio.play(self.music_channel, loop=True)
        self.current_music = audio
        if not self.is_muted:
            self.set_unmuted_pygame_volume()

    def play_sound(self, audio: Audio):
        audio.play(self.sound_channel, loop=False)
        self.current_sound = audio
        if not self.is_muted:
            self.set_unmuted_pygame_volume()

    def stop_music(self):
        self.music_channel.stop()
        self.current_music = None

    def stop_sounds(self):
        self.sound_channel.stop()
        self.current_sound = None

    def pause_music(self):
        self.music_channel.pause()

    def unpause_music(self):
        self.music_channel.unpause()

    def pause_sounds(self):
        self.sound_channel.pause()

    def unpause_sounds(self):
        self.sound_channel.unpause()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self.set_unmuted_pygame_volume()

    @staticmethod
    def pygame_volume(volume):
        """Converts the given volume to one that can be fed to pygame.mixer's set_volume() method."""
        volume *= 0.01  # Adjusting from percentage
        if 0.0005 < volume < 0.0078125:
            volume = 0.0078125  # pygame's min volume. This stops it going silent when volume is low but not muted.
        return volume

    def set_unmuted_pygame_volume(self):
        self.is_muted = False
        music_volume = self.volume
        if self.current_music is not None:
            music_volume *= self.current_music.volume_multiplier
        self.music_channel.set_volume(self.pygame_volume(music_volume))
        sound_volume = self.volume
        if self.current_sound is not None:
            sound_volume *= self.current_sound.volume_multiplier
        self.sound_channel.set_volume(self.pygame_volume(sound_volume))

    def mute(self):
        self.music_channel.set_volume(0)
        self.sound_channel.set_volume(0)
        self.is_muted = True

    def unmute(self):
        self.set_unmuted_pygame_volume()

    def toggle_mute(self):
        """Enables mute if it's off, disables it if it's on."""
        if self.is_muted:
            self.unmute()
        else:
            self.mute()
