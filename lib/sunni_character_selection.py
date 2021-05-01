# Choose your character screen
screen.blit(choose_character_overlay, (0,0))
screen.blit(character_choice1, (400,300))
screen.blit(character_choice2, (810,300))

if left and not display_options:
    if mousein(400,300,470,480):
        character = "character1"
        character_normal = pygame.image.load(file_directory + "Image Files\sunni_character1_normal1.png").convert_alpha()
        character_backwards = pygame.image.load(file_directory + "Image Files\sunni_character1_backwards.png").convert_alpha()
        character_scared = pygame.image.load(file_directory + "Image Files\sunni_character1_scared.png").convert_alpha()
        character_scared_redflash = pygame.image.load(file_directory + "Image Files\sunni_character1_scared_redflash.png").convert_alpha()
        character_tilt_left = pygame.image.load(file_directory + "Image Files\sunni_character1_tilt_left.png").convert_alpha()
        character_tilt_right = pygame.image.load(file_directory + "Image Files\sunni_character1_tilt_right.png").convert_alpha()
        character_dead = pygame.image.load(file_directory + "Image Files\sunni_character1_dead.png").convert_alpha()
        character_headbutt_stance = pygame.image.load(file_directory + "Image Files\sunni_character1_tilt_right.png").convert_alpha()
        character_frostbeam_stance = pygame.image.load(file_directory + "Image Files\sunni_character1_frostbeam_stance.png").convert_alpha()
        
    elif mousein(810,300,880,480):
        character = "character2"
        character_normal = pygame.image.load(file_directory + "Image Files\sunni_character2_normal1.png").convert_alpha()
        character_backwards = pygame.image.load(file_directory + "Image Files\sunni_character2_backwards.png").convert_alpha()
        character_scared = pygame.image.load(file_directory + "Image Files\sunni_character2_normal1.png").convert_alpha()
        character_scared_redflash = pygame.image.load(file_directory + "Image Files\sunni_character2_scared_redflash.png").convert_alpha()
        character_tilt_left = pygame.image.load(file_directory + "Image Files\sunni_character2_tilt_left.png").convert_alpha()
        character_tilt_right = pygame.image.load(file_directory + "Image Files\sunni_character2_tilt_right.png").convert_alpha()
        character_dead = pygame.image.load(file_directory + "Image Files\sunni_character2_dead.png").convert_alpha()
        character_headbutt_stance = pygame.image.load(file_directory + "Image Files\sunni_character2_headbutt_stance.png").convert_alpha()
        character_frostbeam_stance = pygame.image.load(file_directory + "Image Files\sunni_character2_frostbeam_stance.png").convert_alpha()

    character_max_hp = 90 + 10*int(character_level)
    character_current_hp = 90 + 10*int(character_level)
    character_max_mana = 95 + 5*int(character_level)
    character_current_mana = 95 + 5*int(character_level)
    
    if mousein(400,300,470,480) or mousein(810,300,880,480):
        enemy_max_hp, enemy_current_hp, enemy_max_mana, enemy_current_mana, current = assign_enemy_stats(opponent_name)

