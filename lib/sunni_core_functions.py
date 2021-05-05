import pygame


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


# Definining a function to make the screen fade out or in
def fade(direction,opacity):
    fade_overlay = pygame.image.load(file_directory + "images/sunni_fade_overlay" + str(opacity) + ".png").convert_alpha()
    screen.blit(fade_overlay, (0,0))
    
    if direction == "in":
        new_opacity = opacity - 10
    elif direction == "out":
        new_opacity = opacity + 10
    return new_opacity
