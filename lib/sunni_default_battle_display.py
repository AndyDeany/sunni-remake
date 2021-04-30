# Background
screen.blit(battle_background_hallway, (0,0))
# Assigning variables which contain the positions the ends of the health and mana bars
character_health_end_pos = ((200/float(character_max_hp))*character_current_hp)
character_mana_end_pos = ((200/float(character_max_mana))*character_current_mana)
dog_health_end_pos = ((200/float(enemy_max_hp))*enemy_current_hp)
dog_mana_end_pos = ((200/float(enemy_max_mana))*enemy_current_mana)
# Character health and mana bars
pygame.draw.rect(screen, HEALTH_RED, [10,30,character_health_end_pos,30])   
pygame.draw.rect(screen, EMPTY_RED, [10+character_health_end_pos,30,200-character_health_end_pos,30])
pygame.draw.rect(screen, MANA_BLUE, [10,60,character_mana_end_pos,30])
pygame.draw.rect(screen, EMPTY_BLUE, [10+character_mana_end_pos,60,200-character_mana_end_pos,30])
# Dog health and mana bars
pygame.draw.rect(screen, HEALTH_RED, [1070,30,dog_health_end_pos,30])
pygame.draw.rect(screen, EMPTY_RED, [1070+dog_health_end_pos,30,200-dog_health_end_pos,30])
pygame.draw.rect(screen, MANA_BLUE, [1070,60,dog_mana_end_pos,30])
pygame.draw.rect(screen, EMPTY_BLUE, [1070+dog_mana_end_pos,60,200-dog_mana_end_pos,30])
# Health and mana bar borders   
pygame.draw.rect(screen, BLACK, [10,30,200,30], 1)
pygame.draw.rect(screen, BLACK, [10,60,200,30], 1)
pygame.draw.rect(screen, BLACK, [1070,30,200,30], 1)
pygame.draw.rect(screen, BLACK, [1070,60,200,30], 1)
# Health and mana icons
screen.blit(health_icon, (210,20))
screen.blit(mana_icon, (210,50))
screen.blit(health_icon, (1020,20))
screen.blit(mana_icon, (1020,50))
# Health and mana number display
character_current_hp_display = font.render("Health: " + str(character_current_hp) + "/" + str(character_max_hp), True, BLACK)
character_current_mana_display = font.render("Mana: " + str(character_current_mana) + "/" + str(character_max_mana), True, BLACK)
enemy_current_hp_display = font.render("Health: " + str(enemy_current_hp) + "/" + str(enemy_max_hp), True, BLACK)
enemy_current_mana_display = font.render("Mana: " + str(enemy_current_mana) + "/" + str(enemy_max_mana), True, BLACK)
screen.blit(character_current_hp_display, (15,32))
screen.blit(character_current_mana_display, (15,62))
screen.blit(enemy_current_hp_display, (1075,32))
screen.blit(enemy_current_mana_display, (1075,62))
# Character name display
character_name_display = font.render(character_name, True, BLACK)
opponent_name_display = font.render(opponent_name, True, BLACK)
screen.blit(character_name_display, (15,2))
screen.blit(opponent_name_display, (1075,2))
# Options button
screen.blit(options_button, (10,665))
if (escape or (mousein(10,665,100,715) and left == 1)) and not display_options and current != "choose_character": # Focus on choosing your character!
    display_options = True
    options_just_selected = True
