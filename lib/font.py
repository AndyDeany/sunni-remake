import pygame


pygame.init()


class Font:     # pylint: disable=too-few-public-methods
    """Class for storing the different fonts used by the game so that they can be accessed everywhere."""

    TITLE = pygame.font.SysFont("Arial Black", 40, False, False)
    OPENING = pygame.font.SysFont("Arial Black", 30, False, False)
    DEFAULT = pygame.font.SysFont("Impact", 20, False, False)
    SUNNI = pygame.font.SysFont("Candara", 40, False, False)

    MOVE_INFO_BIG = pygame.font.SysFont("Franklin Gothic", 30, False, False)
    MOVE_INFO_SMALL = pygame.font.SysFont("Franklin Gothic", 24, False, False)
