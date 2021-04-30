# Defining a function to decide which move the dog is going to use
def choose_dog_move():
    if character_current_hp < 15:
        if enemy_current_mana < 15:
            return "dog bark move"

        elif enemy_current_mana < 25:
            r = random.randint(1,2)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog bite move"
        
        elif enemy_current_mana > 90:            
            r = random.randint(1,2)
            if r == 1:
                return "dog bite move"
            elif r == 2:
                return "dog spin move"
            
        else:
            r = random.randint(1,3)        
            if r == 1:
                return "dog bite move"
            elif r == 2:
                return "dog spin move"
            elif r == 3:                
                return "dog bark move"
            
    elif enemy_current_hp < enemy_max_hp/4:
        if enemy_current_mana < 10:
            return "dog bark move"

        elif enemy_current_mana > 90:
            r = random.randint(1,20)
            if r == 1:
                return "dog bite move"
            elif r == 2:
                return "dog spin move"
            else:
                return "dog heal move"

        elif enemy_current_mana < 15:
            r = random.randint(1,10)
            if r == 1:
                return "dog bark move"
            else:
                return "dog heal move"

        elif enemy_current_mana < 25:
            r = random.randint(1,20)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog bite move"
            else:
                return "dog heal move"

        else:
            r = random.randint(1,30)
            if r == 1:
                return "dog bite move"
            elif r == 2:
                return "dog spin move"
            elif r == 3:                
                return "dog bark move"
            else:
                return "dog heal move"

    elif enemy_current_hp > 3*(enemy_max_hp/4):
        if enemy_current_mana < 10:
            return "dog bark move"

        elif enemy_current_mana < 25:
            r = random.randint(1,2)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog bite move"

        elif enemy_current_mana > 90:
            r = random.randint(1,2)
            if r == 1:
                return "dog bite move"
            elif r == 2:
                return "dog spin move"

        else:
            r = random.randint(1,3)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog bite move"
            elif r == 3:
                return "dog spin move"

    else:
        if enemy_current_mana < 10:
            return "dog bark move"

        elif enemy_current_mana < 15:
            r = random.randint(1,2)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog heal move"

        elif enemy_current_mana < 25:
            r = random.randint(1,3)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog heal move"
            elif r == 3:
                return "dog bite move"

        elif enemy_current_mana > 90:
            r = random.randint(1,3)
            if r == 1:
                return "dog heal move"
            elif r == 2:
                return "dog bite move"
            elif r == 3:
                return "dog spin move"

        else:
            r = random.randint(1,4)
            if r == 1:
                return "dog bark move"
            elif r == 2:
                return "dog heal move"
            elif r == 3:
                return "dog bite move"
            elif r == 4:
                return "dog spin move"

# Defining a function to change the dog's mana
def dog_change_mana(enemy_current_mana,dog_next_move):
    if dog_next_move == "dog bark move":
        return enemy_current_mana + 10
    elif dog_next_move == "dog heal move":
        return enemy_current_mana - 10
    elif dog_next_move == "dog bite move":
        return enemy_current_mana - 15
    elif dog_next_move == "dog spin move":
        return enemy_current_mana - 25

# Defining a function to play a sound when the dog attacks
def dog_attack_sound():
    r = random.randint(1,3)
    if r == 1:
        pygame.mixer.music.load(file_directory + "Sound Files\sunni_dog_attack1.ogg")
        pygame.mixer.music.set_volume(volume_multiplier)
        pygame.mixer.music.play(0)
    elif r == 2:
        pygame.mixer.music.load(file_directory + "Sound Files\sunni_dog_attack2.ogg")
        pygame.mixer.music.set_volume(volume_multiplier)
        pygame.mixer.music.play(0)
    elif r == 3:
        pygame.mixer.music.load(file_directory + "Sound Files\sunni_dog_attack3.ogg")
        pygame.mixer.music.set_volume(volume_multiplier)
        pygame.mixer.music.play(0)
