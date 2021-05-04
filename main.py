import time


import pygame


from lib.game import Game
from lib.options import Options
from lib.main_menu import MainMenu
from lib.image import Surface, Image, Text
from lib.player import Player
from lib.move import Move
from lib.character import Character
from lib.meme_dog import MemeDog
from lib.battle import Battle
from lib.color import Color
from lib.font import Font


pygame.init()

# Setting essential game variables
game = Game()

opacity = 10    # Variable showing opacity of fading overlay for fading in/out
fade_direction = "out"
load_file = False

# Setting up screen
pygame.display.set_caption("Sunni (Alpha 3.0)")
Surface.initialise(game)
Game.initialise()
Options.initialise()
Move.initialise(game)
Character.initialise()
Player.initialise()
MainMenu.initialise()
MemeDog.initialise()
Battle.initialise()


# Images ---------------------------------------------------------------------------------------------------------------
# Game icon
game_icon = Image("sunni_game_icon.png")
pygame.display.set_icon(game_icon.image)  # Setting the icon

# Title screen
title_screen = Image("sunni_title_screen.png", (0, 0))

# Load screens
load_game_screen = Image("sunni_load_game_screen.png", (0, 0))
enter_character_name = Image("sunni_enter_character_name.png")
continue_button_flared = Image("sunni_continue_button_flared.png")
are_you_sure = Image("sunni_are_you_sure.png")
sure_yes_flared = Image("sunni_sure_yes_flared.png", (0, 0))
sure_no_flared = Image("sunni_sure_no_flared.png", (0, 0))

# Character
character_choice1 = Image("sunni_character1_normal1.png")
character_choice2 = Image("sunni_character2_normal1.png")

# Snake
snake_normal = Image("sunni_snake_normal.png")
snake_backwards = Image("sunni_snake_backwards.png")
snake_moving = Image("sunni_snake_moving.png")
snake_dead = Image("sunni_snake_dead.png")
snake_laser_stance = Image("sunni_snake_laser_stance.png")
snake_venom_stance = Image("sunni_snake_venom_stance.png")
snake_laser_beam = Image("sunni_snake_laser_beam.png")
snake_venom_beam = Image("sunni_snake_venom_beam.png")

# Ghost Dog
ghost_dog_dead = Image("sunni_ghost_dog_dead.png")
ghost_dog_glow1 = Image("sunni_ghost_dog_glow1.png")
ghost_dog_glow2 = Image("sunni_ghost_dog_glow2.png")
ghost_dog_glow3 = Image("sunni_ghost_dog_glow3.png")
ghost_dog_glow4 = Image("sunni_ghost_dog_glow4.png")
ghost_dog_glow5 = Image("sunni_ghost_dog_glow5.png")

ghost_dog_top_claw_swipe1 = Image("sunni_ghost_dog_top_claw_swipe1.png")
ghost_dog_top_claw_swipe2 = Image("sunni_ghost_dog_top_claw_swipe2.png")
ghost_dog_top_claw_swipe3 = Image("sunni_ghost_dog_top_claw_swipe3.png")
ghost_dog_top_claw_swipe4 = Image("sunni_ghost_dog_top_claw_swipe4.png")
ghost_dog_top_claw_swipe5 = Image("sunni_ghost_dog_top_claw_swipe5.png")
ghost_dog_top_claw_size1 = Image("sunni_ghost_dog_top_claw_size1.png")
ghost_dog_top_claw_size2 = Image("sunni_ghost_dog_top_claw_size2.png")
ghost_dog_top_claw_size3 = Image("sunni_ghost_dog_top_claw_size3.png")
ghost_dog_top_claw_size4 = Image("sunni_ghost_dog_top_claw_size4.png")
ghost_dog_top_claw_size5 = Image("sunni_ghost_dog_top_claw_size5.png")
ghost_dog_top_claw_size6 = Image("sunni_ghost_dog_top_claw_size6.png")
ghost_dog_top_claw_size7 = Image("sunni_ghost_dog_top_claw_size7.png")
ghost_dog_top_claw_size8 = Image("sunni_ghost_dog_top_claw_size8.png")
ghost_dog_top_claw_fade20 = Image("sunni_ghost_dog_top_claw_fade20.png")
ghost_dog_top_claw_fade40 = Image("sunni_ghost_dog_top_claw_fade40.png")
ghost_dog_top_claw_fade60 = Image("sunni_ghost_dog_top_claw_fade60.png")
ghost_dog_top_claw_fade80 = Image("sunni_ghost_dog_top_claw_fade80.png")

