import pygame
import random 
pygame.init()

GREY = (129, 129, 129)
RED = (255, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Documentation")
clock = pygame.time.Clock()



done = False
position_list_x = []
position_list_y = []

screen.fill(GREY)
while not done:
    # --- Main event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

   
    
    if event.type == pygame.MOUSEBUTTONDOWN:
    	position = pygame.mouse.get_pos()
    	position_list_x.append(position[0])
    	position_list_y.append(position[1])
    	pygame.draw.circle(screen, RED, (position_list_x[0], position_list_y[0]), 50, 4)
    else:
    	print("")
  
    

    pygame.display.flip()
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit()