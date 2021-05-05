## SNAKE BATTLE - START

# Default battle screen, where the player chooses which move to use
if current == "choose ability":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_normal, (930,440))

    if mousein(960,430,1100,540):
        screen.blit(kick_move_icon_faded, (960,390))
        screen.blit(headbutt_move_icon_faded, (1010,390))
        screen.blit(frostbeam_move_icon_faded, (1060,390))

        if left and not self.game.options.is_showing:
            current = "aggressive moves"
    elif mousein(135,380,235,520):
        screen.blit(heal_move_icon_faded, (165,330))

        if left and not self.game.options.is_showing:
            current = "defensive moves"

# Screen showing the player their aggressive move options
elif current == "aggressive moves":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_normal, (930,440))
    
    screen.blit(kick_move_icon_solid, (960,390))
    screen.blit(headbutt_move_icon_solid, (1010,390))
    screen.blit(frostbeam_move_icon_solid, (1060,390))

    if mousein(960,390,1000,430):
        screen.blit(kick_move_info, (930,130))
    elif mousein(1010,390,1050,430):
        screen.blit(headbutt_move_info, (930,130))
    elif mousein(1060,390,1100,430):
        screen.blit(frostbeam_move_info, (930,130))
    
    if left and not self.game.options.is_showing:
        if mousein(960,390,1000,430):
            character_current_mana += 10
            if character_current_mana > character_max_mana:
                character_current_mana = character_max_mana
            display_mana_notification_time = 2*fps
            current = "kick move"
        elif mousein(1010,390,1050,430):
            if character_current_mana >= 20:
                character_current_mana -= 20
                display_mana_notification_time = 2*fps
                current = "headbutt move"
            else:
                display_mana_notification_time = 0
        elif mousein(1060,390,1100,430):
            if character_current_mana >= 30:
                character_current_mana -= 30
                display_mana_notification_time = 2*fps
                current = "frostbeam move"
            else:
                display_mana_notification_time = 0
        elif not mousein(930,380,1130,540):
            current = "choose ability"
            
# Screen showing the player their defensive move options
elif current == "defensive moves":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_normal, (930,440))
    
    screen.blit(heal_move_icon_solid, (165,330))

    if mousein(165,330,205,370):
        screen.blit(heal_move_info, (220,130))

    if left and not self.game.options.is_showing:
        if mousein(165,330,205,370):
            if character_current_mana >= 10:
                character_current_mana -= 10
                display_mana_notification_time = 2*fps
                current = "heal move"
            else:
                display_mana_notification_time = 0
        elif not mousein(150,320,220,560):
            current = "choose ability"

# Not enough mana screen - displays text telling the player that they do not have enough mana to use the move they tried to use
elif current == "snake_not_enough_mana":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_normal, (930,440))

    if duration_time < 2*fps:
        screen.blit(not_enough_mana, (300,200))
        duration_time += 1
    else:
        current = "choose ability"
        duration_time = 0

