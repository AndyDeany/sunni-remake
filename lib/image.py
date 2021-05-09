import pygame

from lib.color import Color


class Surface:

    default_screen = None

    @classmethod
    def initialise(cls, session):
        cls.default_screen = session.screen

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
    """Class for representing a generated text image."""
    def __init__(self, text, font, color, default_coords: tuple = (None, None), *,
                 antialias=True, with_outline=False, outline_color=Color.BLACK):
        super().__init__(default_coords)
        self.image = font.render(text, antialias, color)
        self.is_outlined = with_outline
        if self.is_outlined:
            outline_text = font.render(text, antialias, outline_color)
            width, height = self.image.get_size()
            outlined_image = pygame.Surface((width + 2, height + 2)).convert_alpha()
            pygame.draw.rect(outlined_image, (0, 0, 0, 0), [0, 0, width + 2, height + 2])
            outlined_image.blit(outline_text, (0, 0))
            outlined_image.blit(outline_text, (0, 2))
            outlined_image.blit(outline_text, (2, 0))
            outlined_image.blit(outline_text, (2, 2))
            outlined_image.blit(self.image, (1, 1))
            self.image = outlined_image
            if self.default_x is not None:
                self.default_x -= 1
            if self.default_y is not None:
                self.default_y -= 1

    def display(self, x=None, y=None, *, screen=None):
        if self.is_outlined:
            if x is not None:
                x -= 1
            if y is not None:
                y -= 1
        super().display(x, y, screen=screen)
