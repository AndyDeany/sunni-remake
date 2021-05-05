from lib.game import Game
from lib.image import Image


game = Game()

opacity = 10    # Variable showing opacity of fading overlay for fading in/out
fade_direction = "out"
load_file = False

# Snake
snake_laser_beam = Image("sunni_snake_laser_beam.png")
snake_venom_beam = Image("sunni_snake_venom_beam.png")

# Ghost Dog
ghost_dog_dead = Image("sunni_ghost_dog_dead.png")
ghost_dog_glow1 = Image("sunni_ghost_dog_glow1.png")
ghost_dog_glow2 = Image("sunni_ghost_dog_glow2.png")
ghost_dog_glow3 = Image("sunni_ghost_dog_glow3.png")
ghost_dog_glow4 = Image("sunni_ghost_dog_glow4.png")
ghost_dog_glow5 = Image("sunni_ghost_dog_glow5.png")

ghost_dog_top_claw_swipe1 = Image("sunni_ghost_dog_top_claw_swipe1.png")
ghost_dog_top_claw_swipe2 = Image("sunni_ghost_dog_top_claw_swipe2.png")
ghost_dog_top_claw_swipe3 = Image("sunni_ghost_dog_top_claw_swipe3.png")
ghost_dog_top_claw_swipe4 = Image("sunni_ghost_dog_top_claw_swipe4.png")
ghost_dog_top_claw_swipe5 = Image("sunni_ghost_dog_top_claw_swipe5.png")
ghost_dog_top_claw_size1 = Image("sunni_ghost_dog_top_claw_size1.png")
ghost_dog_top_claw_size2 = Image("sunni_ghost_dog_top_claw_size2.png")
ghost_dog_top_claw_size3 = Image("sunni_ghost_dog_top_claw_size3.png")
ghost_dog_top_claw_size4 = Image("sunni_ghost_dog_top_claw_size4.png")
ghost_dog_top_claw_size5 = Image("sunni_ghost_dog_top_claw_size5.png")
ghost_dog_top_claw_size6 = Image("sunni_ghost_dog_top_claw_size6.png")
ghost_dog_top_claw_size7 = Image("sunni_ghost_dog_top_claw_size7.png")
ghost_dog_top_claw_size8 = Image("sunni_ghost_dog_top_claw_size8.png")
ghost_dog_top_claw_fade20 = Image("sunni_ghost_dog_top_claw_fade20.png")
ghost_dog_top_claw_fade40 = Image("sunni_ghost_dog_top_claw_fade40.png")
ghost_dog_top_claw_fade60 = Image("sunni_ghost_dog_top_claw_fade60.png")
ghost_dog_top_claw_fade80 = Image("sunni_ghost_dog_top_claw_fade80.png")

ghost_dog_side_claw_swipe1 = Image("sunni_ghost_dog_side_claw_swipe1.png")
ghost_dog_side_claw_swipe2 = Image("sunni_ghost_dog_side_claw_swipe2.png")
ghost_dog_side_claw_swipe3 = Image("sunni_ghost_dog_side_claw_swipe3.png")
ghost_dog_side_claw_swipe4 = Image("sunni_ghost_dog_side_claw_swipe4.png")
ghost_dog_side_claw_swipe5 = Image("sunni_ghost_dog_side_claw_swipe5.png")
ghost_dog_side_claw_size1 = Image("sunni_ghost_dog_side_claw_size1.png")
ghost_dog_side_claw_size2 = Image("sunni_ghost_dog_side_claw_size2.png")
ghost_dog_side_claw_size3 = Image("sunni_ghost_dog_side_claw_size3.png")
ghost_dog_side_claw_size4 = Image("sunni_ghost_dog_side_claw_size4.png")
ghost_dog_side_claw_size5 = Image("sunni_ghost_dog_side_claw_size5.png")
ghost_dog_side_claw_size6 = Image("sunni_ghost_dog_side_claw_size6.png")
ghost_dog_side_claw_size7 = Image("sunni_ghost_dog_side_claw_size7.png")
ghost_dog_side_claw_size8 = Image("sunni_ghost_dog_side_claw_size8.png")
ghost_dog_side_claw_fade20 = Image("sunni_ghost_dog_side_claw_fade20.png")
ghost_dog_side_claw_fade40 = Image("sunni_ghost_dog_side_claw_fade40.png")
ghost_dog_side_claw_fade60 = Image("sunni_ghost_dog_side_claw_fade60.png")
ghost_dog_side_claw_fade80 = Image("sunni_ghost_dog_side_claw_fade80.png")


game.loop()
