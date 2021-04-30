import pygame

from lib.sunni_keydown import Keys
from lib.sunni_core_functions import mousein


BLACK = (0, 0, 0)
MANA_BLUE = (36, 91, 255)
HEALTH_RED = (235, 0, 0)
EMPTY_BLUE = (0, 20, 79)
EMPTY_RED = (117, 0, 0)


def default_battle_display(font, battle_background_hallway, health_icon, mana_icon, options_button, left, mouse_x, mouse_y, game):
    # Background
    game.screen.blit(battle_background_hallway, (0,0))
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
    game.screen.blit(health_icon, (210, 20))
    game.screen.blit(mana_icon, (210, 50))
    game.screen.blit(health_icon, (1020, 20))
    game.screen.blit(mana_icon, (1020, 50))

    # Health and mana number display. Should do these on set with a @property method instead on the Character class.
    game.player.current_hp_display = font.render("Health: " + str(game.player.current_hp) + "/" + str(game.player.max_hp), True, BLACK)
    game.player.current_mana_display = font.render("Mana: " + str(game.player.current_mana) + "/" + str(game.player.max_mana), True, BLACK)
    game.opponent.current_hp_display = font.render("Health: " + str(game.opponent.current_hp) + "/" + str(game.opponent.max_hp), True, BLACK)
    game.opponent.current_mana_display = font.render("Mana: " + str(game.opponent.current_mana) + "/" + str(game.opponent.max_mana), True, BLACK)
    game.screen.blit(game.player.current_hp_display, (15,32))
    game.screen.blit(game.player.current_mana_display, (15,62))
    game.screen.blit(game.opponent.current_hp_display, (1075,32))
    game.screen.blit(game.opponent.current_mana_display, (1075,62))
    # Character name display. Same with these and a @property method.
    game.player.name_display = font.render(game.player.name, True, BLACK)
    game.opponent.name_display = font.render(game.opponent.name, True, BLACK)
    game.screen.blit(game.player.name_display, (15, 2))
    game.screen.blit(game.opponent.name_display, (1075, 2))

    # Options button
    game.screen.blit(options_button, (10,665))
    if (Keys.escape or (mousein(mouse_x, mouse_y, 10, 665, 100, 715) and left == 1))\
            and not game.display_options and game.current != "choose_character":   # Focus on choosing your character!
        game.display_options = True
        game.options_just_selected = True
