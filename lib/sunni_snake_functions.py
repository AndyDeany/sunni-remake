# Defining a function to decide which move the snake is going to use
def choose_snake_move():
    if enemy_current_mana < 10:
        return "snake confuse move"
    elif enemy_current_mana < 20:
        if enemy_current_hp <= 100:
            r = random.randint(1,2)
            if r == 1:
                return "snake heal move"
            elif r == 2:
                return "snake confuse move"
        else:
            return "snake confuse move"
    else:
        if character_current_hp < 20:
            if enemy_current_mana < 40:
                return "snake venom move"
            else:
                r = random.randint(1,2)
                if r == 1:
                    return "snake venom move"
                elif r == 2:
                    return "snake laser move"

        elif enemy_current_hp < 25:
            if enemy_current_mana > 110:
                r = random.randint(1,20)
                if r == 1:
                    return "snake venom move"
                elif r == 2:
                    return "snake laser move"
                else:
                    return "snake heal move"

            elif enemy_current_mana < 40:
                r = random.randint(1,20)
                if r == 1:
                    return "snake confuse move"
                elif r == 2:
                    return "snake venom move"
                else:
                    return "snake heal move"

            else:
                r = random.randint(1,30)
                if r == 1:
                    return "snake confuse move"
                elif r == 2:
                    return "snake venom move"
                elif r == 3:                
                    return "snake laser move"
                else:
                    return "snake heal move"

        elif enemy_current_hp > 3*(enemy_max_hp/4):
        
            if enemy_current_mana < 40:
                r = random.randint(1,2)
                if r == 1:
                    return "snake confuse move"
                elif r == 2:
                    return "snake venom move"

            elif enemy_current_mana > 110:
                r = random.randint(1,2)
                if r == 1:
                    return "snake venom move"
                elif r == 2:
                    return "snake laser move"

            else:
                r = random.randint(1,3)
                if r == 1:
                    return "snake confuse move"
                elif r == 2:
                    return "snake venom move"
                elif r == 3:
                    return "snake laser move"
            
        else:
            if enemy_current_mana < 40:
                r = random.randint(1,3)
                if r == 1:
                    return "snake heal move"
                elif r == 2:
                    return "snake confuse move"
                elif r == 3:
                    return "snake venom move"

            elif enemy_current_mana > 90:
                r = random.randint(1,3)
                if r == 1:
                    return "snake heal move"
                elif r == 2:
                    return "snake venom move"
                elif r == 3:
                    return "snake laser move"

            else:
                r = random.randint(1,4)
                if r == 1:
                    return "snake heal move"
                elif r == 2:
                    return "snake confuse move"
                elif r == 3:
                    return "snake venom move"
                elif r == 4:
                    return "snake laser move"



# Defining a function to play a sound when the snake uses it's laser move
def laser_move_sound():
    pygame.mixer.music.load(file_directory + "Sound Files\sunni_snake_laser.ogg")
    pygame.mixer.music.set_volume(0.5*volume_multiplier)
    pygame.mixer.music.play(0)
