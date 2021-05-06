# Ghost Dog dead/Victory screen
if current == "ghost dog dead":
    character_stage = idle_movement(character_stage,character,20,150,380)
    screen.blit(ghost_dog_dead, (930,440))
    screen.blit(victory_overlay, (0,0))
    screen.blit(continue_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not self.game.options.is_showing:
        if mousein(1000,600,1120,650):
            current = "title"           # NEEDS CHANGING
            character_level += 1
##            current = "choose ability"         ### CHANGE THIS WHEN CLOUD BATTLE IS COMPLETE
##            opponent_name = "Spook Cloud"   (Doesn't have to be called this, change below too though if you do change it)      
##            character_level += 1
##            character_max_hp = 90 + 10*int(character_level)
##            character_current_hp = 90 + 10*int(character_level)
##            character_max_mana = 95 + 5*int(character_level)
##            character_current_mana = 95 + 5*int(character_level)
##            enemy_max_hp = 180
##            enemy_current_hp = 180
##            enemy_max_mana = 300
##            enemy_current_mana = 300
            savegame(save_number)
        elif mousein(80,600,268,650):
            #opponent_name = "Spook Cloud" ##SHOULD BE THIS, UNCOMMENT WHEN COMPLETED##
            character_level += 1
            savegame(save_number)
            current = "title"
