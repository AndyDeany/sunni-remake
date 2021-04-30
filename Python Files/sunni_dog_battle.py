## DOG BATTLE - START

# Default battle screen, where the player chooses which move to use
if current == "choose ability":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(dog_normal, (930,440))

    if mousein(960,430,1100,540):
        screen.blit(kick_move_icon_faded, (960,390))
        screen.blit(headbutt_move_icon_faded, (1010,390))
        screen.blit(frostbeam_move_icon_faded, (1060,390))

        if left and not display_options:
            current = "aggressive moves"
            
    elif mousein(135,380,235,520):
        screen.blit(heal_move_icon_faded, (165,330))

        if left and not display_options:
            current = "defensive moves"

# Screen showing the player their aggressive move options
elif current == "aggressive moves":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(dog_normal, (930,440))
    
    screen.blit(kick_move_icon_solid, (960,390))
    screen.blit(headbutt_move_icon_solid, (1010,390))
    screen.blit(frostbeam_move_icon_solid, (1060,390))

    if mousein(960,390,1000,430):
        screen.blit(kick_move_info, (930,130))
    elif mousein(1010,390,1050,430):
        screen.blit(headbutt_move_info, (930,130))
    elif mousein(1060,390,1100,430):
        screen.blit(frostbeam_move_info, (930,130))
    
    if left and not display_options:
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
                current = "frostbeam move"
            else:
                display_mana_notification_time = 0
        elif not mousein(930,380,1130,540):
            current = "choose ability"

# Screen showing the player their defensive move options
elif current == "defensive moves":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(dog_normal, (930,440))
    
    screen.blit(heal_move_icon_solid, (165,330))

    if mousein(165,330,205,370):
        screen.blit(heal_move_info, (220,130))

    if left and not display_options:
        if mousein(165,330,205,370):
            if character_current_mana >= 10:
                character_current_mana -= 10
                display_mana_notification_time = 2*fps
                current = "heal move"
            else:
                display_mana_notification_time = 0
        elif not mousein(150,320,220,560):
            current = "choose ability"

