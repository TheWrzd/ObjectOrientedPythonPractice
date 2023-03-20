#pygame widow template

#Import packages
import pygame
from pygame.locals import *
import sys
from ButtonClassHeader import *
from BallClassHeader import *
from TextClass import *


#Define Constants
BLACK = (0,0,0)
WHITE = (255,255,255)
WINDOW_WIDTH = 1100
WINDOW_HEIGTH = 1000 
FRAMES_PER_SECOND = 30

#3 Initialize the world  
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()

#4 Load assests, images and sounds, etc


#5 - Initialize Variables 
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGTH)
oFrameCountLabel = SimpleText(window, (60, 20), 'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500,20), ' ', WHITE)
oRestartButton = SimpleButton(window, (850, 60), 'ButtonAndTextClass/images/ActiveButton.png', 'ButtonAndTextClass/images/inactiveButton.png')

frameCounter = 0

# 6 Loop forever 
while True:

        #7 Check for and handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if oRestartButton.handleEvent(event):
                   frameCounter = 0
        
        #8 Do any "Per Frame" actions 
        oBall.update() #Tell the ball to update itself
        frameCounter = frameCounter + 1
        oFrameCountDisplay.setValue(str(frameCounter))

        #9 - Clear the window   
        window.fill(BLACK)


        #10 Draw all the window elements
        oBall.draw()
        oFrameCountLabel.draw()
        oFrameCountDisplay.draw()
        oRestartButton.draw()

        #11 Update the display window
        pygame.display.update()


        #12 Slows thing down a bit
        clock.tick(FRAMES_PER_SECOND)