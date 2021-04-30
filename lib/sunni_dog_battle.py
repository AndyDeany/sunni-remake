import random

from lib.sunni_core_functions import *
from lib.sunni_dog_functions import *
from lib.color import Color


def dog_battle_display(game, left, mouse_x, mouse_y, dog_normal, kick_move_icon_faded,
                       headbutt_move_icon_faded, frostbeam_move_icon_faded, heal_move_icon_faded, kick_move_icon_solid,
                       headbutt_move_icon_solid, frostbeam_move_icon_solid, heal_move_icon_solid, kick_move_info,
                       headbutt_move_info, frostbeam_move_info, heal_move_info, dog_dead, victory_overlay,
                       continue_button, return_to_title_button, character_dead, defeat_overlay, try_again_button,
                       heal_heart, character_normal, character_tilt_left, character_tilt_right,
                       character_headbutt_stance, character_frostbeam_stance, frostbeam_start, frostbeam_middle,
                       dog_bark_stance):
    # Default battle screen, where the player chooses which move to use
    if game.game.current == "choose ability":
        game.player.stage = idle_movement(game.player.stage,game.game.player_number,20,150,380)
        game.game.screen.blit(dog_normal, (930,440))

        if mousein(mouse_x, mouse_y, 960,430,1100,540):
            game.game.screen.blit(kick_move_icon_faded, (960,390))
            game.game.screen.blit(headbutt_move_icon_faded, (1010,390))
            game.game.screen.blit(frostbeam_move_icon_faded, (1060,390))

            if left and not game.display_options:
                game.current = "aggressive moves"

        elif mousein(mouse_x, mouse_y, 135,380,235,520):
            game.game.screen.blit(heal_move_icon_faded, (165,330))

            if left and not game.display_options:
                game.current = "defensive moves"

    # Screen showing the player their aggressive move options
    elif game.game.current == "aggressive moves":
        game.player.stage = idle_movement(game.player.stage, game.game.player_number, 20, 150, 380)
        game.game.screen.blit(dog_normal, (930,440))

        game.game.screen.blit(kick_move_icon_solid, (960,390))
        game.game.screen.blit(headbutt_move_icon_solid, (1010,390))
        game.game.screen.blit(frostbeam_move_icon_solid, (1060,390))

        if mousein(mouse_x, mouse_y, 960,390,1000,430):
            game.game.screen.blit(kick_move_info, (930,130))
        elif mousein(mouse_x, mouse_y, 1010,390,1050,430):
            game.game.screen.blit(headbutt_move_info, (930,130))
        elif mousein(mouse_x, mouse_y, 1060,390,1100,430):
            game.game.screen.blit(frostbeam_move_info, (930,130))

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 960,390,1000,430):
                game.player.current_mana += 10
                if game.player.current_mana > game.player.max_mana:
                    game.player.current_mana = game.player.max_mana
                display_mana_notification_time = 2*game.fps
                game.current = "kick move"
            elif mousein(mouse_x, mouse_y, 1010,390,1050,430):
                if game.player.current_mana >= 20:
                    game.player.current_mana -= 20
                    display_mana_notification_time = 2*game.fps
                    game.current = "headbutt move"
                else:
                    display_mana_notification_time = 0
            elif mousein(mouse_x, mouse_y, 1060,390,1100,430):
                if game.player.current_mana >= 30:
                    game.player.current_mana -= 30
                    game.current = "frostbeam move"
                else:
                    display_mana_notification_time = 0
            elif not mousein(mouse_x, mouse_y, 930,380,1130,540):
                game.current = "choose ability"

    # Screen showing the player their defensive move options
    elif game.current == "defensive moves":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)
        game.screen.blit(dog_normal, (930,440))

        game.screen.blit(heal_move_icon_solid, (165,330))

        if mousein(mouse_x, mouse_y, 165,330,205,370):
            game.screen.blit(heal_move_info, (220,130))

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 165,330,205,370):
                if game.player.current_mana >= 10:
                    game.player.current_mana -= 10
                    display_mana_notification_time = 2*game.fps
                    game.current = "heal move"
                else:
                    display_mana_notification_time = 0
            elif not mousein(mouse_x, mouse_y, 150,320,220,560):
                game.current = "choose ability"

    # Dog dead/Victory screen
    elif game.current == "dog dead":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)
        game.screen.blit(dog_dead, (930,440))
        game.screen.blit(victory_overlay, (0,0))
        game.screen.blit(continue_button, (1000,600))
        game.screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 1000,600,1120,650):
                game.current = "choose ability"
                opponent_name = "Kanye Snake"
                game.player.level += 1
                game.player.max_hp = 90 + 10*int(game.player.level)
                game.player.current_hp = 90 + 10*int(game.player.level)
                game.player.max_mana = 95 + 5*int(game.player.level)
                game.player.current_mana = 95 + 5*int(game.player.level)
                game.opponent.max_hp = 120
                game.opponent.current_hp = 120
                game.opponent.max_mana = 120
                game.opponent.current_mana = 120
                game.save()
            elif mousein(mouse_x, mouse_y, 80,600,268,650):
                game.player.level += 1
                opponent_name = "Kayne Snake"
                game.save()
                game.current = "title"

    # Character dead/Defeat screen
    elif game.current == "character dead":
        game.screen.blit(character_dead, (150,480))
        game.screen.blit(dog_normal, (930,440))
        game.screen.blit(defeat_overlay, (0,0))
        game.screen.blit(try_again_button, (1000,600))
        game.screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 1000,600,1200,700):
                game.current = "choose ability"
                game.player.level += 0.25
                game.player.max_hp = 90 + 10*int(game.player.level)
                game.player.current_hp = 90 + 10*int(game.player.level)
                game.player.max_mana = 95 + 5*int(game.player.level)
                game.player.current_mana = 95 + 5*int(game.player.level)
                game.opponent.max_hp = 100
                game.opponent.current_hp = 100
                game.opponent.max_mana = 100
                game.opponent.current_mana = 100
                game.save()
            elif mousein(mouse_x, mouse_y, 80,600,268,650):
                game.save()
                game.current = "title"

    ## Character moves

    # Character heal move animation
    elif game.current == "heal move":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)
        game.screen.blit(dog_normal, (930,440))

        if game.player.heal_heart_y < 350:
            if game.player.heal_heart_y == 170:
                heal_move_sound()
            game.screen.blit(heal_heart, (160,game.player.heal_heart_y))
            game.player.heal_heart_y += 5

        else:
            if not game.player.game.player.healed_already:
                healed_by = random.randint(5,15)
                if game.player.current_hp + healed_by > game.player.max_hp:
                    healed_by = game.player.max_hp - game.player.current_hp
                game.player.current_hp += healed_by
                display_healed = game.font.render("+" + str(healed_by), True, Color.HEAL_GREEN)
                game.player.healed_already = True

            if game.game.duration_time < game.fps/2:
                game.player.display_healed_y = display_stat_change(display_healed,170,game.player.game.player.display_healed_y)
                game.game.duration_time += 1
            else:
                # Resetting variables for next time
                game.player.heal_heart_y = 170
                game.player.display_healed_y = 360
                game.duration_time = 0
                game.player.healed_already = False
                dog_next_move = choose_dog_move()
                game.opponent.current_mana = dog_change_mana(game.opponent.current_mana,dog_next_move)
                game.current = dog_next_move

    # Character kick move animation
    elif game.current == "kick move":
        game.screen.blit(dog_normal, (930,440))

        if game.advancing:
            if game.player.kick_x == 150:
                game.screen.blit(character_normal, (150,380))
                game.player.kick_x += 24
            elif game.player.kick_x < 870:
                if game.player.tilt_direction == "left":
                    game.screen.blit(character_tilt_left, (game.player.kick_x,380))
                    game.player.tilt_direction = "right"
                elif game.player.tilt_direction == "right":
                    game.screen.blit(character_tilt_right, (game.player.kick_x,380))
                    game.player.tilt_direction =  "left"
                game.player.kick_x += 24
                if game.player.kick_x == 750:
                    character_attack_sound()

            elif game.player.kick_x == 870:
                game.screen.blit(character_tilt_left, (870,380))
                kick_damage = random.randint(8,12)
                if game.opponent.current_hp - kick_damage < 0:
                    kick_damage = game.opponent.current_hp
                game.opponent.current_hp -= kick_damage
                display_damage = game.font.render("-" + str(kick_damage), True, Color.DAMAGE_RED)
                display_damage_time = 0
                game.player.kick_x -= 36
                game.advancing = False

        elif not game.advancing:
            if game.player.kick_x > 150:
                game.player.stage = idle_movement(game.player.stage,game.player_number,20,game.player.kick_x,380)
                game.player.kick_x -= 36
            else:
                # Resetting variables for next time
                game.advancing = True
                game.player.kick_x = 150
                game.player.tilt_direction = "left"
                game.player.display_damage_y = 420
                if game.opponent.current_hp == 0:
                    game.current = "dog dead"
                else:
                    dog_next_move = choose_dog_move()
                    game.opponent.current_mana = dog_change_mana(game.opponent.current_mana,dog_next_move)
                    game.current = dog_next_move

        if display_damage_time < game.fps/2:     # Make this into a function in the future? if more battles are made (also for the heal one)
            game.player.display_damage_y = display_stat_change(display_damage,1015,game.player.display_damage_y)
            display_damage_time += 1
        else:
            display_damage_time = game.fps

    # Character headbutt move animation
    elif game.current == "headbutt move":
        game.screen.blit(dog_normal, (930,440))

        if game.advancing:
            if game.player.headbutt_x == 150:
                game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)
                game.player.headbutt_x += 24
            elif game.player.headbutt_x < 870:
                game.screen.blit(character_headbutt_stance, (game.player.headbutt_x,380))
                game.player.headbutt_x += 24
                if game.player.headbutt_x == 750:
                    character_attack_sound()

            elif game.player.headbutt_x == 870:
                game.screen.blit(character_headbutt_stance, (870,380))
                headbutt_damage = random.randint(10,20)
                if game.opponent.current_hp - headbutt_damage < 0:
                    headbutt_damage = game.opponent.current_hp
                game.opponent.current_hp -= headbutt_damage
                display_damage = game.font.render("-" + str(headbutt_damage), True, Color.DAMAGE_RED)
                display_damage_time = 0
                game.player.headbutt_x -= 36
                game.advancing = False

        elif not game.advancing:
            if game.player.headbutt_x > 150:
                game.player.stage = idle_movement(game.player.stage,game.player_number,20,game.player.headbutt_x,380)
                game.player.headbutt_x -= 36
            else:
                # Resetting variables for next time
                game.advancing = True
                game.player.headbutt_x = 150
                game.player.display_damage_y = 420
                if game.opponent.current_hp == 0:
                    game.current = "dog dead"
                else:
                    dog_next_move = choose_dog_move()
                    game.opponent.current_mana = dog_change_mana(game.opponent.current_mana,dog_next_move)
                    game.current = dog_next_move

        if display_damage_time < game.fps/2:
            game.player.display_damage_y = display_stat_change(display_damage,1015,game.player.display_damage_y)
            display_damage_time += 1
        else:
            display_damage_time = game.fps

    # Character frostbeam move animation
    elif game.current == "frostbeam move":
        game.screen.blit(dog_normal, (930,440))
        game.screen.blit(character_frostbeam_stance, (150,380))

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                frostbeam_move_sound()
            elif game.duration_time == game.fps:
                frostbeam_damage = random.randint(15,30)
                if game.opponent.current_hp - frostbeam_damage < 0:
                    frostbeam_damage = game.opponent.current_hp
                game.opponent.current_hp -= frostbeam_damage
                display_damage = game.font.render("-" + str(frostbeam_damage), True, Color.DAMAGE_RED)
                display_damage_time = 0

            game.screen.blit(frostbeam_start, (215,381))
            for x in range(14):
                game.screen.blit(frostbeam_middle, (265+50*x,383+2*x))
            game.duration_time += 1

        else:
            # Resetting variables for next time
            display_damage_time = game.fps
            game.duration_time = 0
            if game.opponent.current_hp == 0:
                    game.current = "dog dead"
            else:
                dog_next_move = choose_dog_move()
                game.opponent.current_mana = dog_change_mana(game.opponent.current_mana,dog_next_move)
                game.current = dog_next_move

        if display_damage_time < game.fps/2:
            game.player.display_damage_y = display_stat_change(display_damage,1015,game.player.display_damage_y)
            display_damage_time += 1

    ## Dog moves

    # Dog bark move animation
    elif game.current == "dog bark move":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                dog_attack_sound()
            elif game.duration_time == 2*(game.fps/3):
                dog_attack_sound()
            elif game.duration_time == game.fps:
                dog_bark_damage = random.randint(5,20)
                if game.player.current_hp - dog_bark_damage < 0:
                    dog_bark_damage = game.player.current_hp
                game.player.current_hp -= dog_bark_damage
                display_damage = game.font.render("-" + str(dog_bark_damage), True, Color.DAMAGE_RED)
                display_damage_time = 0

            game.screen.blit(dog_bark_stance, (930,440))
            game.duration_time += 1

        else:
            # Resetting variables for next time
            display_damage_time = game.fps
            game.duration_time = 0
            if game.player.current_hp == 0:
                game.current = "character dead"
            else:
                game.current = "choose ability"

        if display_damage_time < game.fps/2:
            game.player.character_display_damage_y = display_stat_change(display_damage,170,game.player.character_display_damage_y)
            display_damage_time += 1
        else:
            game.player.character_display_damage_y = 360
            display_damage_time = game.fps

    # Dog heal move animation
    elif game.current == "dog heal move":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)
        game.screen.blit(dog_normal, (930,440))

        if game.opponent.heal_heart_y < 410:
            if game.opponent.heal_heart_y == 230:
                heal_move_sound()
            game.screen.blit(heal_heart, (1005,game.opponent.heal_heart_y))
            game.opponent.heal_heart_y += 5

        else:
            if not game.player.healed_already:
                healed_by = random.randint(5,15)
                if game.opponent.current_hp + healed_by > game.opponent.max_hp:
                    healed_by = game.opponent.max_hp - game.opponent.current_hp
                game.opponent.current_hp += healed_by
                display_healed = game.font.render("+" + str(healed_by), True, Color.HEAL_GREEN)
                game.player.healed_already = True

            if game.duration_time < game.fps/2:
                game.player.display_healed_y = display_stat_change(display_healed,1015,game.player.display_healed_y)
                game.duration_time += 1
            else:
                # Resetting variables for next time
                game.opponent.heal_heart_y = 170
                game.player.display_healed_y = 360
                game.duration_time = 0
                game.player.healed_already = False
                game.current = "choose ability"

    # Dog bite move animation
    elif game.current == "dog bite move":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)

        if game.advancing:
            if game.opponent.game.opponent.dog_bite_x == 930:
                game.screen.blit(dog_normal, (930,440))
                game.opponent.game.opponent.dog_bite_x -= 24
            elif game.opponent.game.opponent.dog_bite_x > 90:
                game.screen.blit(dog_normal, (game.opponent.dog_bite_x,440))
                game.opponent.dog_bite_x -= 24
                if game.opponent.dog_bite_x == 330:
                    dog_attack_sound()

            elif game.opponent.dog_bite_x == 90:
                game.screen.blit(game.opponent.dog_backwards, (90,440))
                bite_damage = random.randint(10,20)
                if game.player.current_hp - bite_damage < 0:
                    bite_damage = game.player.current_hp
                game.player.current_hp -= bite_damage
                display_damage = game.font.render("-" + str(bite_damage), True, Color.DAMAGE_RED)
                display_damage_time = 0
                game.opponent.dog_bite_x += 42
                game.advancing = False

        elif not game.advancing:
            if game.opponent.dog_bite_x < 930:
                game.screen.blit(game.opponent.dog_backwards, (game.opponent.dog_bite_x,440))
                game.opponent.dog_bite_x += 42
            else:
                # Resetting variables for next time
                game.advancing = True
                game.opponent.dog_bite_x = 930
                if game.player.current_hp == 0:
                    game.current = "character dead"
                else:
                    game.current = "choose ability"

        if display_damage_time < game.fps/2:
            game.player.character_display_damage_y = display_stat_change(display_damage,170,game.player.character_display_damage_y)
            display_damage_time += 1
        else:
            game.player.character_display_damage_y = 360
            display_damage_time = game.fps

    # Dog spin move animation
    elif game.current == "dog spin move":
        game.player.stage = idle_movement(game.player.stage,game.player_number,20,150,380)

        if game.advancing:
            if game.dog_spin_x == 930:
                game.screen.blit(dog_normal, (930,440))
                game.dog_spin_x -= 25
            elif game.dog_spin_x > 180:
                game.screen.blit(dog_normal, (game.dog_spin_x,440))
                game.dog_spin_x -= 25
            elif game.dog_spin_x == 180:
                game.screen.blit(dog_normal, (180,440))
                dog_spin_time = 0
                game.advancing = False
                dog_attack_sound()

        elif game.retreating:
            if game.dog_spin_x < 930:
                game.screen.blit(game.opponent.dog_backwards, (game.dog_spin_x,440))
                game.dog_spin_x += 30
            else:
                game.advancing = True
                game.retreating = False
                game.dog_spin_x = 930
                if game.player.current_hp == 0:
                    game.current = "character dead"
                else:
                    game.current = "choose ability"

        if dog_spin_time < game.fps:
            if dog_spin_time == 15:
                spin_damage = random.randint(10,30)
                if game.player.current_hp - spin_damage < 0:
                    spin_damage = game.player.current_hp
                game.player.current_hp -= spin_damage
                display_damage = game.font.render("-" + str(spin_damage), True, Color.DAMAGE_RED)
                display_damage_time = 0
            if game.opponent.dog_spin_direction == "backwards":
                game.screen.blit(game.opponent.dog_backwards, (180,440))
                game.opponent.dog_spin_direction = "forwards"
            elif game.opponent.dog_spin_direction == "forwards":
                game.screen.blit(dog_normal, (180,440))
                game.opponent.dog_spin_direction = "backwards"
            dog_spin_time += 1
            if dog_spin_time == game.fps-1:
                game.retreating = True
        else:
            dog_spin_time = game.fps

        if display_damage_time < game.fps/2:
            game.player.character_display_damage_y = display_stat_change(display_damage,170,game.player.character_display_damage_y)
            display_damage_time += 1
        else:
            game.player.character_display_damage_y = 360
            display_damage_time = game.fps

    # DOG BATTLE - END