# Snake dead/Victory screen
elif current == "snake dead":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_dead, (930,440))
    screen.blit(victory_overlay, (0,0))
    screen.blit(continue_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not self.game.options.is_showing:
        if mousein(1000,600,1120,650):
            current = "choose ability"
            opponent_name = "Spook Dog"
            character_level += 1
            character_max_hp = 90 + 10*int(character_level)
            character_current_hp = 90 + 10*int(character_level)
            character_max_mana = 95 + 5*int(character_level)
            character_current_mana = 95 + 5*int(character_level)
            enemy_max_hp = 200
            enemy_current_hp = 200
            enemy_max_mana = 150
            enemy_current_mana = 150
            savegame(save_number)
        elif mousein(80,600,268,650):
            character_level += 1
            opponent_name = "Spook Dog"
            savegame(save_number)
            current = "title"
        
# Character dead/Defeat screen
elif current == "character dead":
    screen.blit(character_dead, (150,480))
    screen.blit(snake_normal, (930,440))
    screen.blit(defeat_overlay, (0,0))
    screen.blit(try_again_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not self.game.options.is_showing:
        if mousein(1000,600,1200,700):
            current = "choose ability"
            character_level += 0.25
            character_max_hp = 90 + 10*int(character_level)
            character_current_hp = 90 + 10*int(character_level)
            character_max_mana = 95 + 5*int(character_level)
            character_current_mana = 95 + 5*int(character_level)
            enemy_max_hp = 120
            enemy_current_hp = 120
            enemy_max_mana = 120
            enemy_current_mana = 120
            savegame(save_number)
        elif mousein(80,600,268,650):
            savegame(save_number)
            current = "title"

# Character heal move animation
elif current == "heal move":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_normal, (930,440))

    if heal_heart_y < 350:
        if heal_heart_y == 170:
            heal_move_sound()
        screen.blit(heal_heart, (160,heal_heart_y))
        heal_heart_y += 5

    else:
        if not healed_already:
            healed_by = random.randint(5,15)
            if character_current_hp + healed_by > character_max_hp:
                healed_by = character_max_hp - character_current_hp
            character_current_hp += healed_by
            display_healed = font.render("+" + str(healed_by), True, HEAL_GREEN)
            healed_already = True

        if duration_time < fps/2:
            screen.blit(display_healed, (170, display_healed_y))
            duration_time += 1
            display_healed_y -= 3
        else:
            # Resetting variables for next time
            heal_heart_y = 170
            display_healed_y = 360
            duration_time = 0
            healed_already = False
            snake_next_move = choose_snake_move()
            enemy_current_mana = snake_change_mana(enemy_current_mana,snake_next_move)
            current = snake_next_move

# Character kick move animation
elif current == "kick move":
    screen.blit(snake_normal, (930,440))
    
    if advancing:
        if character_kick_x == 150:
            character_stage = idle_movement(character_stage,character,20,150,380)
            character_kick_x += 24
        elif character_kick_x < 870:
            if character_tilt_direction == "left":
                screen.blit(character_tilt_left, (character_kick_x,380))
                character_tilt_direction = "right"
            elif character_tilt_direction == "right":
                screen.blit(character_tilt_right, (character_kick_x,380))
                character_tilt_direction =  "left"
            character_kick_x += 24
            if character_kick_x == 750:
                character_attack_sound()
                
        elif character_kick_x == 870:
            screen.blit(character_tilt_left, (870,380))
            kick_damage = random.randint(8,12)
            if enemy_current_hp - kick_damage < 0:
                kick_damage = enemy_current_hp
            enemy_current_hp -= kick_damage                        
            display_damage = font.render("-" + str(kick_damage), True, DAMAGE_RED)
            display_damage_time = 0
            character_kick_x -= 36
            advancing = False
            
    elif not advancing:
        if character_kick_x > 150:
            character_stage = idle_movement(character_stage,character,20,character_kick_x,380)
            character_kick_x -= 36
        else:
            # Resetting variables for next time
            advancing = True
            character_kick_x = 150
            character_tilt_direction = "left"
            display_damage_y = 420
            if enemy_current_hp == 0:
                current = "snake dead"
            else:
                snake_next_move = choose_snake_move()
                enemy_current_mana = snake_change_mana(enemy_current_mana,snake_next_move)
                current = snake_next_move

    if display_damage_time < fps/2:     # Make this into a function in the future? if more battles are made (also for the heal one)
        screen.blit(display_damage, (1015,display_damage_y))
        display_damage_time += 1
        display_damage_y -= 3
    else:
        display_damage_time = fps

# Character headbutt move animation
elif current == "headbutt move":
    screen.blit(snake_normal, (930,440))
    
    if advancing:
        if character_headbutt_x == 150:
            character_stage = idle_movement(character_stage,character,20,150,380)
            character_headbutt_x += 24
        elif character_headbutt_x < 870:
            screen.blit(character_headbutt_stance, (character_headbutt_x,380))
            character_headbutt_x += 24
            if character_headbutt_x == 750:
                character_attack_sound()
                
        elif character_headbutt_x == 870:
            screen.blit(character_headbutt_stance, (870,380))
            headbutt_damage = random.randint(10,20)
            if enemy_current_hp - headbutt_damage < 0:
                headbutt_damage = enemy_current_hp
            enemy_current_hp -= headbutt_damage                        
            display_damage = font.render("-" + str(headbutt_damage), True, DAMAGE_RED)
            display_damage_time = 0
            character_headbutt_x -= 36
            advancing = False
            
    elif not advancing:
        if character_headbutt_x > 150:
            character_stage = idle_movement(character_stage,character,20,character_headbutt_x,380)
            character_headbutt_x -= 36                        
        else:
            # Resetting variables for next time
            advancing = True
            character_headbutt_x = 150
            character_tilt_direction = "left"
            display_damage_y = 420
            if enemy_current_hp == 0:
                current = "snake dead"
            else:
                snake_next_move = choose_snake_move()
                enemy_current_mana = snake_change_mana(enemy_current_mana,snake_next_move)
                current = snake_next_move

    if display_damage_time < fps/2:
        screen.blit(display_damage, (1015,display_damage_y))
        display_damage_time += 1
        display_damage_y -= 3
    else:
        display_damage_time = fps
        
# Character frostbeam move animation
elif current == "frostbeam move":
    screen.blit(snake_normal, (930,440))
    screen.blit(character_frostbeam_stance, (150,380))

    if duration_time < 2*fps:
        if duration_time == 0:
            frostbeam_move_sound()
        elif duration_time == fps:
            frostbeam_damage = random.randint(15,30)
            if enemy_current_hp - frostbeam_damage < 0:
                frostbeam_damage = enemy_current_hp
            enemy_current_hp -= frostbeam_damage                        
            display_damage = font.render("-" + str(frostbeam_damage), True, DAMAGE_RED)
            display_damage_time = 0
            
        screen.blit(frostbeam_start, (215,381))
        screen.blit(frostbeam_middle, (265,383))
        screen.blit(frostbeam_middle, (315,385))
        screen.blit(frostbeam_middle, (365,387))
        screen.blit(frostbeam_middle, (415,389))
        screen.blit(frostbeam_middle, (465,391))
        screen.blit(frostbeam_middle, (515,393))
        screen.blit(frostbeam_middle, (565,395))
        screen.blit(frostbeam_middle, (615,397))
        screen.blit(frostbeam_middle, (665,399))
        screen.blit(frostbeam_middle, (715,401))
        screen.blit(frostbeam_middle, (765,403))
        screen.blit(frostbeam_middle, (815,405))
        screen.blit(frostbeam_middle, (865,407))
        screen.blit(frostbeam_middle, (915,409))
        screen.blit(frostbeam_middle, (965,411))
        screen.blit(snake_normal, (930,440))
        duration_time += 1
    
    else:
        # Resetting variables for next time
        display_damage_time = fps
        duration_time = 0
        if enemy_current_hp == 0:
                current = "snake dead"
        else:
            snake_next_move = choose_snake_move()
            enemy_current_mana = snake_change_mana(enemy_current_mana,snake_next_move)
            current = snake_next_move

    if display_damage_time < fps/2:
        screen.blit(display_damage, (1015,display_damage_y))
        display_damage_time += 1
        display_damage_y -= 3

## Snake moves
        
# Snake heal move animation
elif current == "snake heal move":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(snake_normal, (930,440))

    if enemy_heal_y < 410:
        if enemy_heal_y == 230:
            heal_move_sound()
        screen.blit(heal_heart, (1005,enemy_heal_y))
        enemy_heal_y += 5

    else:
        if not healed_already:
            healed_by = random.randint(5,15)
            if enemy_current_hp + healed_by > enemy_max_hp:
                healed_by = enemy_max_hp - enemy_current_hp
            enemy_current_hp += healed_by
            display_healed = font.render("+" + str(healed_by), True, HEAL_GREEN)
            healed_already = True

        if duration_time < fps/2:
            screen.blit(display_healed, (1015, display_healed_y))
            duration_time += 1
            display_healed_y -= 3
        else:
            # Resetting variables for next time
            enemy_heal_y = 170
            display_healed_y = 360
            duration_time = 0
            healed_already = False
            current = "choose ability"

# Snake laser move animation
elif current == "snake laser move":
    screen.blit(snake_laser_stance, (930,440))
    character_stage = idle_movement(character_stage,character,20,150,380)

    if duration_time < 2*fps:
        if duration_time == 0:
            laser_move_sound()
        elif duration_time == fps:
            laser_damage = random.randint(10,40)
            if character_current_hp - laser_damage < 0:
                laser_damage = character_current_hp
            character_current_hp -= laser_damage                        
            display_damage = font.render("-" + str(laser_damage), True, DAMAGE_RED)
            display_damage_time = 0
            
        screen.blit(snake_laser_beam, (730,440))
        screen.blit(snake_laser_beam, (530,440))
        screen.blit(snake_laser_beam, (330,440))
        screen.blit(snake_laser_beam, (180,440))
        screen.blit(character_normal, (150,380))
        duration_time += 1
    
    else:
        # Resetting variables for next time
        display_damage_time = fps
        duration_time = 0
        if character_current_hp == 0:
            current = "character dead"
        else:
            current = "choose ability"

    if display_damage_time < fps/2:
        screen.blit(display_damage, (170,character_display_damage_y))
        display_damage_time += 1
        character_display_damage_y -= 3

# SNAKE BATTLE - END
