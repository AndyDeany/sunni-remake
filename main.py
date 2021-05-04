import pygame

from lib.game import Game
from lib.image import Image
from lib.page import Page


pygame.init()

# Setting essential game variables
game = Game()

opacity = 10    # Variable showing opacity of fading overlay for fading in/out
fade_direction = "out"
load_file = False

# Setting up screen
pygame.display.set_caption("Sunni (Alpha 3.0)")


# Images ---------------------------------------------------------------------------------------------------------------
# Load screens

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


# Main program loop
while game.is_running:
    game.run()

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

    if game.current == game.opening_sequence:
        game.current.run()
    elif game.options.is_showing:   # Options takes priority from all screens outside the opening sequence
        game.options.display()
    elif isinstance(game.current, Page):
        game.current.run()
    elif game.battle is not None:
        game.battle.run_all()
    else:
        print(f"Probably not meant to be here! {game.current=}")

    pygame.display.flip()       # Updating the screen at the end of drawing
    game.clock.tick(game.fps)   # Setting fps limit


# Closing the program
try:
    game.save()
except (NameError, AttributeError, ValueError):   # incase saving is not yet possible
    pass
pygame.quit()
