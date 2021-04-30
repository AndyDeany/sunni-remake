import os
import time


import pygame


from lib.sunni_keydown import Keys
from lib.sunni_core_functions import *
from lib.game import Game
from lib.character import Character
from lib.player import Player
from lib.color import Color
from lib.sunni_dog_functions import *
from lib.sunni_snake_functions import *
from lib.sunni_ghost_dog_functions import *
from lib.sunni_default_battle_display import default_battle_display
from lib.sunni_dog_battle import dog_battle_display


pygame.init()


# Setting essential game variables
game = Game()

character_name_assigned = False
opacity = 10    # Variable showing opacity of fading overlay for fading in/out
fade_direction = "out"
left_held = 0
middle_held = 0
right_held = 0
load_file = False

accepting_text = False
maximum_characters = 0
input_text = ""
keys_pressed = 0


Keys.initialise()
Keys.process_keydown(pygame.key.get_pressed(), accepting_text)

# Moves
display_mana_notification_time = 2*game.fps  # Variable to allow the "Not enough mana" notification to appear when necessary

opponent_name = None

# Setting colours

# Setting fonts
title_font = pygame.font.SysFont("Arial Black", 40, False, False)
opening_font = pygame.font.SysFont("Arial Black", 30, False, False)
game.font = pygame.font.SysFont("Impact", 20, False, False)
sunni_font = pygame.font.SysFont("Candara", 40, False, False)

# Setting up screen
size = (1280, 720)
game.screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunni (Alpha 3.0)")


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
##            self.image = pygame.image.load(game.file_directory + "images\sunni_" + self.name + "_normal2.png").convert_alpha()
##            game.screen.blit(self.image, (x,y))
##            return 1
##        else:
##            if stage <= frames:
##                self.image = pygame.image.load(game.file_directory + "images\sunni_" + self.name + "_normal" + str(stage) + ".png").convert_alpha()
##            else:
##                character_image = pygame.image.load(game.file_directory + "images\sunni_" + self.name + "_normal" + str(2*frames - stage) + ".png").convert_alpha()
##            game.screen.blit(character_image, (x,y))
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
##            character_stage = idle_movement(character_stage,game.character_number,20,150,380)
##            game.screen.blit(dog_normal, (930,440))
##
##            if heal_heart_y < 350:
##                if heal_heart_y == 170:
##                    heal_move_sound()
##                game.screen.blit(heal_heart, (160,heal_heart_y))
##                heal_heart_y += 5
##
##            else:
##                if not healed_already:
##                    healed_by = random.randint(5,15)
##                    if character_current_hp + healed_by > character_max_hp:
##                        healed_by = character_max_hp - character_current_hp
##                    character_current_hp += healed_by
##                    display_healed = game.font.render("+" + str(healed_by), True, HEAL_GREEN)
##                    healed_already = True
##
##                if duration_time < game.fps/2:
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
##                    game.current = dog_next_move
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
print(game.file_directory)
print(game.file_directory + "images\sunni_game_icon.png")
game_icon = pygame.image.load(game.file_directory + "images\sunni_game_icon.png").convert_alpha()
pygame.display.set_icon(game_icon)  # Setting the icon

# Title screen
title_screen =  pygame.image.load(game.file_directory + "images\sunni_title_screen.png").convert_alpha()

# Main menu
main_menu = pygame.image.load(game.file_directory + "images\sunni_main_menu.png").convert_alpha()
menu_exit_flared = pygame.image.load(game.file_directory + "images\sunni_menu_exit_flared.png").convert_alpha()
menu_load_flared = pygame.image.load(game.file_directory + "images\sunni_menu_load_flared.png").convert_alpha()
menu_options_flared = pygame.image.load(game.file_directory + "images\sunni_menu_options_flared.png").convert_alpha()
menu_play_flared = pygame.image.load(game.file_directory + "images\sunni_menu_play_flared.png").convert_alpha()