# Dog dead/Victory screen
elif current == "dog dead":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(dog_dead, (930,440))
    screen.blit(victory_overlay, (0,0))
    screen.blit(continue_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not display_options:
        if mousein(1000,600,1120,650):
            current = "choose ability"
            opponent_name = "Kanye Snake"
            character_level += 1
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
            character_level += 1
            opponent_name = "Kayne Snake"
            savegame(save_number)
            current = "title"
        
# Character dead/Defeat screen
elif current == "character dead":
    screen.blit(character_dead, (150,480))
    screen.blit(dog_normal, (930,440))
    screen.blit(defeat_overlay, (0,0))
    screen.blit(try_again_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not display_options:
        if mousein(1000,600,1200,700):
            current = "choose ability"
            character_level += 0.25
            character_max_hp = 90 + 10*int(character_level)
            character_current_hp = 90 + 10*int(character_level)
            character_max_mana = 95 + 5*int(character_level)
            character_current_mana = 95 + 5*int(character_level)
            enemy_max_hp = 100
            enemy_current_hp = 100
            enemy_max_mana = 100
            enemy_current_mana = 100
            savegame(save_number)
        elif mousein(80,600,268,650):
            savegame(save_number)
            current = "title"

## Character moves
            
# Character heal move animation
elif current == "heal move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(dog_normal, (930,440))

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
            display_healed_y = display_stat_change(display_healed,170,display_healed_y)
            duration_time += 1
        else:
            # Resetting variables for next time
            heal_heart_y = 170
            display_healed_y = 360
            duration_time = 0
            healed_already = False
            dog_next_move = choose_dog_move()
            enemy_current_mana = dog_change_mana(enemy_current_mana,dog_next_move)
            current = dog_next_move

# Character kick move animation
elif current == "kick move":
    screen.blit(dog_normal, (930,440))
    
    if advancing:
        if character_kick_x == 150:
            screen.blit(character_normal, (150,380))
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
            character_stage = idle_movement(character_stage,character_number,20,character_kick_x,380)
            character_kick_x -= 36
        else:
            # Resetting variables for next time
            advancing = True
            character_kick_x = 150
            character_tilt_direction = "left"
            display_damage_y = 420
            if enemy_current_hp == 0:
                current = "dog dead"
            else:
                dog_next_move = choose_dog_move()
                enemy_current_mana = dog_change_mana(enemy_current_mana,dog_next_move)
                current = dog_next_move

    if display_damage_time < fps/2:     # Make this into a function in the future? if more battles are made (also for the heal one)
        display_damage_y = display_stat_change(display_damage,1015,display_damage_y)
        display_damage_time += 1
    else:
        display_damage_time = fps

# Character headbutt move animation
elif current == "headbutt move":
    screen.blit(dog_normal, (930,440))
    
    if advancing:
        if character_headbutt_x == 150:
            character_stage = idle_movement(character_stage,character_number,20,150,380)
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
            character_stage = idle_movement(character_stage,character_number,20,character_headbutt_x,380)
            character_headbutt_x -= 36
        else:
            # Resetting variables for next time
            advancing = True
            character_headbutt_x = 150
            display_damage_y = 420
            if enemy_current_hp == 0:
                current = "dog dead"
            else:
                dog_next_move = choose_dog_move()
                enemy_current_mana = dog_change_mana(enemy_current_mana,dog_next_move)
                current = dog_next_move

    if display_damage_time < fps/2:
        display_damage_y = display_stat_change(display_damage,1015,display_damage_y)
        display_damage_time += 1
    else:
        display_damage_time = fps
        
# Character frostbeam move animation
elif current == "frostbeam move":
    screen.blit(dog_normal, (930,440))
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
        for x in range(14):
            screen.blit(frostbeam_middle, (265+50*x,383+2*x))
        duration_time += 1
    
    else:
        # Resetting variables for next time
        display_damage_time = fps
        duration_time = 0
        if enemy_current_hp == 0:
                current = "dog dead"
        else:
            dog_next_move = choose_dog_move()
            enemy_current_mana = dog_change_mana(enemy_current_mana,dog_next_move)
            current = dog_next_move

    if display_damage_time < fps/2:
        display_damage_y = display_stat_change(display_damage,1015,display_damage_y)
        display_damage_time += 1

## Dog moves
                        
# Dog bark move animation
elif current == "dog bark move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)

    if duration_time < 2*fps:
        if duration_time == 0:
            dog_attack_sound()
        elif duration_time == 2*(fps/3):
            dog_attack_sound()
        elif duration_time == fps:
            dog_bark_damage = random.randint(5,20)
            if character_current_hp - dog_bark_damage < 0:
                dog_bark_damage = character_current_hp
            character_current_hp -= dog_bark_damage                        
            display_damage = font.render("-" + str(dog_bark_damage), True, DAMAGE_RED)
            display_damage_time = 0
            
        screen.blit(dog_bark_stance, (930,440))
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
        character_display_damage_y = display_stat_change(display_damage,170,character_display_damage_y)
        display_damage_time += 1
    else:
        character_display_damage_y = 360
        display_damage_time = fps                   
 
# Dog heal move animation
elif current == "dog heal move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(dog_normal, (930,440))

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
            display_healed_y = display_stat_change(display_healed,1015,display_healed_y)
            duration_time += 1
        else:
            # Resetting variables for next time
            enemy_heal_y = 170
            display_healed_y = 360
            duration_time = 0
            healed_already = False
            current = "choose ability"

# Dog bite move animation
elif current == "dog bite move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)

    if advancing:
        if dog_bite_x == 930:
            screen.blit(dog_normal, (930,440))
            dog_bite_x -= 24
        elif dog_bite_x > 90:
            screen.blit(dog_normal, (dog_bite_x,440))                        
            dog_bite_x -= 24
            if dog_bite_x == 330:
                dog_attack_sound()
                
        elif dog_bite_x == 90:
            screen.blit(dog_backwards, (90,440))
            bite_damage = random.randint(10,20)
            if character_current_hp - bite_damage < 0:
                bite_damage = character_current_hp
            character_current_hp -= bite_damage                        
            display_damage = font.render("-" + str(bite_damage), True, DAMAGE_RED)
            display_damage_time = 0
            dog_bite_x += 42
            advancing = False
            
    elif not advancing:
        if dog_bite_x < 930:
            screen.blit(dog_backwards, (dog_bite_x,440))
            dog_bite_x += 42
        else:
            # Resetting variables for next time
            advancing = True
            dog_bite_x = 930
            if character_current_hp == 0:
                current = "character dead"
            else:
                current = "choose ability"

    if display_damage_time < fps/2:
        character_display_damage_y = display_stat_change(display_damage,170,character_display_damage_y)
        display_damage_time += 1
    else:
        character_display_damage_y = 360
        display_damage_time = fps

# Dog spin move animation
elif current == "dog spin move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)

    if advancing:
        if dog_spin_x == 930:
            screen.blit(dog_normal, (930,440))
            dog_spin_x -= 25
        elif dog_spin_x > 180:
            screen.blit(dog_normal, (dog_spin_x,440))                        
            dog_spin_x -= 25
        elif dog_spin_x == 180:
            screen.blit(dog_normal, (180,440))
            dog_spin_time = 0
            advancing = False
            dog_attack_sound()

    elif retreating:
        if dog_spin_x < 930:
            screen.blit(dog_backwards, (dog_spin_x,440))
            dog_spin_x += 30
        else:
            advancing = True
            retreating = False
            dog_spin_x = 930
            if character_current_hp == 0:
                current = "character dead"
            else:
                current = "choose ability"                        

    if dog_spin_time < fps:
        if dog_spin_time == 15:
            spin_damage = random.randint(10,30)
            if character_current_hp - spin_damage < 0:
                spin_damage = character_current_hp
            character_current_hp -= spin_damage                        
            display_damage = font.render("-" + str(spin_damage), True, DAMAGE_RED)
            display_damage_time = 0
        if dog_spin_direction == "backwards":
            screen.blit(dog_backwards, (180,440))
            dog_spin_direction = "forwards"
        elif dog_spin_direction == "forwards":
            screen.blit(dog_normal, (180,440))
            dog_spin_direction = "backwards"
        dog_spin_time += 1
        if dog_spin_time == fps-1:
            retreating = True
    else:
        dog_spin_time = fps                                
             
    if display_damage_time < fps/2:
        character_display_damage_y = display_stat_change(display_damage,170,character_display_damage_y)
        display_damage_time += 1
    else:
        character_display_damage_y = 360
        display_damage_time = fps

# DOG BATTLE - END
