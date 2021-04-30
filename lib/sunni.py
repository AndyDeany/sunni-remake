import os
import time


import pygame


from lib.sunni_keydown import Keys
from lib.sunni_core_functions import *
from lib.sunni_dog_functions import *
from lib.sunni_snake_functions import *
from lib.sunni_ghost_dog_functions import *
from lib.sunni_default_battle_display import default_battle_display


pygame.init()


## Obtaining the location of the game files so they can be accessed by the program
file_directory = os.getcwd()[:-3]

## Setting essential game variables
current = "title"
music_playing = False
fps = 30    # Setting fps
fullscreen_enabled = False
display_options = False
display_sure = False
character_name_assigned = False
opacity = 10 # Variable showing opacity of fading overlay for fading in/out
fade_direction = "out"
left_held = 0
middle_held = 0
right_held = 0
volume_multiplier = 1
load_file = False

accepting_text = False
maximum_characters = 0
input_text = ""
keys_pressed = 0

# Assigning values for the times for how long keys have been held for (so the program doesn't crash if checking these values before they've been incremented,
# also so they can be incremented (they aren't reset to 0 until the key in question is released)
scrolllock = 0 #(this one is probably pointless, if you remove, remove the code below detecting scrolllock too)
Keys.initialise()
Keys.process_keydown(pygame.key.get_pressed(), accepting_text)



## Moves
duration_time = 0   # Variable to show how long something has been occuring (will be changed by other parts of the program)
damage_decided = False  # Variable to show whether or not the damage that will be done has been calculated already, so it is not done multiple times in loops
character_stage = 1
display_mana_notification_time = 2*fps # Variable to allow the "Not enough mana" notification to appear when necessary
# Heal move variables
heal_heart_y = 170
display_healed_y = 360
healed_already = False
enemy_heal_y = 230
# Kick move variables
character_kick_x = 150
character_tilt_direction = "left"
display_damage_y = 420
character_display_damage_y = 360
advancing = True
retreating = False
display_damage_time = fps
# Headbutt move variables
character_headbutt_x = 150
# Dog bite move variables
dog_bite_x = 930
# Dog spin move variables
dog_spin_x = 930
dog_spin_time = fps
dog_spin_direction = "backwards"
# Snake confuse move variables
snake_confuse_x = 930
snake_position = "normal"
snake_confuse_direction = "backwards"
# Ghost dog variables
ghost_dog_stage = 1     # Variable showing which frame of idle movement the ghost dog is in
# Ghost dog glide move variables
ghost_dog_glide_x = 930
# Ghost dog teleport move variables
started_glowing = False
ghost_dog_attack_time = fps/2
# Ghost dog claw move variables
already_clawed = False

# Setting up character and enemy stats
character_max_hp = 100
character_current_hp = 100
character_max_mana = 100
character_current_mana = 100
enemy_max_hp = 100
enemy_current_hp = 100
enemy_max_mana = 100
enemy_current_mana = 100

# Setting colours
BLACK = (0,0,0)
WHITE = (255,255,255)
MILD_BLUE = (122,222,250)
MURKY_YELLOW = (210,217,26)
MANA_BLUE = (36,91,255)
HEALTH_RED = (235,0,0)
EMPTY_BLUE = (0,20,79)
EMPTY_RED = (117,0,0)
HEAL_GREEN = (98,255,0)
DAMAGE_RED = (255,0,0)

# Setting fonts
title_font = pygame.font.SysFont("Arial Black", 40, False, False)
opening_font = pygame.font.SysFont("Arial Black", 30, False, False)
font = pygame.font.SysFont("Impact", 20, False, False)
sunni_font = pygame.font.SysFont("Candara", 40, False, False)

# Setting up screen
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunni (Alpha 3.0)")

### ------------------- VARIABLE ASSIGNMENT - END ------------------- ###

### ------------------- CLASS DEFINING - START ------------------- ###