ghost_dog_side_claw_swipe1 = Image("sunni_ghost_dog_side_claw_swipe1.png")
ghost_dog_side_claw_swipe2 = Image("sunni_ghost_dog_side_claw_swipe2.png")
ghost_dog_side_claw_swipe3 = Image("sunni_ghost_dog_side_claw_swipe3.png")
ghost_dog_side_claw_swipe4 = Image("sunni_ghost_dog_side_claw_swipe4.png")
ghost_dog_side_claw_swipe5 = Image("sunni_ghost_dog_side_claw_swipe5.png")
ghost_dog_side_claw_size1 = Image("sunni_ghost_dog_side_claw_size1.png")
ghost_dog_side_claw_size2 = Image("sunni_ghost_dog_side_claw_size2.png")
ghost_dog_side_claw_size3 = Image("sunni_ghost_dog_side_claw_size3.png")
ghost_dog_side_claw_size4 = Image("sunni_ghost_dog_side_claw_size4.png")
ghost_dog_side_claw_size5 = Image("sunni_ghost_dog_side_claw_size5.png")
ghost_dog_side_claw_size6 = Image("sunni_ghost_dog_side_claw_size6.png")
ghost_dog_side_claw_size7 = Image("sunni_ghost_dog_side_claw_size7.png")
ghost_dog_side_claw_size8 = Image("sunni_ghost_dog_side_claw_size8.png")
ghost_dog_side_claw_fade20 = Image("sunni_ghost_dog_side_claw_fade20.png")
ghost_dog_side_claw_fade40 = Image("sunni_ghost_dog_side_claw_fade40.png")
ghost_dog_side_claw_fade60 = Image("sunni_ghost_dog_side_claw_fade60.png")
ghost_dog_side_claw_fade80 = Image("sunni_ghost_dog_side_claw_fade80.png")


# Miscellaneous
choose_character_overlay = Image("sunni_choose_character_overlay.png")


# Text -----------------------------------------------------------------------------------------------------------------
# Opening screen - Start
# REMOVE THIS, MAYBE ADD ANOTHER OPENING SCREEN WITH A LOGO + COMPANY NAME. MAKE CREDITS FOR NAMES)
welcome_l1 = Text("Welcome to Sunni!", Font.OPENING, Color.BLACK)
welcome_l2 = Text("This is coded entirely with Python and the pygame module!", Font.OPENING, Color.BLACK)
welcome_l3 = Text("created by Andrew and co.", Font.OPENING, Color.BLACK)
welcome_l4 = Text("Enjoy!", Font.OPENING, Color.BLACK)

# Title screen - Start
game_title = Text("SUNNI", Font.TITLE, Color.MURKY_YELLOW)


# Main program loop
start_time = time.time()

