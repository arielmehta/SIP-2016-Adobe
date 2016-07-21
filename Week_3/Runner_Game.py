

import pygame
import random
from city_scroller_template_meera import Scroller 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
YELLOW = (210, 215, 57)
colors = [BLACK, GREY, WHITE]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Loop until the user clicks the close button.
done = False

# Set the title of the window
pygame.display.set_caption("CityScroller")

clock = pygame.time.Clock()

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)


front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, BACK_SCROLLER_COLOR, -3)
middle_scroller = Scroller(SCREEN_WIDTH, 30, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, -2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), FRONT_SCROLLER_COLOR, -1)


back_scroller.add_buildings()

middle_scroller.add_buildings()

front_scroller.add_buildings()
# ------- RUNNER SPRITE CLASSES-------- #
class Runner_Sprite (pygame.sprite.Sprite):
    def __init__(self, color, size, position):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = size
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.position = position
        self.rect = self.image.get_rect(center = self.position)

    def update (self, speed):
        pygame.rect.move(100 + speed, 450)
        if 

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
    screen.fill(GREY)
    mouse_pos = pygame.mouse.get_pos()

    # --- Drawing code should go here
    all_sprites_list = pygame.sprite.Group()
    player_1 = Runner_Sprite(RED, 50, mouse_pos)
    good_sprite = Runner_Sprite(GREEN, 50, (100,450))

    all_sprites_list.add(player_1)
    all_sprites_list.add(good_sprite)

    good_sprite.update(5)
    

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    
    front_scroller.draw_buildings()
    front_scroller.move_buildings()


    
    

    pygame.draw.rect(screen, BLACK, (0, 450, SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, (0, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (100, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (200, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (300, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (400, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (500, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (600, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (700, 525, 50, 5))
    pygame.draw.rect(screen, WHITE, (795, 525, 50, 5))

    pygame.draw.circle(screen, YELLOW , (60,60), 50)
    pygame.draw.circle(screen, GREY , (90,90), 50)

    pygame.draw.circle(screen, WHITE , (200,90), 30)
    pygame.draw.circle(screen, WHITE , (225,90), 30)
    pygame.draw.circle(screen, WHITE , (240,90), 30)
    pygame.draw.circle(screen, WHITE , (265,90), 30)
    pygame.draw.circle(screen, WHITE , (280,90), 30)

    pygame.draw.circle(screen, WHITE , (300,70), 30)
    pygame.draw.circle(screen, WHITE , (325,70), 30)
    pygame.draw.circle(screen, WHITE , (340,70), 30)
    pygame.draw.circle(screen, WHITE , (365,70), 30)
    pygame.draw.circle(screen, WHITE , (380,70), 30)

    pygame.draw.circle(screen, WHITE , (500,70), 35)
    pygame.draw.circle(screen, WHITE , (525,70), 35)
    pygame.draw.circle(screen, WHITE , (540,70), 35)
    pygame.draw.circle(screen, WHITE , (565,70), 35)
    pygame.draw.circle(screen, WHITE , (580,70), 35)

    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
