import pygame


class Music:
    def __init__(self, game):
        self.game = game
        self.volume = 1.0

    def play_music(self, audio):
        self.stop()
        self.play(audio, loop=True)

    def play_sound(self, audio):
        self.play(audio, loop=False)

    def play(self, audio, *, loop):
        audio.__play__(self.volume, loop=loop)

    @staticmethod
    def stop():
        pygame.mixer.music.stop()


class Audio:
    def __init__(self, file_name, volume_multiplier=1.0):
        self.path = f"../audio/{file_name}"
        self.volume_multiplier = volume_multiplier  # Used for adjusting tracks that are naturally too loud/quiet

    def __play__(self, volume, *, loop):
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.set_volume(volume * self.volume_multiplier)
        pygame.mixer.music.play(-1 if loop else 0)
