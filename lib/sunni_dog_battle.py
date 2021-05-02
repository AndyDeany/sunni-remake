import random

from lib.sunni_core_functions import *


def dog_battle_display(game, victory_overlay, continue_button, return_to_title_button, defeat_overlay,
                       try_again_button, heal_heart, frostbeam_start, frostbeam_middle):
    # Default battle screen, where the player chooses which move to use
    if game.current == game.player.CHOOSE_ABILITY:
        game.player.idle_movement(150, 380)
        game.opponent.dog_normal.display(930, 440)

        if game.mouse.is_in(960, 430, 1100, 540):
            game.player.MOVE_KICK.icon_faded.display(960, 390)
            game.player.MOVE_HEADBUTT.icon_faded.display(1010, 390)
            game.player.MOVE_FROSTBEAM.icon_faded.display(1060, 390)

            if game.mouse.left and not game.display_options:
                game.current = "aggressive moves"

        elif game.mouse.is_in(135, 380, 235, 520):
            game.player.MOVE_HEAL.icon_faded.display(165, 330)

            if game.mouse.left and not game.display_options:
                game.current = "defensive moves"

    # Screen showing the player their aggressive move options
    elif game.current == "aggressive moves":
        game.player.idle_movement(150, 380)
        game.opponent.dog_normal.display(930, 440)

        game.player.MOVE_KICK.icon.display(960, 390)
        game.player.MOVE_HEADBUTT.icon.display(1010, 390)
        game.player.MOVE_FROSTBEAM.icon.display(1060, 390)

        if game.mouse.is_in(960,390,1000,430):
            game.player.MOVE_KICK.info.display(930, 130)
        elif game.mouse.is_in(1010,390,1050,430):
            game.player.MOVE_HEADBUTT.info.display(930, 130)
        elif game.mouse.is_in(1060,390,1100,430):
            game.player.MOVE_FROSTBEAM.info.display(930, 130)

        if game.mouse.left and not game.display_options:
            if game.mouse.is_in(960,390,1000,430):
                game.player.use_move(game.player.MOVE_KICK)
            elif game.mouse.is_in(1010,390,1050,430):
                game.player.use_move(game.player.MOVE_HEADBUTT)
            elif game.mouse.is_in(1060,390,1100,430):
                game.player.use_move(game.player.MOVE_FROSTBEAM)
            elif not game.mouse.is_in(930,380,1130,540):
                game.current = game.player.CHOOSE_ABILITY

    # Screen showing the player their defensive move options
    elif game.current == "defensive moves":
        game.player.idle_movement(150,380)
        game.opponent.dog_normal.display(930, 440)

        game.player.MOVE_HEAL.icon.display(165, 330)

        if game.mouse.is_in(165,330,205,370):
            game.player.MOVE_HEAL.info.display(220, 130)

        if game.mouse.left and not game.display_options:
            if game.mouse.is_in(165, 330, 205, 370):
                game.player.use_move(game.player.MOVE_HEAL)
            elif not game.mouse.is_in(150, 320, 220, 560):
                game.current = game.player.CHOOSE_ABILITY

    # Dog dead/Victory screen
    elif game.current == game.opponent.DEAD:
        game.player.idle_movement(150,380)
        game.opponent.dog_dead.display(930, 440)
        victory_overlay.display(0, 0)
        continue_button.display(1000, 600)
        return_to_title_button.display(80, 600)   # Stopping the return to title button being faded out by the overlay

        if game.mouse.left and not game.display_options:
            if game.mouse.is_in(1000,600,1120,650):
                game.current = game.player.CHOOSE_ABILITY
                game.player.level_up()
                game.load_battle("Kanye Snake")
                game.save()
            elif game.mouse.is_in(80,600,268,650):
                game.player.level_up()
                game.load_battle("Kanye Snake")
                game.save()
                game.current = "title"

    # Character dead/Defeat screen
    elif game.current == game.player.DEAD:
        game.player.character_dead.display(150, 480)
        game.opponent.dog_normal.display(930, 440)
        defeat_overlay.display(0, 0)
        try_again_button.display(1000, 600)
        return_to_title_button.display(80, 600)   # Stopping the return to title button being faded out by the overlay

        if game.mouse.left and not game.display_options:
            if game.mouse.is_in(1000, 600, 1200, 700):
                game.current = game.player.CHOOSE_ABILITY
                game.player.level_up(0.25)
                game.player.fully_restore()
                game.opponent.fully_restore()
                game.save()
            elif game.mouse.is_in(80, 600, 268, 650):
                game.save()
                game.current = "title"

    # Character moves
    # Character heal move animation
    elif game.current == game.player.MOVE_HEAL:
        game.player.idle_movement(150, 380)
        game.opponent.dog_normal.display(930, 440)

        if game.player.heal_heart_y < 350:
            if game.player.heal_heart_y == 170:
                game.player.MOVE_HEAL.play_sound()
            heal_heart.display(160, game.player.heal_heart_y)
            game.player.heal_heart_y += 5
        else:
            game.player.heal(random.randint(5, 15))
            game.player.heal_heart_y = 170
            game.opponent.next_move()

    # Character kick move animation
    elif game.current == game.player.MOVE_KICK:
        game.opponent.dog_normal.display(930, 440)

        if game.player.is_advancing:
            if game.player.kick_x == 150:
                game.player.character_normal.display(150, 380)
                game.player.kick_x += 24
            elif game.player.kick_x < 870:
                if game.player.tilt_direction == "left":
                    image = game.player.character_tilt_left
                    game.player.tilt_direction = "right"
                elif game.player.tilt_direction == "right":
                    image = game.player.character_tilt_right
                    game.player.tilt_direction = "left"
                image.display(game.player.kick_x, 380)
                game.player.kick_x += 24
                if game.player.kick_x == 750:
                    game.player.MOVE_KICK.play_sound()

            elif game.player.kick_x == 870:
                game.player.character_tilt_left.display(870, 380)
                game.opponent.damage(random.randint(8, 12))
                game.player.kick_x -= 36
                game.player.is_advancing = False

        elif not game.player.is_advancing:
            if game.player.kick_x > 150:
                game.player.idle_movement(game.player.kick_x, 380)
                game.player.kick_x -= 36
            else:
                # Resetting variables for next time
                game.player.is_advancing = True
                game.player.kick_x = 150
                game.player.tilt_direction = "left"
                game.opponent.next_move()

    # Character headbutt move animation
    elif game.current == game.player.MOVE_HEADBUTT:
        game.opponent.dog_normal.display(930, 440)

        if game.player.is_advancing:
            if game.player.headbutt_x == 150:
                game.player.idle_movement(150,380)
                game.player.headbutt_x += 24
            elif game.player.headbutt_x < 870:
                game.player.character_headbutt_stance.display(game.player.headbutt_x, 380)
                game.player.headbutt_x += 24
                if game.player.headbutt_x == 750:
                    game.player.MOVE_HEADBUTT.play_sound()

            elif game.player.headbutt_x == 870:
                game.player.character_headbutt_stance.display(870, 380)
                game.opponent.damage(random.randint(10, 20))
                game.player.headbutt_x -= 36
                game.player.is_advancing = False

        elif not game.player.is_advancing:
            if game.player.headbutt_x > 150:
                game.player.idle_movement(game.player.headbutt_x,380)
                game.player.headbutt_x -= 36
            else:
                # Resetting variables for next time
                game.player.is_advancing = True
                game.player.headbutt_x = 150
                game.opponent.next_move()

    # Character frostbeam move animation
    elif game.current == game.player.MOVE_FROSTBEAM:
        game.opponent.dog_normal.display(930, 440)
        game.player.character_frostbeam_stance.display(150, 380)

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                game.player.MOVE_FROSTBEAM.play_sound()
            elif game.duration_time == game.fps:
                game.opponent.damage(random.randint(15, 30))

            frostbeam_start.display(215, 381)
            for x in range(14):
                frostbeam_middle.display(265+50*x, 383+2*x)
            game.duration_time += 1

        else:
            # Resetting variables for next time
            game.duration_time = 0
            game.opponent.next_move()

    # Dog moves
    # Dog bark move animation
    elif game.current == game.opponent.MOVE_BARK:
        game.player.idle_movement(150,380)

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                game.opponent.MOVE_BARK.play_sound()
            elif game.duration_time == 2*int(game.fps/3):
                game.opponent.MOVE_BARK.play_sound()
            elif game.duration_time == game.fps:
                game.player.damage(random.randint(5, 20))

            game.opponent.dog_bark_stance.display(930, 440)
            game.duration_time += 1

        else:
            # Resetting variables for next time
            game.duration_time = 0
            game.player.next_move()

    # Dog heal move animation
    elif game.current == game.opponent.MOVE_HEAL:
        game.player.idle_movement(150,380)
        game.opponent.dog_normal.display(930, 440)

        if game.opponent.heal_heart_y < 410:
            if game.opponent.heal_heart_y == 230:
                game.player.MOVE_HEAL.play_sound()
            heal_heart.display(1005, game.opponent.heal_heart_y)
            game.opponent.heal_heart_y += 5

        else:
            game.opponent.heal(random.randint(5, 15))
            game.opponent.heal_heart_y = 230
            game.current = game.player.CHOOSE_ABILITY

    # Dog bite move animation
    elif game.current == game.opponent.MOVE_BITE:
        game.player.idle_movement(150, 380)

        if game.opponent.is_advancing:
            if game.opponent.bite_x == 930:
                game.opponent.dog_normal.display(930, 440)
                game.opponent.bite_x -= 24
            elif game.opponent.bite_x > 90:
                game.opponent.dog_normal.display(game.opponent.bite_x, 440)
                game.opponent.bite_x -= 24
                if game.opponent.bite_x == 330:
                    game.opponent.MOVE_BITE.play_sound()

            elif game.opponent.bite_x == 90:
                game.opponent.dog_backwards.display(90, 440)
                game.player.damage(random.randint(10, 20))
                game.opponent.bite_x += 42
                game.opponent.is_advancing = False

        elif not game.opponent.is_advancing:
            if game.opponent.bite_x < 930:
                game.opponent.dog_backwards.display(game.opponent.bite_x, 440)
                game.opponent.bite_x += 42
            else:
                # Resetting variables for next time
                game.opponent.is_advancing = True
                game.opponent.bite_x = 930
                game.player.next_move()

    # Dog spin move animation
    elif game.current == game.opponent.MOVE_SPIN:
        game.player.idle_movement(150,380)

        if game.opponent.is_advancing:
            if game.opponent.spin_x == 930:
                game.opponent.dog_normal.display(930, 440)
                game.opponent.spin_x -= 25
            elif game.opponent.spin_x > 180:
                game.opponent.dog_normal.display(game.opponent.spin_x, 440)
                game.opponent.spin_x -= 25
            elif game.opponent.spin_x == 180:
                game.opponent.dog_normal.display(180, 440)
                game.opponent.spin_time = 0
                game.opponent.is_advancing = False
                game.opponent.MOVE_SPIN.play_sound()

        elif game.opponent.is_retreating:
            if game.opponent.spin_x < 930:
                game.opponent.dog_backwards.display(game.opponent.spin_x, 440)
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
                game.opponent.dog_backwards.display(180, 440)
                game.opponent.spin_direction = "forwards"
            elif game.opponent.spin_direction == "forwards":
                game.opponent.dog_normal.display(180, 440)
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
