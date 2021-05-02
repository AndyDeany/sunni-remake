import time


import pygame


from lib.sunni_keydown import Keys
from lib.game import Game
from lib.image import Surface, Image, Text
from lib.music import Audio
from lib.player import Player
from lib.character import Character
from lib.battle import Battle
from lib.color import Color
from lib.font import Font
from lib.sunni_dog_battle import dog_battle_display


pygame.init()


# Setting essential game variables
game = Game()

opacity = 10    # Variable showing opacity of fading overlay for fading in/out
fade_direction = "out"
load_file = False

accepting_text = False
maximum_characters = 0
input_text = ""
keys_pressed = 0


Keys.initialise()
Keys.process_keydown(pygame.key.get_pressed(), accepting_text)


# Setting up screen
size = (1280, 720)
game.screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunni (Alpha 3.0)")
Surface.initialise(game)
Game.initialise()
Character.initialise()
Battle.initialise()


# Images ---------------------------------------------------------------------------------------------------------------
# Game icon
game_icon = Image("images/sunni_game_icon.png")
pygame.display.set_icon(game_icon.image)  # Setting the icon

# Title screen
title_screen = Image("images/sunni_title_screen.png", (0, 0))

# Main menu
main_menu = Image("images/sunni_main_menu.png", (0, 0))
menu_exit_flared = Image("images/sunni_menu_exit_flared.png", (166, 476))
menu_load_flared = Image("images/sunni_menu_load_flared.png", (82, 106))
menu_options_flared = Image("images/sunni_menu_options_flared.png", (82, 212))
menu_play_flared = Image("images/sunni_menu_play_flared.png", (79, 0))

# Load screens
load_game_screen = Image("images/sunni_load_game_screen.png")
enter_character_name = Image("images/sunni_enter_character_name.png")
continue_button_flared = Image("images/sunni_continue_button_flared.png")
are_you_sure = Image("images/sunni_are_you_sure.png")
sure_yes_flared = Image("images/sunni_sure_yes_flared.png")
sure_no_flared = Image("images/sunni_sure_no_flared.png")
load1_flared = Image("images/sunni_load1_flared.png")
load2_flared = Image("images/sunni_load2_flared.png")
load3_flared = Image("images/sunni_load3_flared.png")
load4_flared = Image("images/sunni_load4_flared.png")

# Battle screen

# Victory and defeat overlays
victory_overlay = Image("images/sunni_victory_overlay.png")
defeat_overlay = Image("images/sunni_defeat_overlay.png")
continue_button = Image("images/sunni_continue_button.png")
try_again_button = Image("images/sunni_try_again_button.png")

# Options menu
return_to_game_button = Image("images/sunni_return_to_game_button.png")
return_to_title_button = Image("images/sunni_return_to_title_button.png")
volume_plus_button = Image("images/sunni_volume_plus_button.png")
volume_minus_button = Image("images/sunni_volume_minus_button.png")
volume_mute_button = Image("images/sunni_volume_mute_button.png")
fullscreen_button = Image("images/sunni_fullscreen_button.png")
windowed_button = Image("images/sunni_windowed_button.png")

heal_move_icon_faded = Image("images/sunni_heal_move_icon_faded.png")
heal_move_icon_solid = Image("images/sunni_heal_move_icon_solid.png")

kick_move_icon_faded = Image("images/sunni_kick_move_icon_faded.png")
kick_move_icon_solid = Image("images/sunni_kick_move_icon_solid.png")

headbutt_move_icon_faded = Image("images/sunni_headbutt_move_icon_faded.png")
headbutt_move_icon_solid = Image("images/sunni_headbutt_move_icon_solid.png")

frostbeam_move_icon_faded = Image("images/sunni_frostbeam_move_icon_faded.png")
frostbeam_move_icon_solid = Image("images/sunni_frostbeam_move_icon_solid.png")

# Move information
kick_move_info = Image("images/sunni_kick_move_info.png")
heal_move_info = Image("images/sunni_heal_move_info.png")
headbutt_move_info = Image("images/sunni_headbutt_move_info.png")
frostbeam_move_info = Image("images/sunni_frostbeam_move_info.png")

# Character
character_choice1 = Image("images/sunni_character1_normal1.png")
character_choice2 = Image("images/sunni_character2_normal1.png")

