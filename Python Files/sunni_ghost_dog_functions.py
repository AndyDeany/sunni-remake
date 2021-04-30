# Defining a function to decide which move the ghost dog is going to use
def choose_ghost_dog_move():
    if enemy_current_mana < 10:
        return "ghost dog teleport move"
    elif enemy_current_mana < 50:
        if enemy_current_hp <= 180:
            if character_current_hp <= 20:
                return "ghost dog glide move"
            elif character_current_hp <= 30:
                r = random.randint(1,10)
                if r == 1:
                    return "ghost dog heal move"
                elif r < 5:
                    return "ghost dog teleport move"
                else:
                    return "ghost dog glide move"
                
            elif enemy_current_hp < 25:
                r = random.randint(1,10)
                if r == 1:
                    return "ghost dog teleport move"
                if r == 2:
                    return "ghost dog glide move"
                else:
                    return "ghost dog heal move"
            else:                
                r = random.randint(1,3)
                if r == 1:
                    return "ghost dog heal move"
                elif r == 2:
                    return "ghost dog teleport move"
                elif r == 3:
                    return "ghost dog glide move"
                
        else:
            if character_current_hp <= 20:
                return "ghost dog glide move"
            elif character_current_hp <= 30:
                r = random.randint(1,9)
                if r < 4:
                    return "ghost dog teleport move"
                else:
                    return "ghost dog glide move"                
            else:                
                r = random.randint(1,2)
                if r == 1:
                    return "ghost dog teleport move"
                elif r == 2:
                    return "ghost dog glide move"

    elif enemy_current_mana <= 140:
        if enemy_current_hp <= 180:
            if character_current_hp <= 10:
                return "ghost dog claw move"
            elif character_current_hp <= 20:
                return "ghost dog glide move"
            elif character_current_hp <= 30:
                r = random.randint(1,20)
                if r == 1:
                    return "ghost dog heal move"
                elif r < 4:
                    return "ghost dog teleport move"
                elif r < 8:
                    return "ghost dog glide move"
                else:
                    return "ghost dog claw move"

            elif enemy_current_hp < 25:
                if character_current_hp <= 40:
                    r = random.randint(1,2)
                    if r == 1:
                        return "ghost dog claw move"
                    elif r == 2:
                        return "ghost dog heal move"
                else:
                    r == random.randint(1,20)
                    if r == 1:
                        return "ghost dog teleport move"
                    elif r == 2:
                        return "ghost dog glide move"
                    elif r == 3:
                        return "ghost dog claw move"
                    else:
                        return "ghost dog heal move"
            else:
                r = random.randint(1,4)
                if r == 1:
                    return "ghost dog heal move"
                elif r == 2:
                    return "ghost dog teleport move"
                elif r == 3:
                    return "ghost dog glide move"
                elif r == 4:
                    return "ghost dog claw move"

        else:
            if character_current_hp <= 10:
                return "ghost dog claw move"
            elif character_current_hp <= 20:
                return "ghost dog glide move"
            elif character_current_hp <= 30:
                r = random.randint(1,5)
                if r == 1:
                    return "ghost dog teleport move"
                elif r == 2:
                    return "ghost dog glide move"
                else:
                    return "ghost dog claw move"

            else:
                r = random.randint(1,3)
                if r == 1:
                    return "ghost dog teleport move"
                elif r == 2:
                    return "ghost dog glide move"
                elif r == 3:
                    return "ghost dog claw move"

    else:
        if enemy_current_hp <= 180:
            if character_current_hp <= 10:
                return "ghost dog claw move"
            elif character_current_hp <= 20:
                return "ghost dog glide move"
            elif character_current_hp <= 30:
                r = random.randint(1,15)
                if r == 1:
                    return "ghost dog heal move"
                elif r < 6:
                    return "ghost dog glide move"
                else:
                    return "ghost dog claw move"

            elif enemy_current_hp < 25:
                if character_current_hp <= 40:
                    r = random.randint(1,2)
                    if r == 1:
                        return "ghost dog claw move"
                    elif r == 2:
                        return "ghost dog heal move"
                else:
                    r == random.randint(1,20)
                    if r == 1:
                        return "ghost dog glide move"
                    elif r == 2:
                        return "ghost dog claw move"
                    else:
                        return "ghost dog heal move"
            else:
                r = random.randint(1,3)
                if r == 1:
                    return "ghost dog heal move"
                elif r == 2:
                    return "ghost dog glide move"
                elif r == 3:
                    return "ghost dog claw move"

        else:
            if character_current_hp <= 10:
                return "ghost dog claw move"
            elif character_current_hp <= 20:
                return "ghost dog glide move"
            elif character_current_hp <= 30:
                r = random.randint(1,4)
                if r == 1:
                    return "ghost dog glide move"
                else:
                    return "ghost dog claw move"

            else:
                r = random.randint(1,2)
                if r == 1:
                    return "ghost dog glide move"
                elif r == 2:
                    return "ghost dog claw move"       
        
# Defining a function to change the ghost dog's mana
def ghost_dog_change_mana(enemy_current_mana,ghost_dog_next_move):
    if ghost_dog_next_move == "ghost dog heal move":
        return enemy_current_mana - 10
    if ghost_dog_next_move == "ghost dog glide move":
        return enemy_current_mana - 10
    if ghost_dog_next_move == "ghost dog teleport move":
        return enemy_current_mana + 10
    if ghost_dog_next_move == "ghost dog claw move":
        return enemy_current_mana - 50

# Defining a function to play a sound when the ghost dog uses it's glide move
def glide_move_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_ghost_dog_glide.ogg")
    pygame.mixer.music.set_volume(volume_multiplier)
    pygame.mixer.music.play(0)

# Defining a function to play a sound when the ghost dog uses it's teleport move
def teleport_move_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_ghost_dog_teleport.ogg")
    pygame.mixer.music.set_volume(volume_multiplier)
    pygame.mixer.music.play(0)

# Defining a function to play a sound when the ghost dog uses it's claw move
def claw_move_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_ghost_dog_claw.ogg")
    pygame.mixer.music.set_volume(volume_multiplier)
    pygame.mixer.music.play(0)
