import pygame


class Music:
    def __init__(self, game):
        self.game = game

    def play_music(self, audio):
        self.stop()
        self.play(audio, loop=True)

    def play_sound(self, audio):
        self.play(audio, loop=False)

    def play(self, audio, *, loop):
        audio.__play__(self.game.volume_multiplier, loop=loop)

    @staticmethod
    def stop():
        pygame.mixer.music.stop()


class Audio:
    def __init__(self, file_name, volume=1.0):
        self.path = f"../audio/{file_name}"
        self.volume = volume

    def __play__(self, volume_multiplier, *, loop):
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.set_volume(self.volume * volume_multiplier)
        pygame.mixer.music.play(-1 if loop else 0)