# Dog

# Snake
snake_normal = Image("images/sunni_snake_normal.png")
snake_backwards = Image("images/sunni_snake_backwards.png")
snake_moving = Image("images/sunni_snake_moving.png")
snake_dead = Image("images/sunni_snake_dead.png")
snake_laser_stance = Image("images/sunni_snake_laser_stance.png")
snake_venom_stance = Image("images/sunni_snake_venom_stance.png")
snake_laser_beam = Image("images/sunni_snake_laser_beam.png")
snake_venom_beam = Image("images/sunni_snake_venom_beam.png")

# Ghost Dog
ghost_dog_dead = Image("images/sunni_ghost_dog_dead.png")
ghost_dog_glow1 = Image("images/sunni_ghost_dog_glow1.png")
ghost_dog_glow2 = Image("images/sunni_ghost_dog_glow2.png")
ghost_dog_glow3 = Image("images/sunni_ghost_dog_glow3.png")
ghost_dog_glow4 = Image("images/sunni_ghost_dog_glow4.png")
ghost_dog_glow5 = Image("images/sunni_ghost_dog_glow5.png")

ghost_dog_top_claw_swipe1 = Image("images/sunni_ghost_dog_top_claw_swipe1.png")
ghost_dog_top_claw_swipe2 = Image("images/sunni_ghost_dog_top_claw_swipe2.png")
ghost_dog_top_claw_swipe3 = Image("images/sunni_ghost_dog_top_claw_swipe3.png")
ghost_dog_top_claw_swipe4 = Image("images/sunni_ghost_dog_top_claw_swipe4.png")
ghost_dog_top_claw_swipe5 = Image("images/sunni_ghost_dog_top_claw_swipe5.png")
ghost_dog_top_claw_size1 = Image("images/sunni_ghost_dog_top_claw_size1.png")
ghost_dog_top_claw_size2 = Image("images/sunni_ghost_dog_top_claw_size2.png")
ghost_dog_top_claw_size3 = Image("images/sunni_ghost_dog_top_claw_size3.png")
ghost_dog_top_claw_size4 = Image("images/sunni_ghost_dog_top_claw_size4.png")
ghost_dog_top_claw_size5 = Image("images/sunni_ghost_dog_top_claw_size5.png")
ghost_dog_top_claw_size6 = Image("images/sunni_ghost_dog_top_claw_size6.png")
ghost_dog_top_claw_size7 = Image("images/sunni_ghost_dog_top_claw_size7.png")
ghost_dog_top_claw_size8 = Image("images/sunni_ghost_dog_top_claw_size8.png")
ghost_dog_top_claw_fade20 = Image("images/sunni_ghost_dog_top_claw_fade20.png")
ghost_dog_top_claw_fade40 = Image("images/sunni_ghost_dog_top_claw_fade40.png")
ghost_dog_top_claw_fade60 = Image("images/sunni_ghost_dog_top_claw_fade60.png")
ghost_dog_top_claw_fade80 = Image("images/sunni_ghost_dog_top_claw_fade80.png")

ghost_dog_side_claw_swipe1 = Image("images/sunni_ghost_dog_side_claw_swipe1.png")
ghost_dog_side_claw_swipe2 = Image("images/sunni_ghost_dog_side_claw_swipe2.png")
ghost_dog_side_claw_swipe3 = Image("images/sunni_ghost_dog_side_claw_swipe3.png")
ghost_dog_side_claw_swipe4 = Image("images/sunni_ghost_dog_side_claw_swipe4.png")
ghost_dog_side_claw_swipe5 = Image("images/sunni_ghost_dog_side_claw_swipe5.png")
ghost_dog_side_claw_size1 = Image("images/sunni_ghost_dog_side_claw_size1.png")
ghost_dog_side_claw_size2 = Image("images/sunni_ghost_dog_side_claw_size2.png")
ghost_dog_side_claw_size3 = Image("images/sunni_ghost_dog_side_claw_size3.png")
ghost_dog_side_claw_size4 = Image("images/sunni_ghost_dog_side_claw_size4.png")
ghost_dog_side_claw_size5 = Image("images/sunni_ghost_dog_side_claw_size5.png")
ghost_dog_side_claw_size6 = Image("images/sunni_ghost_dog_side_claw_size6.png")
ghost_dog_side_claw_size7 = Image("images/sunni_ghost_dog_side_claw_size7.png")
ghost_dog_side_claw_size8 = Image("images/sunni_ghost_dog_side_claw_size8.png")
ghost_dog_side_claw_fade20 = Image("images/sunni_ghost_dog_side_claw_fade20.png")
ghost_dog_side_claw_fade40 = Image("images/sunni_ghost_dog_side_claw_fade40.png")
ghost_dog_side_claw_fade60 = Image("images/sunni_ghost_dog_side_claw_fade60.png")
ghost_dog_side_claw_fade80 = Image("images/sunni_ghost_dog_side_claw_fade80.png")