##class Character(object):
##    def __init__(self, name, image, stage, max_hp, current_hp, max_mana, current_mana):
##        self.name = name
##        self.image = image
##        self.stage = stage
##        self.max_hp = max_hp
##        self.current_hp = current_hp
##        self.max_mana = max_mana
##        self.current_mana = current_mana
##
##    def idle_movement(self, frames, x, y):
##        if stage == 2*frames - 2:
##            self.image = pygame.image.load(file_directory + "images\sunni_" + self.name + "_normal2.png").convert_alpha()
##            screen.blit(self.image, (x,y))
##            return 1
##        else:
##            if stage <= frames:
##                self.image = pygame.image.load(file_directory + "images\sunni_" + self.name + "_normal" + str(stage) + ".png").convert_alpha()
##            else:
##                character_image = pygame.image.load(file_directory + "images\sunni_" + self.name + "_normal" + str(2*frames - stage) + ".png").convert_alpha()
##            screen.blit(character_image, (x,y))
##            return stage + 1
##
##    class Move(object):
##        def __init__(self, name, mana_cost, health_cost, mana_taken, health_taken):
##            self.name = name
##            self.mana_cost = mana_cost
##            self.health_cost = health_cost
##            self.mana_taken = mana_taken
##            self.health_taken = health_taken
##
##         Move heal(self):
##            character_stage = idle_movement(character_stage,character_number,20,150,380)
##            screen.blit(dog_normal, (930,440))
##
##            if heal_heart_y < 350:
##                if heal_heart_y == 170:
##                    heal_move_sound()
##                screen.blit(heal_heart, (160,heal_heart_y))
##                heal_heart_y += 5
##
##            else:
##                if not healed_already:
##                    healed_by = random.randint(5,15)
##                    if character_current_hp + healed_by > character_max_hp:
##                        healed_by = character_max_hp - character_current_hp
##                    character_current_hp += healed_by
##                    display_healed = font.render("+" + str(healed_by), True, HEAL_GREEN)
##                    healed_already = True
##
##                if duration_time < fps/2:
##                    display_healed_y = display_stat_change(display_healed,170,display_healed_y)
##                    duration_time += 1
##                else:
##                    # Resetting variables for next time
##                    heal_heart_y = 170
##                    display_healed_y = 360
##                    duration_time = 0
##                    healed_already = False
##                    dog_next_move = choose_dog_move()
##                    enemy_current_mana = dog_change_mana(enemy_current_mana,dog_next_move)
##                    current = dog_next_move
##
##
##class Player(Character):
##    def __init__(self, name, max_hp, current_hp, max_mana, current_mana, level):
##        super(Player, self).__init__(name, max_hp, current_hp, max_mana, current_mana)
##        self.level = level            
##
##class Opponent(Character):
##    def __init__(self, name, max_hp, current_hp, max_mana, current_mana):
##        super(Opponent, self).__init__(name, max_hp, current_hp, max_mana, current_mana)



### ------------------- CLASS DEFINING - END ------------------- ###

### ------------------- IMPORTING IMAGES - START ------------------- ###

# Game icon
print(file_directory)
print(file_directory + "images\sunni_game_icon.png")
game_icon = pygame.image.load(file_directory + "images\sunni_game_icon.png").convert_alpha()
pygame.display.set_icon(game_icon)  # Setting the icon

# Title screen
title_screen =  pygame.image.load(file_directory + "images\sunni_title_screen.png").convert_alpha()

# Main menu
main_menu = pygame.image.load(file_directory + "images\sunni_main_menu.png").convert_alpha()
menu_exit_flared = pygame.image.load(file_directory + "images\sunni_menu_exit_flared.png").convert_alpha()
menu_load_flared = pygame.image.load(file_directory + "images\sunni_menu_load_flared.png").convert_alpha()
menu_options_flared = pygame.image.load(file_directory + "images\sunni_menu_options_flared.png").convert_alpha()
menu_play_flared = pygame.image.load(file_directory + "images\sunni_menu_play_flared.png").convert_alpha()

# Load screens
load_game_screen = pygame.image.load(file_directory + "images\sunni_load_game_screen.png").convert_alpha()
enter_character_name = pygame.image.load(file_directory + "images\sunni_enter_character_name.png").convert_alpha()
continue_button_flared = pygame.image.load(file_directory + "images\sunni_continue_button_flared.png").convert_alpha()
are_you_sure = pygame.image.load(file_directory + "images\sunni_are_you_sure.png").convert_alpha()
sure_yes_flared = pygame.image.load(file_directory + "images\sunni_sure_yes_flared.png").convert_alpha()
sure_no_flared = pygame.image.load(file_directory + "images\sunni_sure_no_flared.png").convert_alpha()
load1_flared = pygame.image.load(file_directory + "images\sunni_load1_flared.png").convert_alpha()
load2_flared = pygame.image.load(file_directory + "images\sunni_load2_flared.png").convert_alpha()
load3_flared = pygame.image.load(file_directory + "images\sunni_load3_flared.png").convert_alpha()
load4_flared = pygame.image.load(file_directory + "images\sunni_load4_flared.png").convert_alpha()

# Battle screen
battle_background_hallway =  pygame.image.load(file_directory + "images\sunni_battle_background_hallway.png").convert_alpha()

