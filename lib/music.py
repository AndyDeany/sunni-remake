from multiprocessing.dummy import Pool

import pygame


def pygame_volume(volume):
    """Converts the given volume to one that can be fed to pygame.mixer's set_volume() method."""
    volume *= 0.01  # Adjusting from percentage
    if 0.0005 < volume < 0.0078125:
        volume = 0.0078125  # pygame's min volume. This stops it going silent when volume is low but not muted.
    return volume


class Audio:
    """Class for representing and containing an audio clip."""
    def __init__(self, file_name, volume_multiplier=1.0, *, load_async=True):
        self.path = f"../audio/{file_name}"
        if load_async:
            self.sound_pool = Pool(processes=1).apply_async(pygame.mixer.Sound, [self.path])
            self._sound = None
        else:
            self._sound = pygame.mixer.Sound(self.path)
        self.volume_multiplier = volume_multiplier  # Used for adjusting tracks that are naturally too loud/quiet

    @property
    def sound(self):
        if self._sound is None:
            self._sound = self.sound_pool.get(10)
        return self._sound

    @property
    def is_loaded(self):
        return self.sound_pool.ready()

    def play(self, channel, *, loop: bool, fade: bool):
        """Play the audio clip. Loops indefinitely if loop is True. Fades in if fade is True."""
        channel.play(self.sound, -1 if loop else 0, fade_ms=1000 if fade else 0)

    def set_volume(self, volume):
        """Set the volume of the audio clip."""
        volume = pygame_volume(volume)
        self.sound.set_volume(volume * self.volume_multiplier)


class Music:
    """Class for controlling audio playback in the game."""
    def __init__(self, game):
        self.game = game
        self._volume = 100
        self.is_muted = False
        self.current_music = None
        self.current_sound = None

        self.music_channel = pygame.mixer.Channel(0)
        self.sound_channel = pygame.mixer.Channel(1)    # Can add more if multiple sounds need to play simultaneously

    def play_music(self, audio: Audio):
        """Play the given song on loop. Mainly for BGM purposes."""
        self.stop_music()
        if not self.is_muted:
            audio.set_volume(self.volume)
        audio.play(self.music_channel, loop=True, fade=True)
        self.current_music = audio

    def play_sound(self, audio: Audio):
        """Play the given sound once. Mainly for short sounds effects."""
        if not self.is_muted:
            audio.set_volume(self.volume)
        audio.play(self.sound_channel, loop=False, fade=False)
        self.current_sound = audio

    def stop_music(self):
        """Stop the currently playing music (BGM)."""
        if self.current_music is not None:
            self.current_music.sound.stop()
        self.current_music = None

    def stop_sounds(self):
        """Stop all currently playing SFX."""
        if self.current_sound is not None:
            self.current_sound.sound.stop()
        self.current_sound = None

    def pause_music(self):
        """Pause the currently playing music (BGM)."""
        self.music_channel.pause()

    def unpause_music(self):
        """Unpause the currently paused music (BGM)."""
        self.music_channel.unpause()

    def pause_sounds(self):
        """Pause the currently playing SFX."""
        self.sound_channel.pause()

    def unpause_sounds(self):
        """Unpause the currently paused SFX."""
        self.sound_channel.unpause()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self.set_unmuted_pygame_volume()

    def set_unmuted_pygame_volume(self):
        self.is_muted = False
        if self.current_music is not None:
            self.current_music.set_volume(self.volume)
        if self.current_sound is not None:
            self.current_sound.set_volume(self.volume)

    def mute(self):
        """Mute all game audio."""
        self.is_muted = True
        if self.current_music is not None:
            self.current_music.sound.set_volume(0)
        if self.current_sound is not None:
            self.current_sound.sound.set_volume(0)

    def unmute(self):
        """Unmute all game audio (if it was muted)."""
        self.set_unmuted_pygame_volume()

    def toggle_mute(self):
        """Enables mute if it's off, disables it if it's on."""
        if self.is_muted:
            self.unmute()
        else:
            self.mute()