# Load screens
load_game_screen = pygame.image.load(game.file_directory + "images\sunni_load_game_screen.png").convert_alpha()
enter_character_name = pygame.image.load(game.file_directory + "images\sunni_enter_character_name.png").convert_alpha()
continue_button_flared = pygame.image.load(game.file_directory + "images\sunni_continue_button_flared.png").convert_alpha()
are_you_sure = pygame.image.load(game.file_directory + "images\sunni_are_you_sure.png").convert_alpha()
sure_yes_flared = pygame.image.load(game.file_directory + "images\sunni_sure_yes_flared.png").convert_alpha()
sure_no_flared = pygame.image.load(game.file_directory + "images\sunni_sure_no_flared.png").convert_alpha()
load1_flared = pygame.image.load(game.file_directory + "images\sunni_load1_flared.png").convert_alpha()
load2_flared = pygame.image.load(game.file_directory + "images\sunni_load2_flared.png").convert_alpha()
load3_flared = pygame.image.load(game.file_directory + "images\sunni_load3_flared.png").convert_alpha()
load4_flared = pygame.image.load(game.file_directory + "images\sunni_load4_flared.png").convert_alpha()

# Battle screen
battle_background_hallway =  pygame.image.load(game.file_directory + "images\sunni_battle_background_hallway.png").convert_alpha()

# Victory and defeat overlays
victory_overlay = pygame.image.load(game.file_directory + "images\sunni_victory_overlay.png").convert_alpha()
defeat_overlay = pygame.image.load(game.file_directory + "images\sunni_defeat_overlay.png").convert_alpha()
continue_button = pygame.image.load(game.file_directory + "images\sunni_continue_button.png").convert_alpha()
try_again_button = pygame.image.load(game.file_directory + "images\sunni_try_again_button.png").convert_alpha()

# Options menu
options_button = pygame.image.load(game.file_directory + "images\sunni_options_button.png").convert_alpha()
return_to_game_button = pygame.image.load(game.file_directory + "images\sunni_return_to_game_button.png").convert_alpha()
return_to_title_button = pygame.image.load(game.file_directory + "images\sunni_return_to_title_button.png").convert_alpha()
options_button = pygame.image.load(game.file_directory + "images\sunni_options_button.png").convert_alpha()
volume_plus_button = pygame.image.load(game.file_directory + "images\sunni_volume_plus_button.png").convert_alpha()
volume_minus_button = pygame.image.load(game.file_directory + "images\sunni_volume_minus_button.png").convert_alpha()
volume_mute_button = pygame.image.load(game.file_directory + "images\sunni_volume_mute_button.png").convert_alpha()
fullscreen_button = pygame.image.load(game.file_directory + "images\sunni_fullscreen_button.png").convert_alpha()
windowed_button = pygame.image.load(game.file_directory + "images\sunni_windowed_button.png").convert_alpha()

# Icons
health_icon = pygame.image.load(game.file_directory + "images\sunni_health_icon.png").convert_alpha()
mana_icon = pygame.image.load(game.file_directory + "images\sunni_mana_icon.png").convert_alpha()

heal_move_icon_faded = pygame.image.load(game.file_directory + "images\sunni_heal_move_icon_faded.png").convert_alpha()
heal_move_icon_solid = pygame.image.load(game.file_directory + "images\sunni_heal_move_icon_solid.png").convert_alpha()

kick_move_icon_faded = pygame.image.load(game.file_directory + "images\sunni_kick_move_icon_faded.png").convert_alpha()
kick_move_icon_solid = pygame.image.load(game.file_directory + "images\sunni_kick_move_icon_solid.png").convert_alpha()

headbutt_move_icon_faded = pygame.image.load(game.file_directory + "images\sunni_headbutt_move_icon_faded.png").convert_alpha()
headbutt_move_icon_solid = pygame.image.load(game.file_directory + "images\sunni_headbutt_move_icon_solid.png").convert_alpha()

frostbeam_move_icon_faded = pygame.image.load(game.file_directory + "images\sunni_frostbeam_move_icon_faded.png").convert_alpha()
frostbeam_move_icon_solid = pygame.image.load(game.file_directory + "images\sunni_frostbeam_move_icon_solid.png").convert_alpha()

