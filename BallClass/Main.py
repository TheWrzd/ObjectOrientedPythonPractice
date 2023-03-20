#pygame widow template

#Import packages
import pygame
from pygame.locals import *
import sys
import random
from BallClass import *

#Define Constants
BLACK = (0,0,0)
WINDOW_WIDTH = 1200
WINDOW_HEIGTH = 1000 
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
N_BALLS = 3


#3 Initialize the world  
pygame.init
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()

#4 Load assests, images and sounds, etc



#5 - Initialize Variables 

ballList = []
for oBall in range(0, N_BALLS):
        oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGTH)
        oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGTH)
        ballList.append(oBall)


# 6 Loop forever 
while True:
        
        #7 Check for and handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


        #8 Do any "Per Frame" actions 
        for oBall in ballList:
                oBall.update()              

        #9 - Clear the window   
        window.fill(BLACK)

        #10 Draw all the window elements
        for oBall in ballList:
                oBall.draw() #Tell the ball to draw itself
    
        #11 Update the display window
        pygame.display.update()

        #12 Slows thing down a bit
        clock.tick(FRAMES_PER_SECOND)
