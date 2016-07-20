import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Catch That Mouse!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Mouse(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.size = size
    
    def mouse_appear(self,screen):
        pygame.draw.circle(screen, WHITE, [self.x_location, self.y_location], self.size)

#initialize game attributes
screen.fill(GREEN)

#initialize mouse
mouse_x_pos = 350
mouse_y_pos = 250
mymouse = Mouse(mouse_x_pos, mouse_y_pos, 5, 5, 10)
mymouse.mouse_appear(screen)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    mymouse.mouse_appear(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE




