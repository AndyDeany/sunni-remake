from lib.character import Character
import pygame

# Defining a function to check if the mouse is in a certain area
def mousein(mouse_x, mouse_y, start_x, start_y, end_x, end_y):
    return mouse_x > start_x and mouse_x < end_x and mouse_y > start_y and mouse_y < end_y

# Defining a function to load files from the directory
def load(file_type, name):
    file_location = file_directory + file_type + " Files\\" + name + "."
    if location == "Image":
        return pygame.image.load(file_location + "png").convert_alpha()
    elif file_type == "Sound":
        return pygame.mixer.music.load(file_location + "ogg")
    
# Defining a function to save the game

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
        

## Character sound functions ##

    
    
## Default battle functions ##
# Defining a function to display how much health or mana has been added or removed


# Defining a function for the idle movement of characters
def idle_movement(game, frames,x,y):
    if game.player.stage == 2*frames - 2:
        character_image = pygame.image.load(game.file_directory + "images/sunni_" + game.character_number + "_normal2.png").convert_alpha()
        game.screen.blit(character_image, (x,y))
        return 1
    else:
        if game.player.stage <= frames:
            character_image = pygame.image.load(game.file_directory + "images/sunni_" + game.character_number + "_normal" + str(game.player.stage) + ".png").convert_alpha()
        else:
            character_image = pygame.image.load(game.file_directory + "images/sunni_" + game.character_number + "_normal" + str(2*frames - game.player.stage) + ".png").convert_alpha()
        game.screen.blit(character_image, (x,y))
        return game.player.stage + 1

# Definining a function to make the screen fade out or in
def fade(direction,opacity):
    fade_overlay = pygame.image.load(file_directory + "images/sunni_fade_overlay" + str(opacity) + ".png").convert_alpha()
    screen.blit(fade_overlay, (0,0))
    
    if direction == "in":
        new_opacity = opacity - 10
    elif direction == "out":
        new_opacity = opacity + 10
    return new_opacity
