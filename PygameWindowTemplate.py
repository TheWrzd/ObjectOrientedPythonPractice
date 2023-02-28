#pygame widow template

#Import packages
import pygame
from pygame.locals import *
import sys

#Define Constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGTH = 480 
FRAMES_PER_SECOND = 30

#3 Initialize the world  
pygame.init
window = pygame.diplay.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()

#4 Load assests, images and sounds, etc


#5 - Initialize Variables 


# 6 Loop forever 
while True:

        #7 Check for and handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        
        #8 Do any "Per Frame" actions 
        

        #9 - Clear the window   
        window.fill(BLACK)


        #10 Draw all the window elements


        #11 Update the display window
        pygame.display.update()


        #12 Slows thing down a bit
        clock.tick(FRAMES_PER_SECOND)