# Move information
kick_move_info = pygame.image.load(game.file_directory + "images\sunni_kick_move_info.png").convert_alpha()
heal_move_info = pygame.image.load(game.file_directory + "images\sunni_heal_move_info.png").convert_alpha()
headbutt_move_info = pygame.image.load(game.file_directory + "images\sunni_headbutt_move_info.png").convert_alpha()
frostbeam_move_info = pygame.image.load(game.file_directory + "images\sunni_frostbeam_move_info.png").convert_alpha()

# Character
character_choice1 = pygame.image.load(game.file_directory + "images\sunni_character1_normal1.png").convert_alpha()
character_choice2 = pygame.image.load(game.file_directory + "images\sunni_character2_normal1.png").convert_alpha()

# Dog

# Snake
snake_normal = pygame.image.load(game.file_directory + "images\sunni_snake_normal.png").convert_alpha()
snake_backwards = pygame.image.load(game.file_directory + "images\sunni_snake_backwards.png").convert_alpha()
snake_moving = pygame.image.load(game.file_directory + "images\sunni_snake_moving.png").convert_alpha()
snake_dead = pygame.image.load(game.file_directory + "images\sunni_snake_dead.png").convert_alpha()
snake_laser_stance = pygame.image.load(game.file_directory + "images\sunni_snake_laser_stance.png").convert_alpha()
snake_venom_stance = pygame.image.load(game.file_directory + "images\sunni_snake_venom_stance.png").convert_alpha()
snake_laser_beam = pygame.image.load(game.file_directory + "images\sunni_snake_laser_beam.png").convert_alpha()
snake_venom_beam = pygame.image.load(game.file_directory + "images\sunni_snake_venom_beam.png").convert_alpha()

# Ghost Dog
ghost_dog_dead = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_dead.png").convert_alpha()
ghost_dog_glow1 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_glow1.png").convert_alpha()
ghost_dog_glow2 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_glow2.png").convert_alpha()
ghost_dog_glow3 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_glow3.png").convert_alpha()
ghost_dog_glow4 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_glow4.png").convert_alpha()
ghost_dog_glow5 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_glow5.png").convert_alpha()

ghost_dog_top_claw_swipe1 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_swipe1.png").convert_alpha()
ghost_dog_top_claw_swipe2 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_swipe2.png").convert_alpha()
ghost_dog_top_claw_swipe3 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_swipe3.png").convert_alpha()
ghost_dog_top_claw_swipe4 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_swipe4.png").convert_alpha()
ghost_dog_top_claw_swipe5 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_swipe5.png").convert_alpha()
ghost_dog_top_claw_size1 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size1.png").convert_alpha()
ghost_dog_top_claw_size2 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size2.png").convert_alpha()
ghost_dog_top_claw_size3 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size3.png").convert_alpha()
ghost_dog_top_claw_size4 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size4.png").convert_alpha()
ghost_dog_top_claw_size5 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size5.png").convert_alpha()
ghost_dog_top_claw_size6 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size6.png").convert_alpha()
ghost_dog_top_claw_size7 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size7.png").convert_alpha()
ghost_dog_top_claw_size8 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_size8.png").convert_alpha()
ghost_dog_top_claw_fade20 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_fade20.png").convert_alpha()
ghost_dog_top_claw_fade40 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_fade40.png").convert_alpha()
ghost_dog_top_claw_fade60 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_fade60.png").convert_alpha()
ghost_dog_top_claw_fade80 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_top_claw_fade80.png").convert_alpha()

ghost_dog_side_claw_swipe1 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_swipe1.png").convert_alpha()
ghost_dog_side_claw_swipe2 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_swipe2.png").convert_alpha()
ghost_dog_side_claw_swipe3 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_swipe3.png").convert_alpha()
ghost_dog_side_claw_swipe4 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_swipe4.png").convert_alpha()
ghost_dog_side_claw_swipe5 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_swipe5.png").convert_alpha()
ghost_dog_side_claw_size1 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size1.png").convert_alpha()
ghost_dog_side_claw_size2 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size2.png").convert_alpha()
ghost_dog_side_claw_size3 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size3.png").convert_alpha()
ghost_dog_side_claw_size4 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size4.png").convert_alpha()
ghost_dog_side_claw_size5 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size5.png").convert_alpha()
ghost_dog_side_claw_size6 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size6.png").convert_alpha()
ghost_dog_side_claw_size7 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size7.png").convert_alpha()
ghost_dog_side_claw_size8 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_size8.png").convert_alpha()
ghost_dog_side_claw_fade20 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_fade20.png").convert_alpha()
ghost_dog_side_claw_fade40 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_fade40.png").convert_alpha()
ghost_dog_side_claw_fade60 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_fade60.png").convert_alpha()
ghost_dog_side_claw_fade80 = pygame.image.load(game.file_directory + "images\sunni_ghost_dog_side_claw_fade80.png").convert_alpha()


