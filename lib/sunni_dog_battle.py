import random

from lib.sunni_core_functions import *


def dog_battle_display(game, victory_overlay, continue_button, return_to_title_button,
                       defeat_overlay, try_again_button):
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

        if game.mouse.is_in(960, 390, 1000, 430):
            game.player.MOVE_KICK.info.display(930, 130)
        elif game.mouse.is_in(1010, 390, 1050, 430):
            game.player.MOVE_HEADBUTT.info.display(930, 130)
        elif game.mouse.is_in(1060, 390, 1100, 430):
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
    elif game.current == game.player.MOVE_HEAL:
        game.battle.active_character.MOVE_HEAL.run()
    elif game.current == game.player.MOVE_KICK:
        game.battle.active_character.MOVE_KICK.run()
    elif game.current == game.player.MOVE_HEADBUTT:
        game.battle.active_character.MOVE_HEADBUTT.run()
    elif game.current == game.player.MOVE_FROSTBEAM:
        game.battle.active_character.MOVE_FROSTBEAM.run()

    # Dog moves
    elif game.current == game.opponent.MOVE_BARK:
        game.battle.active_character.MOVE_BARK.run()
    elif game.current == game.opponent.MOVE_HEAL:
        game.battle.active_character.MOVE_HEAL.run()
    elif game.current == game.opponent.MOVE_BITE:
        game.current.run()
    elif game.current == game.opponent.MOVE_SPIN:
        game.current.run()

    game.player.display_stat_change()
    game.opponent.display_stat_change()