# Moves
# Heal
heal_heart = Image("images/sunni_heal_heart.png")

# Frostbeam
frostbeam_start = Image("images/sunni_frostbeam_start.png")
frostbeam_middle = Image("images/sunni_frostbeam_middle.png")
frostbeam_end = Image("images/sunni_frostbeam_end.png")


# Miscellaneous
blank_overlay = Image("images/sunni_blank_overlay.png")
choose_character_overlay = Image("images/sunni_choose_character_overlay.png")


# Text -----------------------------------------------------------------------------------------------------------------
# Opening screen - Start
# REMOVE THIS, MAYBE ADD ANOTHER OPENING SCREEN WITH A LOGO + COMPANY NAME. MAKE CREDITS FOR NAMES)
welcome_l1 = Text("Welcome to Sunni!", Font.OPENING, Color.BLACK)
welcome_l2 = Text("This is coded entirely with Python and the pygame module!", Font.OPENING, Color.BLACK)
welcome_l3 = Text("created by Andrew and co.", Font.OPENING, Color.BLACK)
welcome_l4 = Text("Enjoy!", Font.OPENING, Color.BLACK)

# Title screen - Start
game_title = Text("SUNNI", Font.TITLE, Color.MURKY_YELLOW)

# Miscellaneous
not_enough_mana = Text("You don't have enough mana to use that", Font.OPENING, Color.MANA_BLUE)

# Audio
title_screen_music = Audio("sunni_title_screen_music.ogg", 0.1)


# Main program loop
ongoing = True
clock = pygame.time.Clock()     # used to manage how fast the screen updates
start_time = time.time()