# Victory and defeat overlays
victory_overlay = pygame.image.load(file_directory + "images\sunni_victory_overlay.png").convert_alpha()
defeat_overlay = pygame.image.load(file_directory + "images\sunni_defeat_overlay.png").convert_alpha()
continue_button = pygame.image.load(file_directory + "images\sunni_continue_button.png").convert_alpha()
try_again_button = pygame.image.load(file_directory + "images\sunni_try_again_button.png").convert_alpha()

# Options menu
options_button = pygame.image.load(file_directory + "images\sunni_options_button.png").convert_alpha()
return_to_game_button = pygame.image.load(file_directory + "images\sunni_return_to_game_button.png").convert_alpha()
return_to_title_button = pygame.image.load(file_directory + "images\sunni_return_to_title_button.png").convert_alpha()
options_button = pygame.image.load(file_directory + "images\sunni_options_button.png").convert_alpha()
volume_plus_button = pygame.image.load(file_directory + "images\sunni_volume_plus_button.png").convert_alpha()
volume_minus_button = pygame.image.load(file_directory + "images\sunni_volume_minus_button.png").convert_alpha()
volume_mute_button = pygame.image.load(file_directory + "images\sunni_volume_mute_button.png").convert_alpha()
fullscreen_button = pygame.image.load(file_directory + "images\sunni_fullscreen_button.png").convert_alpha()
windowed_button = pygame.image.load(file_directory + "images\sunni_windowed_button.png").convert_alpha()

# Icons
health_icon = pygame.image.load(file_directory + "images\sunni_health_icon.png").convert_alpha()
mana_icon = pygame.image.load(file_directory + "images\sunni_mana_icon.png").convert_alpha()

heal_move_icon_faded = pygame.image.load(file_directory + "images\sunni_heal_move_icon_faded.png").convert_alpha()
heal_move_icon_solid = pygame.image.load(file_directory + "images\sunni_heal_move_icon_solid.png").convert_alpha()

kick_move_icon_faded = pygame.image.load(file_directory + "images\sunni_kick_move_icon_faded.png").convert_alpha()
kick_move_icon_solid = pygame.image.load(file_directory + "images\sunni_kick_move_icon_solid.png").convert_alpha()

headbutt_move_icon_faded = pygame.image.load(file_directory + "images\sunni_headbutt_move_icon_faded.png").convert_alpha()
headbutt_move_icon_solid = pygame.image.load(file_directory + "images\sunni_headbutt_move_icon_solid.png").convert_alpha()

frostbeam_move_icon_faded = pygame.image.load(file_directory + "images\sunni_frostbeam_move_icon_faded.png").convert_alpha()
frostbeam_move_icon_solid = pygame.image.load(file_directory + "images\sunni_frostbeam_move_icon_solid.png").convert_alpha()

# Move information
kick_move_info = pygame.image.load(file_directory + "images\sunni_kick_move_info.png").convert_alpha()
heal_move_info = pygame.image.load(file_directory + "images\sunni_heal_move_info.png").convert_alpha()
headbutt_move_info = pygame.image.load(file_directory + "images\sunni_headbutt_move_info.png").convert_alpha()
frostbeam_move_info = pygame.image.load(file_directory + "images\sunni_frostbeam_move_info.png").convert_alpha()

# Character
character_choice1 = pygame.image.load(file_directory + "images\sunni_character1_normal1.png").convert_alpha()
character_choice2 = pygame.image.load(file_directory + "images\sunni_character2_normal1.png").convert_alpha()

# Dog
dog_normal = pygame.image.load(file_directory + "images\sunni_dog_normal.png").convert_alpha()
dog_dead = pygame.image.load(file_directory + "images\sunni_dog_dead.png").convert_alpha()
dog_backwards = pygame.image.load(file_directory + "images\sunni_dog_backwards.png").convert_alpha()
dog_bark_stance = pygame.image.load(file_directory + "images\sunni_dog_bark_stance.png").convert_alpha()

# Snake
snake_normal = pygame.image.load(file_directory + "images\sunni_snake_normal.png").convert_alpha()
snake_backwards = pygame.image.load(file_directory + "images\sunni_snake_backwards.png").convert_alpha()
snake_moving = pygame.image.load(file_directory + "images\sunni_snake_moving.png").convert_alpha()
snake_dead = pygame.image.load(file_directory + "images\sunni_snake_dead.png").convert_alpha()
snake_laser_stance = pygame.image.load(file_directory + "images\sunni_snake_laser_stance.png").convert_alpha()
snake_venom_stance = pygame.image.load(file_directory + "images\sunni_snake_venom_stance.png").convert_alpha()
snake_laser_beam = pygame.image.load(file_directory + "images\sunni_snake_laser_beam.png").convert_alpha()
snake_venom_beam = pygame.image.load(file_directory + "images\sunni_snake_venom_beam.png").convert_alpha()

