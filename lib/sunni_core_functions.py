## Coding related functions ##
# Defining a function to check if the mouse is in a certain area
def mousein(start_x, start_y, end_x, end_y):
    if mouse_x > start_x and mouse_x < end_x and mouse_y > start_y and mouse_y < end_y:
        return True
    else:
        return False

# Defining a function to load files from the directory
def load(file_type, name):
    file_location = file_directory + file_type + " Files\\" + name + "."
    if location == "Image":
        return pygame.image.load(file_location + "png").convert_alpha()
    elif file_type == "Sound":
        return pygame.mixer.music.load(file_location + "ogg")
    
# Defining a function to save the game
def savegame(savefile):
    save = open(file_directory + "Save Files\save" + savefile + ".txt", "w")
    save.write(character_name + "\n")
    save.write(str(character_level) + "\n")
    save.write(opponent_name + "\n")
    save.write(character_number + "\n")
    save.close()

# Defining a function to delete save files
def deletesave(savefile):
    line_number = 0
    save = open(file_directory + "Save Files\save" + savefile + ".txt", "r")
    while True:
        if save.readline() == "\n":
            number_of_lines = line_number
            break
        else:
            line_number += 1
    save.close()
    
    save = open(file_directory + "Save Files\save" + savefile + ".txt", "w")
    save.write("No save data\n")
    for line in range(number_of_lines - 1):
        save.write("\n")
    save.close()
    
# Defining a function to accept text input from the user
def accept_text():
    input_text = ""
    while True:
        key_pressed = get_key()
        if key_pressed == K_BACKSPACE and len(input_text) != 0:
            input_text = input_text[0:-1]
        elif key_pressed <= 127:
            if shift_held:
                input_text += chr(key_pressed - 32)
            else:
                input_text += chr(key_pressed)
        

# Defining a function to designate the appropriate stats to the enemy depending on what it is
def assign_enemy_stats(opponent_name):
    if opponent_name == "Meme Dog":
        max_hp = 100
        current_hp = 100
        max_mana = 100
        current_mana = 100
    elif opponent_name == "Kanye Snake":
        max_hp = 120
        current_hp = 120
        max_mana = 120
        current_mana = 120
    elif opponent_name == "Spook Dog":
        max_hp = 200
        current_hp = 200
        max_mana = 150
        current_mana = 150
        
    else:   # if there is an error
        return 1,1,1,1,"null"

    return max_hp, current_hp, max_mana, current_mana, "choose ability"
    

## Character sound functions ##
# Defining a function to play a sound when heal heart is used
def heal_move_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_heal_move.ogg")
    pygame.mixer.music.set_volume(0.1*volume_multiplier)
    pygame.mixer.music.play(0)

# Defining a function to play a sound when the character attack (with kick or headbutt)
def character_attack_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_character_attack1.ogg")
    pygame.mixer.music.set_volume(volume_multiplier)
    pygame.mixer.music.play(0)

# Defining a function to play a sound when frostbeam is user
def frostbeam_move_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_frostbeam_move.ogg")
    pygame.mixer.music.set_volume(0.2*volume_multiplier)
    pygame.mixer.music.play(0)
    
    
## Default battle functions ##
# Defining a function to display how much health or mana has been added or removed
def display_stat_change(display_amount_text,display_x,display_y):    
    screen.blit(display_amount_text, (display_x,display_y))
    return display_y - 3

# Defining a function for the idle movement of characters
def idle_movement(stage,character,frames,x,y):
    if stage == 2*frames - 2:
        character_image = pygame.image.load(file_directory + "Image Files\sunni_" + character + "_normal2.png").convert_alpha()
        screen.blit(character_image, (x,y))
        return 1
    else:
        if stage <= frames:
            character_image = pygame.image.load(file_directory + "Image Files\sunni_" + character + "_normal" + str(stage) + ".png").convert_alpha()
        else:
            character_image = pygame.image.load(file_directory + "Image Files\sunni_" + character + "_normal" + str(2*frames - stage) + ".png").convert_alpha()
        screen.blit(character_image, (x,y))
        return stage + 1

# Definining a function to make the screen fade out or in
def fade(direction,opacity):
    fade_overlay = pygame.image.load(file_directory + "Image Files\sunni_fade_overlay" + str(opacity) + ".png").convert_alpha()
    screen.blit(fade_overlay, (0,0))
    
    if direction == "in":
        new_opacity = opacity - 10
    elif direction == "out":
        new_opacity = opacity + 10
    return new_opacity