# Moves
# Heal
heal_heart = pygame.image.load(game.file_directory + "images\sunni_heal_heart.png").convert_alpha()

# Frostbeam
frostbeam_start = pygame.image.load(game.file_directory + "images\sunni_frostbeam_start.png").convert_alpha()
frostbeam_middle = pygame.image.load(game.file_directory + "images\sunni_frostbeam_middle.png").convert_alpha()
frostbeam_end = pygame.image.load(game.file_directory + "images\sunni_frostbeam_end.png").convert_alpha()


# Miscellaneous
blank_overlay = pygame.image.load(game.file_directory + "images\sunni_blank_overlay.png").convert_alpha()
choose_character_overlay = pygame.image.load(game.file_directory + "images\sunni_choose_character_overlay.png").convert_alpha()


### ------------------- TEXT ASSIGNMENT - START ------------------- ###

## Opening screen - Start   ### REMOVE THIS, MAYBE ADD ANOTHER OPENING SCREEN WITH A LOGO + COMPANY NAME. MAKE CREDITS FOR NAMES) ###
welcome_l1 = opening_font.render("Welcome to Sunni!", True, Color.BLACK)
welcome_l2 = opening_font.render("This is coded entirely with Python and the pygame module!", True, Color.BLACK)
welcome_l3 = opening_font.render("created by Andrew and co.", True, Color.BLACK)
welcome_l4 = opening_font.render("Enjoy!", True, Color.BLACK)
# Opening screen - End

## Title screen - Start
game_title = title_font.render("SUNNI", True, Color.MURKY_YELLOW)

# Miscellaneous
not_enough_mana = opening_font.render("You don't have enough mana to use that", True, Color.MANA_BLUE)


# Main program loop
ongoing = True
clock = pygame.time.Clock()     # used to manage how fast the screen updates
start_time = time.time()


