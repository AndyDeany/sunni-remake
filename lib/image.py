import pygame


class Surface:

    default_screen = None

    @classmethod
    def initialise(cls, game):
        cls.default_screen = game.screen

    def __init__(self, default_coords: tuple):
        self.default_x, self.default_y = default_coords
        self.image = None

    def display(self, x=None, y=None, *, screen=None):
        x = x if x is not None else self.default_x
        y = y if y is not None else self.default_y
        screen = screen or self.default_screen
        screen.blit(self.image, (x, y))


class Image(Surface):
    def __init__(self, path, default_coords: tuple = (None, None), *, convert_alpha=True):
        super().__init__(default_coords)
        self.image = pygame.image.load("../images/" + path)
        if convert_alpha:
            self.image = self.image.convert_alpha()


class Text(Surface):
    def __init__(self, text, font, color, default_coords: tuple = (None, None), *, antialias=True):
        super().__init__(default_coords)
        self.image = font.render(text, antialias, color)