while game.is_running:
    current_time = time.time() - start_time     # Storing the current amount of time that the program has been running
    game.mouse.reset_buttons()
    game.mouse.update_coordinates()
    game.keys.reset()

    # Main event loop (dealing with user input)
    for event in pygame.event.get():                    # i.e. Whenever the user does something                                                                                                                          
        if event.type == pygame.QUIT:                   # i.e. The user clicks close                                    
            game.is_running = False                     # Show that the user is finished
        elif event.type == pygame.TEXTINPUT:
            game.keys.process_text_input(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:      # Checking if the mouse button is being pressed down
            game.mouse.process_button_down()
        elif event.type == pygame.MOUSEBUTTONUP:        # Checking whether the mouse button was pressed and released
            game.mouse.process_button_up()
        elif event.type == pygame.KEYDOWN:
            game.keys.process_key_down(event)
            game.keys.process_text_input_special_keys()
        elif event.type == pygame.KEYUP:
            game.keys.process_key_up(event)

    # Opening credits
    if current_time < 5:
        game.screen.fill(Color.MILD_BLUE)
        welcome_l1.display(480, 100)
        if game.mouse.left and current_time <= 2:   # Enables the user to skip through the starting sequence by clicking
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

    elif game.current == "opening sequence":
        if current_time < 8:
            title_screen.display()
            if game.mouse.left and current_time <= 6:
                start_time = time.time() - 6

            if current_time > 6:
                game_title.display(555, 100)
                if game.mouse.left:
                    start_time = time.time() - 8
        else:
            game.main_menu.visit()

    elif game.options.is_showing:   # Options takes priority from all screens outside the opening sequence
        game.options.display()

    elif game.current == game.main_menu:
        game.current.run()

    elif game.current == "start new game":
        load_game_screen.display()
        game.display_save_names()

        if game.keys.receiving_text_input:
            enter_character_name.display(0, 0)
            if game.keys.text_input:    # Only allow the user to continue with a name entered.
                if game.keys.enter or game.keys.numpad_enter:
                    game.keys.stop_text_input()
                if game.mouse.is_in(553, 404, 727, 442):
                    continue_button_flared.display(0, 0)
                    if game.mouse.left:
                        game.keys.stop_text_input()
            Text(game.keys.text_input, Font.SUNNI, Color.BLACK, (370, 338)).display()
            if not game.keys.receiving_text_input:
                character_name = game.keys.text_input
        else:
            Text(f"Character name: {character_name}", Font.DEFAULT, Color.MILD_BLUE, (10, 10)).display()
            save_confirmed = False
            if game.display_sure:
                are_you_sure.display(0, 0)
                if game.mouse.is_in(555, 398, 630, 437):
                    sure_yes_flared.display()
                    if game.mouse.left:
                        save_confirmed = True
                        game.display_sure = False
                elif game.mouse.is_in(648, 398, 723, 437):
                    sure_no_flared.display()
                    if game.mouse.left:
                        game.select_save(None)
                        game.display_sure = False
            else:
                for save in game.saves:
                    if game.mouse.is_in(*save.button_boundaries):
                        save.button_flared.display()
                        save.display_name()
                        if game.mouse.left:
                            game.select_save(save.number)

            if game.selected_save is not None:
                if game.selected_save.is_empty or save_confirmed:
                    game.music.stop_music()
                    game.current = "choose character"
                    game.load_battle("Meme Dog")
                else:
                    game.display_sure = True

        game.run_options_and_return_to_title_logic()

    elif game.current == "load save file":
        load_game_screen.display()
        game.display_save_names()

        for save in game.saves:
            if game.mouse.is_in(*save.button_boundaries):
                save.button_flared.display()
                save.display_name()
                if game.mouse.left and not save.is_empty:
                    game.select_save(save)
                    game.load()

        game.run_options_and_return_to_title_logic()

    elif game.current == "choose character":
        game.battle.show_background()
        choose_character_overlay.display(0, 0)
        character_choice1.display(400, 300)
        character_choice2.display(810, 300)

        if game.mouse.left:
            character = None
            if game.mouse.is_in(400, 300, 470, 480):
                character = Player.CHARACTER_1
            elif game.mouse.is_in(810, 300, 880, 480):
                character = Player.CHARACTER_2

            if character is not None:
                game.player = Player(game, character_name, character)
                game.current = game.player.CHOOSE_ABILITY

    elif game.battle is not None:
        game.battle.run_all()

    else:
        print("Probably not meant to be here!")

    pygame.display.flip()   # Updating the screen at the end of drawing
    game.clock.tick(game.fps)          # Setting fps limit


# Closing the program
try:
    game.save()
except (NameError, AttributeError, ValueError):   # incase saving is not yet possible
    pass
pygame.quit()
