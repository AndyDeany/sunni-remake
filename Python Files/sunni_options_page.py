if not options_just_selected:
    current_volume_display = opening_font.render("Volume Level: " + str(int(100*volume_multiplier)) + "%", True, MILD_BLUE)
    screen.blit(volume_plus_button, (490,250))
    screen.blit(volume_minus_button, (430,250))
    screen.blit(volume_mute_button, (570,250))
    screen.blit(windowed_button, (80,350))
    screen.blit(fullscreen_button, (250,350))                
    screen.blit(blank_overlay, (0,0))
    screen.blit(return_to_game_button, (10,665))
    if current not in ["choose character", "title"]:
        screen.blit(return_to_title_button, (1082,665))
    screen.blit(current_volume_display, (80,250))
    
    # Showing the buttons faded out if they cannot be clicked
    if volume_multiplier < 1:
        screen.blit(volume_plus_button, (490,250))
    if volume_multiplier > 0:
        screen.blit(volume_minus_button, (430,250))
    else:
        screen.blit(volume_mute_button, (570,250))
    if volume_multiplier == 0:
        volume_muted = True
    else:
        volume_muted = False
    if not fullscreen_enabled:
        screen.blit(windowed_button,(80,350))
    else:
        screen.blit(fullscreen_button,(250,350))
        
    # Returning to game
    if escape:
        display_options = False
    if left:                        
        if mousein(10,665,204,715):
            display_options = False
        # Returning to title
        elif mousein(1082,665,1270,715) and current not in ["choose character", "title"]: 
            savegame(save_number)   # An extra screen/window could come up asking the player which save file they wish to save the game on
            current = "title"
            pygame.mixer.music.load(file_directory + "Sound Files\sunni_title_screen_music.ogg")
            pygame.mixer.music.set_volume(0.1*volume_multiplier)
            if not music_playing:
                pygame.mixer.music.play(-1)
                music_playing = True
            display_options = False
            
        # Volume mute button
        elif mousein(570,250,620,300):# Volume mute button click area
            if not volume_muted:
                volume_muted = True
                withheld_volume = volume_multiplier
                volume_multiplier = 0
                pygame.mixer.music.set_volume(0)
            else:
                volume_muted = False
                volume_multiplier = withheld_volume
                if current == "title":
                    pygame.mixer.music.set_volume(0.1*volume_multiplier)
                elif current == "snake laser move" or "snake venom move":
                    pygame.mixer.music.set_volume(0.5*volume_multiplier)
                else:
                    pygame.mixer.music.set_volume(volume_multiplier)
                    
        # Setting to windowed or fullscreen
        elif mousein(80,350,220,400) and fullscreen_enabled:
            screen = pygame.display.set_mode(size)
            fullscreen_enabled = False
        elif mousein(250,350,390,400) and not fullscreen_enabled:
            screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
            fullscreen_enabled = True

    if left_held:
        # Changing volume on mouse clicks (and holds)
        if mousein(430,250,480,300):
            if volume_multiplier > 0:
                volume_multiplier -= 0.01
                if current == "title":
                    pygame.mixer.music.set_volume(0.1*volume_multiplier)
                elif current == "snake laser move" or "snake venom move":
                    pygame.mixer.music.set_volume(0.5*volume_multiplier)
                else:
                    pygame.mixer.music.set_volume(volume_multiplier)
            volume_muted = False
        elif mousein(490,250,540,300):
            if volume_multiplier < 1:
                volume_multiplier += 0.01
                if current == "title":
                    pygame.mixer.music.set_volume(0.1*volume_multiplier)
                elif current == "snake laser move" or "snake venom move":
                    pygame.mixer.music.set_volume(0.5*volume_multiplier)
                else:
                    pygame.mixer.music.set_volume(volume_multiplier) 
else:
    options_just_selected = False