while ongoing:
    # Obtaining information
    current_time = time.time() - start_time     # Storing the current amount of time that the program has been running
    # print(f"{game.opponent.name}: {game.current}")
    game.mouse.reset_buttons()

    Keys.initialise()
        
    game.mouse.update_coordinates(pygame.mouse.get_pos())

    # Main event loop (dealing with user input)
    for event in pygame.event.get():                    # i.e. Whenever the user does something                                                                                                                          
        if event.type == pygame.QUIT:                   # i.e. The user clicks close                                    
            ongoing = False                             # Show that the user is finished
            
        elif event.type == pygame.MOUSEBUTTONDOWN:      # Checking if the mouse button is being pressed down
            game.mouse.process_button_down(pygame.mouse.get_pressed())
        elif event.type == pygame.MOUSEBUTTONUP:        # Checking whether the mouse button was pressed and released
            game.mouse.process_button_up(pygame.mouse.get_pressed())
        elif event.type == pygame.KEYDOWN:
            Keys.process_keydown(pygame.key.get_pressed(), accepting_text)
            if accepting_text:
                input_text = Keys.process_single_character_input(keys_pressed, maximum_characters, input_text)
            
        elif event.type == pygame.KEYUP:
            Keys.process_keyup(pygame.key.get_pressed())

    # Opening screen
    if current_time < 5:    # change to 5
        game.screen.fill(Color.MILD_BLUE)
        welcome_l1.display(480, 100)
        if game.mouse.left and current_time <= 2:      # Enabling the user to skip through the starting sequence by clicking
            start_time = time.time() - 0.5
            
        if current_time > 0.5:
            welcome_l2.display(150, 140)
            if game.mouse.left and current_time <= 2:
                start_time = time.time() - 2
        if current_time > 2:
            welcome_l3.display(690, 500)
            if game.mouse.left and current_time <= 3:
                start_time = time.time() - 3
        if current_time > 3:
            welcome_l4.display(590, 300)
            if game.mouse.left and current_time <= 5:
                start_time = time.time() - 5

    # Other screens
    else:
        game.screen.fill(Color.WHITE)

        # Title screen
        if game.current == "opening credits":
            if current_time < 8:    # change to 8
                title_screen.display()
                if game.mouse.left and current_time <= 6:
                    start_time = time.time() - 6

                if current_time > 6:    # change to 6
                    game_title.display(555, 100)
                    if game.mouse.left:
                        start_time = time.time() - 8
            else:
                game.current = "title"
                game.music.play_music(title_screen_music)

        elif game.current == "title":
            main_menu.display()
            if game.mouse.is_in(535, 269, 744, 345) and not game.display_options:    # Play button
                menu_play_flared.display()
                if game.mouse.left:
                    input_text = "Sunni"
                    accepting_text = True
                    maximum_characters = 16
                    game.current = "start new game"
            elif game.mouse.is_in(406,375,877,451) and not game.display_options:  # Load button
                menu_load_flared.display()
                if game.mouse.left:
                    game.current = "load save file"
            elif game.mouse.is_in(461,481,817,557) and not game.display_options:  # Options button
                menu_options_flared.display()
                if game.mouse.left:
                    game.display_options = True
                    options_just_selected = True
            elif game.mouse.is_in(547,585,734,661) and not game.display_options:  # Exit button
                menu_exit_flared.display()
                if game.mouse.left:
                    ongoing = False
            elif Keys.escape and not game.display_options:
                game.display_options = True
                options_just_selected = True

        ## Starting the game screens
        # When 'play' is pressed; starting a new game save
        elif game.current == "start new game":
            load_game_screen.display(0, 0)

            save_names = [game.display_save_name(1, (450, 230)), game.display_save_name(2, (450, 349)),
                          game.display_save_name(3, (450, 468)), game.display_save_name(4, (450, 587))]

            if accepting_text:
                enter_character_name.display(0, 0)
                if game.mouse.is_in(553,404,727,442) and not game.display_options:
                    continue_button_flared.display(0, 0)
                    if game.mouse.left:
                        accepting_text = False
                        character_name = input_text
                        input_text = ""
                Text(input_text, Font.SUNNI, Color.BLACK, (370, 338)).display()
            else:
                Text(f"Character name: {character_name}", Font.DEFAULT, Color.MILD_BLUE, (10, 10)).display()
                save_selected = False
                save_confirmed = False
                if game.display_sure:
                    are_you_sure.display(0, 0)
                    if game.mouse.is_in(555, 398, 630, 437) and not game.display_options:
                        sure_yes_flared.display(0, 0)
                        if game.mouse.left:
                            save_selected = True
                            save_confirmed = True
                            game.display_sure = False
                    elif game.mouse.is_in(648,398,723,437) and not game.display_options:
                        sure_no_flared.display(0, 0)
                        if game.mouse.left:
                            game.display_sure = False
                elif not game.display_options:
                    if game.mouse.is_in(355, 225, 925, 338):
                        load1_flared.display(0, 0)
                        game.display_save_name(1, (450, 230))
                        if game.mouse.left:
                            save_selected = True
                            game.save_number = "1"
                    elif game.mouse.is_in(355, 344, 925, 457):
                        load2_flared.display(0, 0)
                        game.display_save_name(2, (450, 349))
                        if game.mouse.left:
                            save_selected = True
                            game.save_number = "2"
                    elif game.mouse.is_in(355, 463, 925, 576):
                        load3_flared.display(0, 0)
                        game.display_save_name(3, (450, 468))
                        if game.mouse.left:
                            save_selected = True
                            game.save_number = "3"
                    elif game.mouse.is_in(355, 582, 925, 695):
                        load4_flared.display(0, 0)
                        game.display_save_name(4, (450, 587))
                        if game.mouse.left:
                            save_selected = True
                            game.save_number = "4"
                if save_selected:
                    if save_names[int(game.save_number)-1] == "No save data" or save_confirmed:
                        game.music.stop()
                        game.current = "choose character"
                        game.load_battle("Meme Dog")
                    else:
                        game.display_sure = True

            return_to_title_button.display(1082, 665)
            game.OPTIONS_BUTTON.display(10, 665)
            if (Keys.escape or (game.mouse.is_in(10,665,100,715) and game.mouse.left == 1)) and not game.display_options:
                game.display_options = True
                options_just_selected = True
            elif game.mouse.is_in(1082,665,1270,715) and game.mouse.left and not game.display_options:
                game.current = "title"
                game.music.play_music(title_screen_music)

        # When 'load' is pressed; loading a previous save
        elif game.current == "load save file":
            load_game_screen.display(0, 0)
            save1_name = game.display_save_name(1, (450, 230))
            save2_name = game.display_save_name(2, (450, 349))
            save3_name = game.display_save_name(3, (450, 468))
            save4_name = game.display_save_name(4, (450, 587))

            if game.mouse.is_in(355, 225, 925, 338) and not game.display_options:
                load1_flared.display(0, 0)
                game.display_save_name(1, (450, 230))
                if game.mouse.left and save1_name != "No save data":
                    game.save_number = "1"
                    game.load_save()
            elif game.mouse.is_in(355, 344, 925, 457) and not game.display_options:
                load2_flared.display(0, 0)
                game.display_save_name(2, (450, 349))
                if game.mouse.left and save2_name != "No save data":
                    game.save_number = "2"
                    game.load_save()
            elif game.mouse.is_in(355, 463, 925, 576) and not game.display_options:
                load3_flared.display(0, 0)
                game.display_save_name(3, (450, 468))
                if game.mouse.left and save3_name != "No save data":
                    game.save_number = "3"
                    game.load_save()
            elif game.mouse.is_in(355, 582, 925, 695) and not game.display_options:
                load4_flared.display(0, 0)
                game.display_save_name(4, (450, 587))
                if game.mouse.left and save4_name != "No save data":
                    game.save_number = "4"
                    game.load_save()

            return_to_title_button.display(1082, 665)
            game.OPTIONS_BUTTON.display(10, 665)
            if (Keys.escape or (game.mouse.is_in(10,665,100,715) and game.mouse.left == 1)) and not game.display_options:
                game.display_options = True
                options_just_selected = True
            elif game.mouse.is_in(1082,665,1270,715) and game.mouse.left and not game.display_options:
                game.current = "title"
                game.music.play_music(title_screen_music)

        # Battle screens - Start
        else:
            # Choose your character page
            if game.current == "choose character":
                # Choose your character screen
                game.battle.show_background()
                choose_character_overlay.display(0, 0)
                character_choice1.display(400, 300)
                character_choice2.display(810, 300)

                if game.mouse.left and not game.display_options:
                    character_chosen = False
                    if game.mouse.is_in(400, 300, 470, 480):
                        character = "character1"
                        character_chosen = True

                    elif game.mouse.is_in(810, 300, 880, 480):
                        character = "character2"
                        character_chosen = True

                    if character_chosen:
                        game.player = Player(game, character_name, character)
                        game.current = "choose ability"
            # Default things that are in every battle screen
            elif game.battle is not None:
                game.battle.run()
                # Dog battle
                if game.opponent.name == "Meme Dog":
                    dog_battle_display(game, kick_move_icon_faded,
                                       headbutt_move_icon_faded, frostbeam_move_icon_faded, heal_move_icon_faded,
                                       kick_move_icon_solid, headbutt_move_icon_solid, frostbeam_move_icon_solid,
                                       heal_move_icon_solid, kick_move_info, headbutt_move_info, frostbeam_move_info,
                                       heal_move_info, victory_overlay, continue_button, return_to_title_button,
                                       defeat_overlay, try_again_button, heal_heart, frostbeam_start, frostbeam_middle)

                # Snake battle
                elif game.opponent.name == "Kanye Snake":
                    execfile(game.file_directory + "Python Files\sunni_snake_battle.py")

                # Ghost Dog battle
                elif game.opponent.name == "Spook Dog":
                    execfile(game.file_directory + "Python Files\sunni_ghost_dog_battle.py")

                else:
                    raise ValueError(f"Unknown opponent '{game.opponent.name}'.")


        # CODE THAT IS RUN THROUGH EVERY FRAME
        # Not enough mana notification
        if game.display_mana_notification_time > 0:
            not_enough_mana.display(300, 200)
            game.display_mana_notification_time -= 1

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
except (NameError, AttributeError):   # incase the variables to be saved haven't been assigned yet
    pass
pygame.quit()