while ongoing:
    # Obtaining information
    current_time = time.time() - start_time     # Storing the current amount of time that the program has been running
    print(f"{opponent_name}: {game.current}")
    left = 0    # Resetting the mouse inputs to 0 (off) so the computer doesn't think the mouse is still pressed
    middle = 0
    right = 0

    Keys.initialise()
        
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Main event loop (dealing with user input)
    for event in pygame.event.get():                    # i.e. Whenever the user does something                                                                                                                          
        if event.type == pygame.QUIT:                   # i.e. The user clicks close                                    
            ongoing = False                             # Show that the user is finished
            
        elif event.type == pygame.MOUSEBUTTONDOWN:      # Checking if the mouse button is being pressed down
            mouse_state = pygame.mouse.get_pressed()    # Checking whether the mouse buttons are pressed               
            left_held = mouse_state[0]                  # Checking whether the left mouse button is pressed
            middle_held = mouse_state[1]                # Checking whether the middle mouse button is pressed
            right_held = mouse_state[2]                 # Checking whether the right mouse button is pressed
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
        game.screen.fill(Color.MILD_BLUE)
        game.screen.blit(welcome_l1, (480,100))
        if left and current_time <= 2:      # Enabling the user to skip through the starting sequence by clicking
            start_time = time.time() - 0.5
            
        if current_time > 0.5:
            game.screen.blit(welcome_l2, (150,140))
            if left and current_time <= 2:
                start_time = time.time() - 2
        if current_time > 2:
            game.screen.blit(welcome_l3, (690,500))
            if left and current_time <= 3:
                start_time = time.time() - 3
        if current_time > 3:
            game.screen.blit(welcome_l4, (590,300))
            if left and current_time <= 5:
                start_time = time.time() - 5

    # Other screens
    else:
        game.screen.fill(Color.WHITE)

        # Title screen
        if game.current == "title":
            if current_time < 8:    # change to 8
                game.screen.blit(title_screen, (0,0))
                if left and current_time <= 6:
                    start_time = time.time() - 6

                if current_time > 6:    # change to 6
                    game.screen.blit(game_title, (555,100))
                    if left:
                        start_time = time.time() - 8

            else:
                if not game.music_playing:
                    pygame.mixer.music.load(game.file_directory + "audio\sunni_title_screen_music.ogg")
                    pygame.mixer.music.set_volume(0.1*game.volume_multiplier)
                    pygame.mixer.music.play(-1)
                    game.music_playing = True
                    
                game.screen.blit(main_menu, (0,0))
                
                if mousein(mouse_x, mouse_y, 535,269,744,345) and not game.display_options:    # Play button
                    game.screen.blit(menu_play_flared, (79,0))
                    if left:
                        input_text = "Sunni"
                        accepting_text = True
                        maximum_characters = 16
                        game.current = "start new game"

                elif mousein(mouse_x, mouse_y, 406,375,877,451) and not game.display_options:  # Load button
                    game.screen.blit(menu_load_flared, (82,106))
                    if left:
                        game.current = "load save file"

                elif mousein(mouse_x, mouse_y, 461,481,817,557) and not game.display_options:  # Options button
                    game.screen.blit(menu_options_flared, (82,212))
                    if left:
                        game.display_options = True
                        options_just_selected = True

                elif mousein(mouse_x, mouse_y, 547,585,734,661) and not game.display_options:  # Exit button
                    game.screen.blit(menu_exit_flared, (166,476))
                    if left:
                        ongoing = False

                elif Keys.escape and not game.display_options:
                    game.display_options = True
                    options_just_selected = True

        ## Starting the game screens
        # When 'play' is pressed; starting a new game save
        elif game.current == "start new game":
            game.screen.blit(load_game_screen, (0, 0))

            save1_name = game.display_save_name(1, (450, 230))
            save2_name = game.display_save_name(2, (450, 349))
            save3_name = game.display_save_name(3, (450, 468))
            save4_name = game.display_save_name(4, (450, 587))

            if accepting_text:
                game.screen.blit(enter_character_name, (0,0))
                game.screen.blit(sunni_font.render(input_text, True, Color.BLACK), (370,338))
                if mousein(mouse_x, mouse_y, 553,404,727,442) and not game.display_options:
                    game.screen.blit(continue_button_flared, (0,0))
                    game.screen.blit(sunni_font.render(input_text, True, Color.BLACK), (370,338))
                    if left:
                        accepting_text = False
            elif not character_name_assigned:
                character_name = input_text
                input_text = ""
                character_name_assigned = True
            elif display_sure:
                game.screen.blit(game.font.render("Character name: " + character_name, True, Color.MILD_BLUE), (10,10))
                game.screen.blit(are_you_sure, (0,0))
                if mousein(mouse_x, mouse_y, 555,398,630,437) and not game.display_options:
                    game.screen.blit(sure_yes_flared, (0,0))
                    if left:
                        opponent_name = "Meme Dog"
                        character_level = 1
                        pygame.mixer.music.stop()
                        game.music_playing = False
                        game.current = "choose character"
                        display_sure = False
                        character_name_assigned = False
                elif mousein(mouse_x, mouse_y, 648,398,723,437) and not game.display_options:
                    game.screen.blit(sure_no_flared, (0,0))
                    if left:
                        display_sure = False
            else:
                game.screen.blit(game.font.render("Character name: " + character_name, True, Color.MILD_BLUE), (10,10))
                if mousein(mouse_x, mouse_y, 355,225,925,338) and not game.display_options:
                    game.screen.blit(load1_flared, (0,0))
                    game.display_save_name(1, (450, 230))
                    if left:
                        game.save_number = "1"
                        if save1_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            game.music_playing = False
                            game.current = "choose character"
                elif mousein(mouse_x, mouse_y, 355,344,925,457) and not game.display_options:
                    game.screen.blit(load2_flared, (0,0))
                    game.display_save_name(2, (450, 349))
                    if left:
                        game.save_number = "2"
                        if save2_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            game.music_playing = False
                            game.current = "choose character"
                elif mousein(mouse_x, mouse_y, 355,463,925,576) and not game.display_options:
                    game.screen.blit(load3_flared, (0,0))
                    game.display_save_name(3, (450, 468))
                    if left:
                        game.save_number = "3"
                        if save3_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            game.music_playing = False
                            game.current = "choose character"
                elif mousein(mouse_x, mouse_y, 355,582,925,695) and not game.display_options:
                    game.screen.blit(load4_flared, (0,0))
                    game.display_save_name(4, (450, 587))
                    if left:
                        game.save_number = "4"
                        if save4_name != "No save data\n":
                            display_sure = True
                        else:
                            opponent_name = "Meme Dog"
                            character_level = 1
                            pygame.mixer.music.stop()
                            game.music_playing = False
                            game.current = "choose character"

            game.screen.blit(return_to_title_button, (1082,665))
            game.screen.blit(options_button, (10,665))
            if (Keys.escape or (mousein(mouse_x, mouse_y, 10,665,100,715) and left == 1)) and not game.display_options:
                game.display_options = True
                options_just_selected = True
            elif mousein(mouse_x, mouse_y, 1082,665,1270,715) and left and not game.display_options:
                character_name_assigned = False
                game.current = "title"
                if not game.music_playing:
                    pygame.mixer.music.load(game.file_directory + "audio\sunni_title_screen_music.ogg")
                    pygame.mixer.music.set_volume(0.1*game.volume_multiplier)
                    pygame.mixer.music.play(-1)
                    game.music_playing = True

        # When 'load' is pressed; loading a previous save
        elif game.current == "load save file":
            game.screen.blit(load_game_screen, (0, 0))
            save1_name = game.display_save_name(1, (450, 230))
            save2_name = game.display_save_name(2, (450, 349))
            save3_name = game.display_save_name(3, (450, 468))
            save4_name = game.display_save_name(4, (450, 587))

            if mousein(mouse_x, mouse_y, 355,225,925,338) and not game.display_options:
                game.screen.blit(load1_flared, (0,0))
                game.display_save_name(1, (450, 230))
                if left and save1_name != "No save data\n":
                    game.save_number = "1"
                    save = open(game.file_directory + "saves/save1.txt", "r")
                    load_file = True
            elif mousein(mouse_x, mouse_y, 355,344,925,457) and not game.display_options:
                game.screen.blit(load2_flared, (0,0))
                game.display_save_name(2, (450, 349))
                if left and save2_name != "No save data\n":
                    game.save_number = "2"
                    save = open(game.file_directory + "saves/save2.txt", "r")
                    load_file = True
            elif mousein(mouse_x, mouse_y, 355,463,925,576) and not game.display_options:
                game.screen.blit(load3_flared, (0,0))
                game.display_save_name(3, (450, 468))
                if left and save3_name != "No save data\n":
                    game.save_number = "3"
                    save = open(game.file_directory + "saves/save3.txt", "r")
                    load_file = True
            elif mousein(mouse_x, mouse_y, 355,582,925,695) and not game.display_options:
                game.screen.blit(load4_flared, (0,0))
                game.display_save_name(4, (450, 587))
                if left and save4_name != "No save data\n":
                    game.save_number = "4"
                    save = open(game.file_directory + "saves/save4.txt", "r")
                    load_file = True

            if load_file:
                character_name = save.readline()[:-1]
                character_level = int(save.readline()[:-1])
                opponent_name = save.readline()[:-1]
                game.character_number = save.readline()[:-1]
                save.close()
                character_normal = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_normal1.png").convert_alpha()
                character_backwards = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_backwards.png").convert_alpha()
                character_scared = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_scared.png").convert_alpha()
                character_scared_redflash = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_scared_redflash.png").convert_alpha()
                character_tilt_left = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_tilt_left.png").convert_alpha()
                character_tilt_right = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_tilt_right.png").convert_alpha()
                character_dead = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_dead.png").convert_alpha()
                character_headbutt_stance = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_headbutt_stance.png").convert_alpha()
                character_frostbeam_stance = pygame.image.load(game.file_directory + f"images\sunni_{game.character_number}_frostbeam_stance.png").convert_alpha()
                load_file = False

                pygame.mixer.music.stop()
                game.music_playing = False

                game.player = Player(game, character_name, 90 + 10*int(character_level), 95 + 5*int(character_level), level=character_level)
                game.opponent = game.assign_enemy_stats(opponent_name)
                game.current = "choose ability"

            game.screen.blit(return_to_title_button, (1082,665))
            game.screen.blit(options_button, (10,665))
            if (Keys.escape or (mousein(mouse_x, mouse_y, 10,665,100,715) and left == 1)) and not game.display_options:
                game.display_options = True
                options_just_selected = True
            elif mousein(mouse_x, mouse_y, 1082,665,1270,715) and left and not game.display_options:
                character_name_assigned = False
                game.current = "title"
                if not game.music_playing:
                    pygame.mixer.music.load(game.file_directory + "audio\sunni_title_screen_music.ogg")
                    pygame.mixer.music.set_volume(0.1*game.volume_multiplier)                
                    pygame.mixer.music.play(-1)
                    game.music_playing = True
                    
        
        ## Battle screens - Start
        else:
            # Default things that are in every battle screen
            default_battle_display(game.font, battle_background_hallway, health_icon, mana_icon, options_button, left, mouse_x, mouse_y, game)

            # Choose your character page
            if game.current == "choose character":
                execfile(game.file_directory + "Python Files\sunni_character_selection.py")            

            ## Enemy battle file opening - Start
            # Dog battle
            if opponent_name == "Meme Dog":
                dog_battle_display(game, left, mouse_x, mouse_y, kick_move_icon_faded,
                                   headbutt_move_icon_faded, frostbeam_move_icon_faded, heal_move_icon_faded,
                                   kick_move_icon_solid, headbutt_move_icon_solid, frostbeam_move_icon_solid,
                                   heal_move_icon_solid, kick_move_info, headbutt_move_info, frostbeam_move_info,
                                   heal_move_info, victory_overlay, continue_button, return_to_title_button,
                                   character_dead, defeat_overlay, try_again_button, heal_heart, character_normal,
                                   character_tilt_left, character_tilt_right, character_headbutt_stance,
                                   character_frostbeam_stance, frostbeam_start, frostbeam_middle)

            # Snake battle
            elif opponent_name == "Kanye Snake":
                execfile(game.file_directory + "Python Files\sunni_snake_battle.py")

            # Ghost Dog battle
            elif opponent_name == "Spook Dog":
                execfile(game.file_directory + "Python Files\sunni_ghost_dog_battle.py")

            else:   ## JUST FOR DEBUGGING ## (maybe make this a screen which says: "ERROR, please restart"
                game.screen.fill(Color.DAMAGE_RED)    # or something instead. Or just remove this completely
                game.screen.blit(title_font.render("ERROR", True, Color.BLACK), (600,300))
            # Enemy battle file opening - End
        # Battle screens - End
        
        # CODE THAT IS RUN THROUGH EVERY FRAME
        # Not enough mana notification
        if display_mana_notification_time < 2*game.fps:
            game.screen.blit(not_enough_mana, (300,200))
            display_mana_notification_time += 1

        # Input text handling
        if accepting_text:
            Keys.process_keyheld()
            input_text = Keys.process_multiple_character_input(game.fps, maximum_characters, input_text)
                
        # Options page
        if game.display_options:
            execfile(game.file_directory + "Python Files\sunni_options_page.py")        

    pygame.display.flip()   # Updating the screen at the end of drawing

    clock.tick(game.fps)          # Setting fps limit


# Closing the program
try:
    game.save()
except NameError:   # incase the variables to be saved haven't been assigned yet
    pass
pygame.quit()

close_condition = input("Press Enter to Quit")  # To stop the console closing as soon as the game is closed
###^^^^^^^^^^^^^^^^^^^^^^^ remove this before compiling to a .exe file