# Ghost Dog
ghost_dog_dead = pygame.image.load(file_directory + "images\sunni_ghost_dog_dead.png").convert_alpha()
ghost_dog_glow1 = pygame.image.load(file_directory + "images\sunni_ghost_dog_glow1.png").convert_alpha()
ghost_dog_glow2 = pygame.image.load(file_directory + "images\sunni_ghost_dog_glow2.png").convert_alpha()
ghost_dog_glow3 = pygame.image.load(file_directory + "images\sunni_ghost_dog_glow3.png").convert_alpha()
ghost_dog_glow4 = pygame.image.load(file_directory + "images\sunni_ghost_dog_glow4.png").convert_alpha()
ghost_dog_glow5 = pygame.image.load(file_directory + "images\sunni_ghost_dog_glow5.png").convert_alpha()

ghost_dog_top_claw_swipe1 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_swipe1.png").convert_alpha()
ghost_dog_top_claw_swipe2 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_swipe2.png").convert_alpha()
ghost_dog_top_claw_swipe3 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_swipe3.png").convert_alpha()
ghost_dog_top_claw_swipe4 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_swipe4.png").convert_alpha()
ghost_dog_top_claw_swipe5 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_swipe5.png").convert_alpha()
ghost_dog_top_claw_size1 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size1.png").convert_alpha()
ghost_dog_top_claw_size2 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size2.png").convert_alpha()
ghost_dog_top_claw_size3 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size3.png").convert_alpha()
ghost_dog_top_claw_size4 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size4.png").convert_alpha()
ghost_dog_top_claw_size5 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size5.png").convert_alpha()
ghost_dog_top_claw_size6 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size6.png").convert_alpha()
ghost_dog_top_claw_size7 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size7.png").convert_alpha()
ghost_dog_top_claw_size8 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_size8.png").convert_alpha()
ghost_dog_top_claw_fade20 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_fade20.png").convert_alpha()
ghost_dog_top_claw_fade40 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_fade40.png").convert_alpha()
ghost_dog_top_claw_fade60 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_fade60.png").convert_alpha()
ghost_dog_top_claw_fade80 = pygame.image.load(file_directory + "images\sunni_ghost_dog_top_claw_fade80.png").convert_alpha()

ghost_dog_side_claw_swipe1 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_swipe1.png").convert_alpha()
ghost_dog_side_claw_swipe2 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_swipe2.png").convert_alpha()
ghost_dog_side_claw_swipe3 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_swipe3.png").convert_alpha()
ghost_dog_side_claw_swipe4 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_swipe4.png").convert_alpha()
ghost_dog_side_claw_swipe5 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_swipe5.png").convert_alpha()
ghost_dog_side_claw_size1 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size1.png").convert_alpha()
ghost_dog_side_claw_size2 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size2.png").convert_alpha()
ghost_dog_side_claw_size3 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size3.png").convert_alpha()
ghost_dog_side_claw_size4 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size4.png").convert_alpha()
ghost_dog_side_claw_size5 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size5.png").convert_alpha()
ghost_dog_side_claw_size6 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size6.png").convert_alpha()
ghost_dog_side_claw_size7 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size7.png").convert_alpha()
ghost_dog_side_claw_size8 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_size8.png").convert_alpha()
ghost_dog_side_claw_fade20 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_fade20.png").convert_alpha()
ghost_dog_side_claw_fade40 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_fade40.png").convert_alpha()
ghost_dog_side_claw_fade60 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_fade60.png").convert_alpha()
ghost_dog_side_claw_fade80 = pygame.image.load(file_directory + "images\sunni_ghost_dog_side_claw_fade80.png").convert_alpha()


## Moves - Start
# Heal
heal_heart = pygame.image.load(file_directory + "images\sunni_heal_heart.png").convert_alpha()

# Frostbeam
frostbeam_start = pygame.image.load(file_directory + "images\sunni_frostbeam_start.png").convert_alpha()
frostbeam_middle = pygame.image.load(file_directory + "images\sunni_frostbeam_middle.png").convert_alpha()
frostbeam_end = pygame.image.load(file_directory + "images\sunni_frostbeam_end.png").convert_alpha()

# Moves - End

# Miscellaneous
blank_overlay = pygame.image.load(file_directory + "images\sunni_blank_overlay.png").convert_alpha()
choose_character_overlay = pygame.image.load(file_directory + "images\sunni_choose_character_overlay.png").convert_alpha()

### ------------------- IMPORTING IMAGES - END ------------------- ###

### ------------------- TEXT ASSIGNMENT - START ------------------- ###

