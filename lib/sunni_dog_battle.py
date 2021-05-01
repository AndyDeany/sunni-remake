import random

from lib.sunni_core_functions import *


def dog_battle_display(game, left, mouse_x, mouse_y, kick_move_icon_faded,
                       headbutt_move_icon_faded, frostbeam_move_icon_faded, heal_move_icon_faded, kick_move_icon_solid,
                       headbutt_move_icon_solid, frostbeam_move_icon_solid, heal_move_icon_solid, kick_move_info,
                       headbutt_move_info, frostbeam_move_info, heal_move_info, victory_overlay,
                       continue_button, return_to_title_button, character_dead, defeat_overlay, try_again_button,
                       heal_heart, character_normal, character_tilt_left, character_tilt_right,
                       character_headbutt_stance, character_frostbeam_stance, frostbeam_start, frostbeam_middle):
    # Default battle screen, where the player chooses which move to use
    if game.current == game.player.CHOOSE_ABILITY:
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

        if mousein(mouse_x, mouse_y, 960,430,1100,540):
            game.screen.blit(kick_move_icon_faded, (960,390))
            game.screen.blit(headbutt_move_icon_faded, (1010,390))
            game.screen.blit(frostbeam_move_icon_faded, (1060,390))

            if left and not game.display_options:
                game.current = "aggressive moves"

        elif mousein(mouse_x, mouse_y, 135,380,235,520):
            game.screen.blit(heal_move_icon_faded, (165,330))

            if left and not game.display_options:
                game.current = "defensive moves"

    # Screen showing the player their aggressive move options
    elif game.current == "aggressive moves":
        game.player.stage = idle_movement(game, 20, 150, 380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

        game.screen.blit(kick_move_icon_solid, (960,390))
        game.screen.blit(headbutt_move_icon_solid, (1010,390))
        game.screen.blit(frostbeam_move_icon_solid, (1060,390))

        if mousein(mouse_x, mouse_y, 960,390,1000,430):
            game.screen.blit(kick_move_info, (930,130))
        elif mousein(mouse_x, mouse_y, 1010,390,1050,430):
            game.screen.blit(headbutt_move_info, (930,130))
        elif mousein(mouse_x, mouse_y, 1060,390,1100,430):
            game.screen.blit(frostbeam_move_info, (930,130))

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 960,390,1000,430):
                game.player.use_move(game.player.MOVE_KICK)
            elif mousein(mouse_x, mouse_y, 1010,390,1050,430):
                game.player.use_move(game.player.MOVE_HEADBUTT)
            elif mousein(mouse_x, mouse_y, 1060,390,1100,430):
                game.player.use_move(game.player.MOVE_FROSTBEAM)
            elif not mousein(mouse_x, mouse_y, 930,380,1130,540):
                game.current = game.player.CHOOSE_ABILITY

    # Screen showing the player their defensive move options
    elif game.current == "defensive moves":
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

        game.screen.blit(heal_move_icon_solid, (165,330))

        if mousein(mouse_x, mouse_y, 165,330,205,370):
            game.screen.blit(heal_move_info, (220,130))

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 165, 330, 205, 370):
                game.player.use_move(game.player.MOVE_HEAL)
            elif not mousein(mouse_x, mouse_y, 150, 320, 220, 560):
                game.current = game.player.CHOOSE_ABILITY

    # Dog dead/Victory screen
    elif game.current == game.opponent.DEAD:
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_dead, (930,440))
        game.screen.blit(victory_overlay, (0,0))
        game.screen.blit(continue_button, (1000,600))
        game.screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 1000,600,1120,650):
                game.current = game.player.CHOOSE_ABILITY
                game.player.level_up()
                game.load_opponent("Kanye Snake")
                game.save()
            elif mousein(mouse_x, mouse_y, 80,600,268,650):
                game.player.level_up()
                game.load_opponent("Kanye Snake")
                game.save()
                game.current = "title"

    # Character dead/Defeat screen
    elif game.current == game.player.DEAD:
        game.screen.blit(character_dead, (150,480))
        game.screen.blit(game.opponent.dog_normal, (930,440))
        game.screen.blit(defeat_overlay, (0,0))
        game.screen.blit(try_again_button, (1000,600))
        game.screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 1000, 600, 1200, 700):
                game.current = game.player.CHOOSE_ABILITY
                game.player.level_up(0.25)
                game.player.fully_restore()
                game.opponent.fully_restore()
                game.save()
            elif mousein(mouse_x, mouse_y, 80, 600, 268, 650):
                game.save()
                game.current = "title"

    # Character moves
    # Character heal move animation
    elif game.current == game.player.MOVE_HEAL:
        game.player.stage = idle_movement(game, 20, 150, 380)
        game.screen.blit(game.opponent.dog_normal, (930, 440))

        if game.player.heal_heart_y < 350:
            if game.player.heal_heart_y == 170:
                game.player.heal_move_sound()
            game.screen.blit(heal_heart, (160, game.player.heal_heart_y))
            game.player.heal_heart_y += 5
        else:
            game.player.heal(random.randint(5, 15))
            game.player.heal_heart_y = 170
            game.opponent.next_move()

    # Character kick move animation
    elif game.current == game.player.MOVE_KICK:
        game.screen.blit(game.opponent.dog_normal, (930, 440))

        if game.player.is_advancing:
            if game.player.kick_x == 150:
                game.screen.blit(character_normal, (150, 380))
                game.player.kick_x += 24
            elif game.player.kick_x < 870:
                if game.player.tilt_direction == "left":
                    image = character_tilt_left
                    game.player.tilt_direction = "right"
                elif game.player.tilt_direction == "right":
                    image = character_tilt_right
                    game.player.tilt_direction = "left"
                game.screen.blit(image, (game.player.kick_x, 380))
                game.player.kick_x += 24
                if game.player.kick_x == 750:
                    game.player.attack_sound()

            elif game.player.kick_x == 870:
                game.screen.blit(character_tilt_left, (870, 380))
                game.opponent.damage(random.randint(8, 12))
                game.player.kick_x -= 36
                game.player.is_advancing = False

        elif not game.player.is_advancing:
            if game.player.kick_x > 150:
                game.player.stage = idle_movement(game, 20, game.player.kick_x, 380)
                game.player.kick_x -= 36
            else:
                # Resetting variables for next time
                game.player.is_advancing = True
                game.player.kick_x = 150
                game.player.tilt_direction = "left"
                game.opponent.next_move()

    # Character headbutt move animation
    elif game.current == game.player.MOVE_HEADBUTT:
        game.screen.blit(game.opponent.dog_normal, (930,440))

        if game.player.is_advancing:
            if game.player.headbutt_x == 150:
                game.player.stage = idle_movement(game, 20,150,380)
                game.player.headbutt_x += 24
            elif game.player.headbutt_x < 870:
                game.screen.blit(character_headbutt_stance, (game.player.headbutt_x,380))
                game.player.headbutt_x += 24
                if game.player.headbutt_x == 750:
                    game.player.attack_sound()

            elif game.player.headbutt_x == 870:
                game.screen.blit(character_headbutt_stance, (870,380))
                game.opponent.damage(random.randint(10, 20))
                game.player.headbutt_x -= 36
                game.player.is_advancing = False

        elif not game.player.is_advancing:
            if game.player.headbutt_x > 150:
                game.player.stage = idle_movement(game, 20,game.player.headbutt_x,380)
                game.player.headbutt_x -= 36
            else:
                # Resetting variables for next time
                game.player.is_advancing = True
                game.player.headbutt_x = 150
                game.opponent.next_move()

    # Character frostbeam move animation
    elif game.current == game.player.MOVE_FROSTBEAM:
        game.screen.blit(game.opponent.dog_normal, (930,440))
        game.screen.blit(character_frostbeam_stance, (150,380))

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                game.player.frostbeam_move_sound()
            elif game.duration_time == game.fps:
                game.opponent.damage(random.randint(15, 30))

            game.screen.blit(frostbeam_start, (215,381))
            for x in range(14):
                game.screen.blit(frostbeam_middle, (265+50*x,383+2*x))
            game.duration_time += 1

        else:
            # Resetting variables for next time
            game.duration_time = 0
            game.opponent.next_move()

    # Dog moves
    # Dog bark move animation
    elif game.current == game.opponent.MOVE_BARK:
        game.player.stage = idle_movement(game, 20,150,380)

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                game.opponent.attack_sound()
            elif game.duration_time == 2*int(game.fps/3):
                game.opponent.attack_sound()
            elif game.duration_time == game.fps:
                game.player.damage(random.randint(5, 20))

            game.screen.blit(game.opponent.dog_bark_stance, (930,440))
            game.duration_time += 1

        else:
            # Resetting variables for next time
            game.duration_time = 0
            game.player.next_move()

    # Dog heal move animation
    elif game.current == game.opponent.MOVE_HEAL:
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

        if game.opponent.heal_heart_y < 410:
            if game.opponent.heal_heart_y == 230:
                game.player.heal_move_sound()
            game.screen.blit(heal_heart, (1005, game.opponent.heal_heart_y))
            game.opponent.heal_heart_y += 5

        else:
            game.opponent.heal(random.randint(5, 15))
            game.opponent.heal_heart_y = 230
            game.current = game.player.CHOOSE_ABILITY

    # Dog bite move animation
    elif game.current == game.opponent.MOVE_BITE:
        game.player.stage = idle_movement(game, 20 ,150, 380)

        if game.opponent.is_advancing:
            if game.opponent.bite_x == 930:
                game.screen.blit(game.opponent.dog_normal, (930,440))
                game.opponent.bite_x -= 24
            elif game.opponent.bite_x > 90:
                game.screen.blit(game.opponent.dog_normal, (game.opponent.bite_x,440))
                game.opponent.bite_x -= 24
                if game.opponent.bite_x == 330:
                    game.opponent.attack_sound()

            elif game.opponent.bite_x == 90:
                game.screen.blit(game.opponent.dog_backwards, (90,440))
                game.player.damage(random.randint(10, 20))
                game.opponent.bite_x += 42
                game.opponent.is_advancing = False

        elif not game.opponent.is_advancing:
            if game.opponent.bite_x < 930:
                game.screen.blit(game.opponent.dog_backwards, (game.opponent.bite_x,440))
                game.opponent.bite_x += 42
            else:
                # Resetting variables for next time
                game.opponent.is_advancing = True
                game.opponent.bite_x = 930
                game.player.next_move()

    # Dog spin move animation
    elif game.current == game.opponent.MOVE_SPIN:
        game.player.stage = idle_movement(game, 20,150,380)

        if game.opponent.is_advancing:
            if game.opponent.spin_x == 930:
                game.screen.blit(game.opponent.dog_normal, (930,440))
                game.opponent.spin_x -= 25
            elif game.opponent.spin_x > 180:
                game.screen.blit(game.opponent.dog_normal, (game.opponent.spin_x,440))
                game.opponent.spin_x -= 25
            elif game.opponent.spin_x == 180:
                game.screen.blit(game.opponent.dog_normal, (180,440))
                game.opponent.spin_time = 0
                game.opponent.is_advancing = False
                game.opponent.attack_sound()

        elif game.opponent.is_retreating:
            if game.opponent.spin_x < 930:
                game.screen.blit(game.opponent.dog_backwards, (game.opponent.spin_x,440))
                game.opponent.spin_x += 30
            else:
                game.opponent.is_advancing = True
                game.opponent.is_retreating = False
                game.opponent.spin_x = 930
                game.player.next_move()

        if game.opponent.spin_time < game.fps:
            if game.opponent.spin_time == 15:
                game.player.damage(random.randint(10, 30))
            if game.opponent.spin_direction == "backwards":
                game.screen.blit(game.opponent.dog_backwards, (180,440))
                game.opponent.spin_direction = "forwards"
            elif game.opponent.spin_direction == "forwards":
                game.screen.blit(game.opponent.dog_normal, (180,440))
                game.opponent.spin_direction = "backwards"
            game.opponent.spin_time += 1
            if game.opponent.spin_time == game.fps-1:
                game.opponent.is_retreating = True
        else:
            game.opponent.spin_time = game.fps

    if game.player.display_stat_change_time > 0:
        game.player.display_stat_change()
        game.player.display_stat_change_time -= 1
    elif game.player.display_stat_change_time == 0:
        game.player.reset_display_stat_y()
        game.player.display_stat_change_time -= 1

    if game.opponent.display_stat_change_time > 0:
        game.opponent.display_stat_change()
        game.opponent.display_stat_change_time -= 1
    elif game.opponent.display_stat_change_time == 0:
        game.opponent.reset_display_stat_y()
        game.opponent.display_stat_change_time -= 1
