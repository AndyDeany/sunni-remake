import random

from lib.sunni_core_functions import *
from lib.sunni_dog_functions import *
from lib.color import Color


def dog_battle_display(game, left, mouse_x, mouse_y, kick_move_icon_faded,
                       headbutt_move_icon_faded, frostbeam_move_icon_faded, heal_move_icon_faded, kick_move_icon_solid,
                       headbutt_move_icon_solid, frostbeam_move_icon_solid, heal_move_icon_solid, kick_move_info,
                       headbutt_move_info, frostbeam_move_info, heal_move_info, victory_overlay,
                       continue_button, return_to_title_button, character_dead, defeat_overlay, try_again_button,
                       heal_heart, character_normal, character_tilt_left, character_tilt_right,
                       character_headbutt_stance, character_frostbeam_stance, frostbeam_start, frostbeam_middle):
    # Default battle screen, where the player chooses which move to use
    if game.current == "choose ability":
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
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

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
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_dead, (930,440))
        game.screen.blit(victory_overlay, (0,0))
        game.screen.blit(continue_button, (1000,600))
        game.screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

        if left and not game.display_options:
            if mousein(mouse_x, mouse_y, 1000,600,1120,650):
                game.current = "choose ability"
                game.player.level_up()
                game.load_opponent("Kanye Snake")
                game.save()
            elif mousein(mouse_x, mouse_y, 80,600,268,650):
                game.player.level_up()
                game.load_opponent("Kanye Snake")
                game.save()
                game.current = "title"

    # Character dead/Defeat screen
    elif game.current == "character dead":
        game.screen.blit(character_dead, (150,480))
        game.screen.blit(game.opponent.dog_normal, (930,440))
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

    # Character moves
    # Character heal move animation
    elif game.current == "heal move":
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

        if game.player.heal_heart_y < 350:
            if game.player.heal_heart_y == 170:
                game.player.heal_move_sound()
            game.screen.blit(heal_heart, (160,game.player.heal_heart_y))
            game.player.heal_heart_y += 5

        else:
            if not game.player.game.player.healed_already:
                healed_by = random.randint(5,15)
                if game.player.current_hp + healed_by > game.player.max_hp:
                    healed_by = game.player.max_hp - game.player.current_hp
                game.player.current_hp += healed_by
                game.player.stat_change_text = game.font.render("+" + str(healed_by), True, Color.HEAL_GREEN)
                game.player.trigger_stat_change_text()
                game.player.heal_heart_y = 170
                game.player.healed_already = True

    # Character kick move animation
    elif game.current == "kick move":
        game.screen.blit(game.opponent.dog_normal, (930,440))

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
                    game.player.attack_sound()

            elif game.player.kick_x == 870:
                game.screen.blit(character_tilt_left, (870,380))
                kick_damage = random.randint(8,12)
                if game.opponent.current_hp - kick_damage < 0:
                    kick_damage = game.opponent.current_hp
                game.opponent.current_hp -= kick_damage
                game.opponent.stat_change_text = game.font.render("-" + str(kick_damage), True, Color.DAMAGE_RED)
                game.opponent.trigger_stat_change_text()
                game.player.kick_x -= 36
                game.advancing = False

        elif not game.advancing:
            if game.player.kick_x > 150:
                game.player.stage = idle_movement(game, 20,game.player.kick_x,380)
                game.player.kick_x -= 36
            else:
                # Resetting variables for next time
                game.advancing = True
                game.player.kick_x = 150
                game.player.tilt_direction = "left"
                if game.opponent.current_hp == 0:
                    game.current = "dog dead"
                else:
                    dog_next_move = game.opponent.choose_move()
                    game.opponent.current_mana = game.opponent.change_mana(dog_next_move)
                    game.current = dog_next_move

    # Character headbutt move animation
    elif game.current == "headbutt move":
        game.screen.blit(game.opponent.dog_normal, (930,440))

        if game.advancing:
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
                headbutt_damage = random.randint(10,20)
                if game.opponent.current_hp - headbutt_damage < 0:
                    headbutt_damage = game.opponent.current_hp
                game.opponent.current_hp -= headbutt_damage
                game.opponent.stat_change_text = game.font.render("-" + str(headbutt_damage), True, Color.DAMAGE_RED)
                game.opponent.trigger_stat_change_text()
                game.player.headbutt_x -= 36
                game.advancing = False

        elif not game.advancing:
            if game.player.headbutt_x > 150:
                game.player.stage = idle_movement(game, 20,game.player.headbutt_x,380)
                game.player.headbutt_x -= 36
            else:
                # Resetting variables for next time
                game.advancing = True
                game.player.headbutt_x = 150
                if game.opponent.current_hp == 0:
                    game.current = "dog dead"
                else:
                    dog_next_move = game.opponent.choose_move()
                    game.opponent.current_mana = game.opponent.change_mana(dog_next_move)
                    game.current = dog_next_move

    # Character frostbeam move animation
    elif game.current == "frostbeam move":
        game.screen.blit(game.opponent.dog_normal, (930,440))
        game.screen.blit(character_frostbeam_stance, (150,380))

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                game.player.frostbeam_move_sound()
            elif game.duration_time == game.fps:
                frostbeam_damage = random.randint(15,30)
                if game.opponent.current_hp - frostbeam_damage < 0:
                    frostbeam_damage = game.opponent.current_hp
                game.opponent.current_hp -= frostbeam_damage
                game.opponent.stat_change_text = game.font.render("-" + str(frostbeam_damage), True, Color.DAMAGE_RED)
                game.opponent.trigger_stat_change_text()

            game.screen.blit(frostbeam_start, (215,381))
            for x in range(14):
                game.screen.blit(frostbeam_middle, (265+50*x,383+2*x))
            game.duration_time += 1

        else:
            # Resetting variables for next time
            game.duration_time = 0
            if game.opponent.current_hp == 0:
                game.current = "dog dead"
            else:
                dog_next_move = game.opponent.choose_move()
                game.opponent.current_mana = game.opponent.change_mana(dog_next_move)
                game.current = dog_next_move

    # Dog moves
    # Dog bark move animation
    elif game.current == "dog bark move":
        game.player.stage = idle_movement(game, 20,150,380)

        if game.duration_time < 2*game.fps:
            if game.duration_time == 0:
                game.opponent.attack_sound()
            elif game.duration_time == 2*(game.fps/3):
                game.opponent.attack_sound()
            elif game.duration_time == game.fps:
                dog_bark_damage = random.randint(5,20)
                if game.player.current_hp - dog_bark_damage < 0:
                    dog_bark_damage = game.player.current_hp
                game.player.current_hp -= dog_bark_damage
                game.player.stat_change_text = game.font.render("-" + str(dog_bark_damage), True, Color.DAMAGE_RED)
                game.player.trigger_stat_change_text()

            game.screen.blit(game.opponent.dog_bark_stance, (930,440))
            game.duration_time += 1

        else:
            # Resetting variables for next time
            game.duration_time = 0
            if game.player.current_hp == 0:
                game.current = "character dead"
            else:
                game.current = "choose ability"

    # Dog heal move animation
    elif game.current == "dog heal move":
        game.player.stage = idle_movement(game, 20,150,380)
        game.screen.blit(game.opponent.dog_normal, (930,440))

        if game.opponent.heal_heart_y < 410:
            if game.opponent.heal_heart_y == 230:
                game.player.heal_move_sound()
            game.screen.blit(heal_heart, (1005,game.opponent.heal_heart_y))
            game.opponent.heal_heart_y += 5

        else:
            if not game.player.healed_already:
                healed_by = random.randint(5,15)
                if game.opponent.current_hp + healed_by > game.opponent.max_hp:
                    healed_by = game.opponent.max_hp - game.opponent.current_hp
                game.opponent.current_hp += healed_by
                game.opponent.stat_change_text = game.font.render("+" + str(healed_by), True, Color.HEAL_GREEN)
                game.player.healed_already = True

            if game.duration_time < game.fps/2:
                game.opponent.display_stat_change()
                game.duration_time += 1
            else:
                # Resetting variables for next time
                game.opponent.heal_heart_y = 170
                game.opponent.reset_display_stat_y()
                game.duration_time = 0
                game.player.healed_already = False
                game.current = "choose ability"

    # Dog bite move animation
    elif game.current == "dog bite move":
        game.player.stage = idle_movement(game, 20,150,380)

        if game.advancing:
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
                bite_damage = random.randint(10,20)
                if game.player.current_hp - bite_damage < 0:
                    bite_damage = game.player.current_hp
                game.player.current_hp -= bite_damage
                game.player.stat_change_text = game.font.render("-" + str(bite_damage), True, Color.DAMAGE_RED)
                game.player.trigger_stat_change_text()
                game.opponent.bite_x += 42
                game.advancing = False

        elif not game.advancing:
            if game.opponent.bite_x < 930:
                game.screen.blit(game.opponent.dog_backwards, (game.opponent.bite_x,440))
                game.opponent.bite_x += 42
            else:
                # Resetting variables for next time
                game.advancing = True
                game.opponent.bite_x = 930
                if game.player.current_hp == 0:
                    game.current = "character dead"
                else:
                    game.current = "choose ability"

    # Dog spin move animation
    elif game.current == "dog spin move":
        game.player.stage = idle_movement(game, 20,150,380)

        if game.advancing:
            if game.opponent.spin_x == 930:
                game.screen.blit(game.opponent.dog_normal, (930,440))
                game.opponent.spin_x -= 25
            elif game.opponent.spin_x > 180:
                game.screen.blit(game.opponent.dog_normal, (game.opponent.spin_x,440))
                game.opponent.spin_x -= 25
            elif game.opponent.spin_x == 180:
                game.screen.blit(game.opponent.dog_normal, (180,440))
                game.opponent.spin_time = 0
                game.advancing = False
                game.opponent.attack_sound()

        elif game.retreating:
            if game.opponent.spin_x < 930:
                game.screen.blit(game.opponent.dog_backwards, (game.opponent.spin_x,440))
                game.opponent.spin_x += 30
            else:
                game.advancing = True
                game.retreating = False
                game.opponent.spin_x = 930
                if game.player.current_hp == 0:
                    game.current = "character dead"
                else:
                    game.current = "choose ability"

        if game.opponent.spin_time < game.fps:
            if game.opponent.spin_time == 15:
                spin_damage = random.randint(10,30)
                if game.player.current_hp - spin_damage < 0:
                    spin_damage = game.player.current_hp
                game.player.current_hp -= spin_damage
                game.player.stat_change_text = game.font.render("-" + str(spin_damage), True, Color.DAMAGE_RED)
                game.player.trigger_stat_change_text()
            if game.opponent.spin_direction == "backwards":
                game.screen.blit(game.opponent.dog_backwards, (180,440))
                game.opponent.spin_direction = "forwards"
            elif game.opponent.spin_direction == "forwards":
                game.screen.blit(game.opponent.dog_normal, (180,440))
                game.opponent.spin_direction = "backwards"
            game.opponent.spin_time += 1
            if game.opponent.spin_time == game.fps-1:
                game.retreating = True
        else:
            game.opponent.spin_time = game.fps

    if game.player.display_stat_change_time > 0:
        game.player.display_stat_change()
        game.player.display_stat_change_time -= 1
    else:
        game.player.reset_display_stat_y()
        if game.current == "heal move":
            game.player.healed_already = False
            dog_next_move = game.opponent.choose_move()
            game.opponent.current_mana = game.opponent.change_mana(dog_next_move)
            game.current = dog_next_move

    if game.opponent.display_stat_change_time > 0:
        game.opponent.display_stat_change()
        game.opponent.display_stat_change_time -= 1
    else:
        game.opponent.reset_display_stat_y()

    # DOG BATTLE - END