## Opening screen - Start   ### REMOVE THIS, MAYBE ADD ANOTHER OPENING SCREEN WITH A LOGO + COMPANY NAME. MAKE CREDITS FOR NAMES) ###
welcome_l1 = opening_font.render("Welcome to Sunni!", True, BLACK)
welcome_l2 = opening_font.render("This is coded entirely with Python and the pygame module!", True, BLACK)
welcome_l3 = opening_font.render("created by Andrew and co.", True, BLACK)
welcome_l4 = opening_font.render("Enjoy!", True, BLACK)
# Opening screen - End

## Title screen - Start
game_title = title_font.render("SUNNI", True, MURKY_YELLOW)

# Miscellaneous
not_enough_mana = opening_font.render("You don't have enough mana to use that", True, MANA_BLUE)

### ------------------- TEXT ASSIGNMENT - END ------------------- ###

### ------------------- PROGRAM DISPLAY - START ------------------- ###

### Start of loop which keeps screen displaying until user closes it ###

ongoing = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

start_time = time.time()
 
## -------- Main Program Loop ----------- ##
while ongoing:
    # Obtaining information
    current_time = time.time() - start_time     # Storing the current amount of time that the program has been running
    try:
        print(opponent_name + ": " + current)
    except:
        print("---: " + current)
    left = 0    # Resetting the mouse inputs to 0 (off) so the computer doesn't think the mouse is still pressed
    middle = 0
    right = 0

    Keys.initialise()
        
    mouse_position = pygame.mouse.get_pos()     # Checking the position of the mouse                            
    mouse_x = mouse_position[0]                 # Checking the x coordinate of the mouse                        
    mouse_y = mouse_position[1]                 # Checking the y coordinate of the mouse
    
    #print current   # Shows the screen the user is currently on 
    
    ## Main event loop (Reactions to user input)                                                                       
    for event in pygame.event.get():                    # i.e. Whenever the user does something                                                                                                                          
        if event.type == pygame.QUIT:                   # i.e. The user clicks close                                    
            ongoing = False                             # Show that the user is finished
            
        elif event.type == pygame.MOUSEBUTTONDOWN:      # Checking if the mouse button is being pressed down
            mouse_state = pygame.mouse.get_pressed()    # Checking whether the mouse buttons are pressed               
            left_held = mouse_state[0]                       # Checking whether the left mouse button is pressed             
            middle_held = mouse_state[1]                     # Checking whether the middle mouse button is pressed           
            right_held = mouse_state[2]                      # Checking whether the right mouse button is pressed
        elif event.type == pygame.MOUSEBUTTONUP:        # Checking whether the mouse button was pressed and released
            mouse_state = pygame.mouse.get_pressed()
            if left_held and not mouse_state[0]:
                left = 1
                left_held = 0  # Showing that the mouse button has been released
            if middle_held and not mouse_state[1]:
                middle = 1
                middle_held = 0
            if right_held and not mouse_state[2]:
                right = 1
                right_held = 0

        elif event.type == pygame.KEYDOWN:
            Keys.process_keydown(pygame.key.get_pressed(), accepting_text)
            if accepting_text:
                input_text = Keys.process_single_character_input(keys_pressed, maximum_characters, input_text)
            
        elif event.type == pygame.KEYUP:
            Keys.process_keyup(pygame.key.get_pressed())
            
        
    # Opening screen
    if current_time < 5:    # change to 5
        screen.fill(MILD_BLUE)
        screen.blit(welcome_l1, (480,100))
        if left and current_time <= 2:      # Enabling the user to skip through the starting sequence by clicking
            start_time = time.time() - 0.5
            
        if current_time > 0.5:
            screen.blit(welcome_l2, (150,140))
            if left and current_time <= 2:
                start_time = time.time() - 2
        if current_time > 2:
            screen.blit(welcome_l3, (690,500))
            if left and current_time <= 3:
                start_time = time.time() - 3
        if current_time > 3:
            screen.blit(welcome_l4, (590,300))
            if left and current_time <= 5:
                start_time = time.time() - 5

    # Other screens
    else:
        screen.fill(WHITE)

        # Title screen
        if current == "title":
            if current_time < 8:    # change to 8
                screen.blit(title_screen, (0,0))
                if left and current_time <= 6:
                    start_time = time.time() - 6

                if current_time > 6:    # change to 6
                    screen.blit(game_title, (555,100))
                    if left:
                        start_time = time.time() - 8

            else:
                if not music_playing:
                    pygame.mixer.music.load(file_directory + "audio\sunni_title_screen_music.ogg")
                    pygame.mixer.music.set_volume(0.1*volume_multiplier)
                    pygame.mixer.music.play(-1)
                    music_playing = True
                    
                screen.blit(main_menu, (0,0))
                
                if mousein(mouse_x, mouse_y, 535,269,744,345) and not display_options:    # Play button
                    screen.blit(menu_play_flared, (79,0))
                    if left:
                        input_text = "Sunni"
                        accepting_text = True
                        maximum_characters = 16
                        current = "start new game"

                elif mousein(mouse_x, mouse_y, 406,375,877,451) and not display_options:  # Load button
                    screen.blit(menu_load_flared, (82,106))
                    if left:
                        current = "load save file"

                elif mousein(mouse_x, mouse_y, 461,481,817,557) and not display_options:  # Options button
                    screen.blit(menu_options_flared, (82,212))
                    if left:
                        display_options = True
                        options_just_selected = True

                elif mousein(mouse_x, mouse_y, 547,585,734,661) and not display_options:  # Exit button
                    screen.blit(menu_exit_flared, (166,476))
                    if left:
                        ongoing = False

                elif Keys.escape and not display_options:
                    display_options = True
                    options_just_selected = True

        ## Starting the game screens
        # When 'play' is pressed; starting a new game save
        elif current == "start new game":
            screen.blit(load_game_screen, (0,0))
            save1 = open(file_directory + "saves\save1.txt", "r")
            save1_name = save1.readline()
            save1_name_text = font.render(save1_name[0:len(save1_name) - 1], True, BLACK)
            save1.close
            screen.blit(save1_name_text, (450,230))
            save2 = open(file_directory + "saves\save2.txt", "r")
            save2_name = save2.readline()
            save2_name_text = font.render(save2_name[0:len(save2_name) - 1], True, BLACK)
            save2.close
            screen.blit(save2_name_text, (450,349))
            save3 = open(file_directory + "saves\save3.txt", "r")
            save3_name = save3.readline()
            save3_name_text = font.render(save3_name[0:len(save3_name) - 1], True, BLACK)
            save3.close
            screen.blit(save3_name_text, (450,468))
            save4 = open(file_directory + "saves\save4.txt", "r")
            save4_name = save4.readline()
            save4_name_text = font.render(save4_name[0:len(save4_name) - 1], True, BLACK)
            save4.close
            screen.blit(save4_name_text, (450,587))

            if accepting_text:
                screen.blit(enter_character_name, (0,0))
                screen.blit(sunni_font.render(input_text, True, BLACK), (370,338))
                if mousein(mouse_x, mouse_y, 553,404,727,442) and not display_options:
                    screen.blit(continue_button_flared, (0,0))
                    screen.blit(sunni_font.render(input_text, True, BLACK), (370,338))
                    if left:
                        accepting_text = False
            elif not character_name_assigned:
                character_name = input_text
                input_text = ""
                character_name_assigned = True
            elif display_sure:
                screen.blit(font.render("Character name: " + character_name, True, MILD_BLUE), (10,10))
                screen.blit(are_you_sure, (0,0))
                if mousein(mouse_x, mouse_y, 555,398,630,437) and not display_options:
                    screen.blit(sure_yes_flared, (0,0))
                    if left:
                        opponent_name = "Meme Dog"
                        character_level = 1
                        pygame.mixer.music.stop()
                        music_playing = False
                        current = "choose character"
                        display_sure = False
                        character_name_assigned = False
                elif mousein(mouse_x, mouse_y, 648,398,723,437) and not display_options:
                    screen.blit(sure_no_flared, (0,0))
                    if left:
                        display_sure = False
            else:
                screen.blit(font.render("Character name: " + character_name, True, MILD_BLUE), (10,10))
                if mousein(mouse_x, mouse_y, 355,225,925,338) and not display_options:
                    screen.blit(load1_flared, (0,0))
                    screen.blit(save1_name_text, (450,230))
                    if left:
                        save_number = "1"
                        if save1_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            music_playing = False
                            current = "choose character"
                elif mousein(mouse_x, mouse_y, 355,344,925,457) and not display_options:
                    screen.blit(load2_flared, (0,0))
                    screen.blit(save2_name_text, (450,349))
                    if left:
                        save_number = "2"
                        if save2_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            music_playing = False
                            current = "choose character"
                elif mousein(mouse_x, mouse_y, 355,463,925,576) and not display_options:
                    screen.blit(load3_flared, (0,0))
                    screen.blit(save3_name_text, (450,468))
                    if left:
                        save_number = "3"
                        if save3_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            music_playing = False
                            current = "choose character"
                elif mousein(mouse_x, mouse_y, 355,582,925,695) and not display_options:
                    screen.blit(load4_flared, (0,0))
                    screen.blit(save4_name_text, (450,587))
                    if left:
                        save_number = "4"
                        if save4_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            music_playing = False
                            current = "choose character"

            screen.blit(return_to_title_button, (1082,665))
            screen.blit(options_button, (10,665))
            if (Keys.escape or (mousein(mouse_x, mouse_y, 10,665,100,715) and left == 1)) and not display_options:
                display_options = True
                options_just_selected = True
            elif mousein(mouse_x, mouse_y, 1082,665,1270,715) and left and not display_options:
                character_name_assigned = False
                current = "title"
                if not music_playing:
                    pygame.mixer.music.load(file_directory + "audio\sunni_title_screen_music.ogg")
                    pygame.mixer.music.set_volume(0.1*volume_multiplier)
                    pygame.mixer.music.play(-1)
                    music_playing = True

        # When 'load' is pressed; loading a previous save
        elif current == "load save file":
            screen.blit(load_game_screen, (0,0))
            save1 = open(file_directory + "saves\save1.txt", "r")
            save1_name = save1.readline()
            save1_name_text = font.render(save1_name[0:len(save1_name) - 1], True, BLACK)
            save1.close
            screen.blit(save1_name_text, (450,230))
            save2 = open(file_directory + "saves\save2.txt", "r")
            save2_name = save2.readline()
            save2_name_text = font.render(save2_name[0:len(save2_name) - 1], True, BLACK)
            save2.close
            screen.blit(save2_name_text, (450,349))
            save3 = open(file_directory + "saves\save3.txt", "r")
            save3_name = save3.readline()
            save3_name_text = font.render(save3_name[0:len(save3_name) - 1], True, BLACK)
            save3.close
            screen.blit(save3_name_text, (450,468))
            save4 = open(file_directory + "saves\save4.txt", "r")
            save4_name = save4.readline()
            save4_name_text = font.render(save4_name[0:len(save4_name) - 1], True, BLACK)
            save4.close
            screen.blit(save4_name_text, (450,587))

            if mousein(mouse_x, mouse_y, 355,225,925,338) and not display_options:
                screen.blit(load1_flared, (0,0))
                screen.blit(save1_name_text, (450,230))
                if left and save1_name != "No save data\n":
                    save_number = "1"
                    save = open(file_directory + "saves\save1.txt", "r")
                    load_file = True
            elif mousein(mouse_x, mouse_y, 355,344,925,457) and not display_options:
                screen.blit(load2_flared, (0,0))
                screen.blit(save2_name_text, (450,349))
                if left and save2_name != "No save data\n":
                    save_number = "2"
                    save = open(file_directory + "saves\save2.txt", "r")
                    load_file = True
            elif mousein(mouse_x, mouse_y, 355,463,925,576) and not display_options:
                screen.blit(load3_flared, (0,0))
                screen.blit(save3_name_text, (450,468))
                if left and save3_name != "No save data\n":
                    save_number = "3"
                    save = open(file_directory + "saves\save3.txt", "r")
                    load_file = True
            elif mousein(mouse_x, mouse_y, 355,582,925,695) and not display_options:
                screen.blit(load4_flared, (0,0))
                screen.blit(save4_name_text, (450,587))
                if left and save4_name != "No save data\n":
                    save_number = "4"
                    save = open(file_directory + "saves\save4.txt", "r")
                    load_file = True

            if load_file:
                character_name = save.readline()
                character_name = character_name[0:len(character_name) - 1]
                character_level = save.readline()
                character_level = int(float(character_level[0:len(character_level) - 1]))
                opponent_name = save.readline()
                opponent_name = opponent_name[0:len(opponent_name) - 1]
                character_number = save.readline()
                character_number = character_number[0:len(character_number) - 1]
                save.close
                if character_number == "character1":
                    character_normal = pygame.image.load(file_directory + "images\sunni_character1_normal1.png").convert_alpha()
                    character_backwards = pygame.image.load(file_directory + "images\sunni_character1_backwards.png").convert_alpha()
                    character_scared = pygame.image.load(file_directory + "images\sunni_character1_scared.png").convert_alpha()
                    character_scared_redflash = pygame.image.load(file_directory + "images\sunni_character1_scared_redflash.png").convert_alpha()
                    character_tilt_left = pygame.image.load(file_directory + "images\sunni_character1_tilt_left.png").convert_alpha()
                    character_tilt_right = pygame.image.load(file_directory + "images\sunni_character1_tilt_right.png").convert_alpha()
                    character_dead = pygame.image.load(file_directory + "images\sunni_character1_dead.png").convert_alpha()
                    character_headbutt_stance = pygame.image.load(file_directory + "images\sunni_character1_tilt_right.png").convert_alpha()
                    character_frostbeam_stance = pygame.image.load(file_directory + "images\sunni_character1_frostbeam_stance.png").convert_alpha()
                elif character_number == "character2":
                    character_normal = pygame.image.load(file_directory + "images\sunni_character2_normal1.png").convert_alpha()
                    character_backwards = pygame.image.load(file_directory + "images\sunni_character2_backwards.png").convert_alpha()
                    character_scared = pygame.image.load(file_directory + "images\sunni_character2_normal1.png").convert_alpha()
                    character_scared_redflash = pygame.image.load(file_directory + "images\sunni_character2_scared_redflash.png").convert_alpha()
                    character_tilt_left = pygame.image.load(file_directory + "images\sunni_character2_tilt_left.png").convert_alpha()
                    character_tilt_right = pygame.image.load(file_directory + "images\sunni_character2_tilt_right.png").convert_alpha()
                    character_dead = pygame.image.load(file_directory + "images\sunni_character2_dead.png").convert_alpha()
                    character_headbutt_stance = pygame.image.load(file_directory + "images\sunni_character2_headbutt_stance.png").convert_alpha()
                    character_frostbeam_stance = pygame.image.load(file_directory + "images\sunni_character2_frostbeam_stance.png").convert_alpha()
                load_file = False

                pygame.mixer.music.stop()
                music_playing = False

                character_max_hp = 90 + 10*int(character_level)
                character_current_hp = 90 + 10*int(character_level)
                character_max_mana = 95 + 5*int(character_level)
                character_current_mana = 95 + 5*int(character_level)
                enemy_max_hp, enemy_current_hp, enemy_max_mana, enemy_current_mana, current = assign_enemy_stats(opponent_name)


            screen.blit(return_to_title_button, (1082,665))
            screen.blit(options_button, (10,665))
            if (Keys.escape or (mousein(mouse_x, mouse_y, 10,665,100,715) and left == 1)) and not display_options:
                display_options = True
                options_just_selected = True
            elif mousein(mouse_x, mouse_y, 1082,665,1270,715) and left and not display_options:
                character_name_assigned = False
                current = "title"
                if not music_playing:
                    pygame.mixer.music.load(file_directory + "audio\sunni_title_screen_music.ogg")
                    pygame.mixer.music.set_volume(0.1*volume_multiplier)                
                    pygame.mixer.music.play(-1)
                    music_playing = True
                    
        
        ## Battle screens - Start
        else:
            # Default things that are in every battle screen
            default_battle_display(screen, font, battle_background_hallway, health_icon, mana_icon, options_button,
                                   character_name, opponent_name, left, mouse_x, mouse_y, display_options, current,
                                   character_max_hp, character_current_hp, character_max_mana, character_current_mana,
                                   enemy_max_hp, enemy_current_hp, enemy_max_mana, enemy_current_mana)

            # Choose your character page
            if current == "choose character":
                execfile(file_directory + "Python Files\sunni_character_selection.py")            

            ## Enemy battle file opening - Start
            # Dog battle
            if opponent_name == "Meme Dog":
                execfile(file_directory + "Python Files\sunni_dog_battle.py")               

            # Snake battle
            elif opponent_name == "Kanye Snake":
                execfile(file_directory + "Python Files\sunni_snake_battle.py")

            # Ghost Dog battle
            elif opponent_name == "Spook Dog":
                execfile(file_directory + "Python Files\sunni_ghost_dog_battle.py")

            else:   ## JUST FOR DEBUGGING ## (maybe make this a screen which says: "ERROR, please restart"
                screen.fill(DAMAGE_RED)   ## or something instead. Or just remove this completely
                screen.blit(title_font.render("ERROR", True, BLACK), (600,300))
            # Enemy battle file opening - End
        # Battle screens - End
        
        ## CODE THAT IS RUN THROUGH EVERY FRAME ##
        # Not enough mana notification
        if display_mana_notification_time < 2*fps:
            screen.blit(not_enough_mana, (300,200))
            display_mana_notification_time += 1

        # Input text handling
        if accepting_text:
            Keys.process_keyheld()
            input_text = Keys.process_multiple_character_input(fps, maximum_characters, input_text)
                
        # Options page
        if display_options:
            execfile(file_directory + "Python Files\sunni_options_page.py")        
                
        
    pygame.display.flip()   # Updating the screen at the end of drawing

    clock.tick(fps)          # Setting fps limit


### End of loop ###

### ------------------- PROGRAM DISPLAY - END ------------------- ###

# Closing the program
try:
    savegame(save_number)
except: # incase the variables to be saved haven't been assigned yet
    pass
pygame.quit()

close_condition = raw_input("Press Enter to Quit")  # To stop the console closing as soon as the game is closed
###^^^^^^^^^^^^^^^^^^^^^^^ remove this before compiling to a .exe file
