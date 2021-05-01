import pygame

from lib.sunni_keydown import Keys
from lib.sunni_core_functions import mousein


BLACK = (0, 0, 0)
MANA_BLUE = (36, 91, 255)
HEALTH_RED = (235, 0, 0)
EMPTY_BLUE = (0, 20, 79)
EMPTY_RED = (117, 0, 0)


def default_battle_display(battle_background_hallway, health_icon, mana_icon, options_button, game):
    # Background
    battle_background_hallway.display(0, 0)
    # Assigning variables which contain the positions the ends of the health and mana bars
    character_health_end_pos = ((200/float(game.player.max_hp))*game.player.current_hp)
    character_mana_end_pos = ((200/float(game.player.max_mana))*game.player.current_mana)
    dog_health_end_pos = ((200/float(game.opponent.max_hp))*game.opponent.current_hp)
    dog_mana_end_pos = ((200/float(game.opponent.max_mana))*game.opponent.current_mana)
    # Character health and mana bars
    pygame.draw.rect(game.screen, HEALTH_RED, [10,30,character_health_end_pos,30])
    pygame.draw.rect(game.screen, EMPTY_RED, [10+character_health_end_pos,30,200-character_health_end_pos,30])
    pygame.draw.rect(game.screen, MANA_BLUE, [10,60,character_mana_end_pos,30])
    pygame.draw.rect(game.screen, EMPTY_BLUE, [10+character_mana_end_pos,60,200-character_mana_end_pos,30])
    # Dog health and mana bars
    pygame.draw.rect(game.screen, HEALTH_RED, [1070,30,dog_health_end_pos,30])
    pygame.draw.rect(game.screen, EMPTY_RED, [1070+dog_health_end_pos,30,200-dog_health_end_pos,30])
    pygame.draw.rect(game.screen, MANA_BLUE, [1070,60,dog_mana_end_pos,30])
    pygame.draw.rect(game.screen, EMPTY_BLUE, [1070+dog_mana_end_pos,60,200-dog_mana_end_pos,30])
    # Health and mana bar borders
    pygame.draw.rect(game.screen, BLACK, [10,30,200,30], 1)
    pygame.draw.rect(game.screen, BLACK, [10,60,200,30], 1)
    pygame.draw.rect(game.screen, BLACK, [1070,30,200,30], 1)
    pygame.draw.rect(game.screen, BLACK, [1070,60,200,30], 1)
    # Health and mana icons
    health_icon.display(210, 20)
    mana_icon.display(210, 50)
    health_icon.display(1020, 20)
    mana_icon.display(1020, 50)

    game.player.current_hp_display.display(15, 32)
    game.player.current_mana_display.display(15, 62)
    game.opponent.current_hp_display.display(1075, 32)
    game.opponent.current_mana_display.display(1075, 62)
    game.player.name_display.display(15, 2)
    game.opponent.name_display.display(1075, 2)

    # Options button
    options_button.display(10, 665)
    if (Keys.escape or (game.mouse.is_in(10, 665, 100, 715) and game.mouse.left == 1))\
            and not game.display_options and game.current != "choose_character":   # Focus on choosing your character!
        game.display_options = True
        game.options_just_selected = True
