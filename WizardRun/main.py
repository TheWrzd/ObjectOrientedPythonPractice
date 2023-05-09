#pygame widow template

#Import packages
import pygame
from pygame.locals import *
import sys
from Map import *
from PlayerClass import *
from WizrardRunConstants import *

#Define Constants
BLACK = (0,0,0)
showObstacles = False
RED = (255,0,0)
WINDOW_WIDTH = 1080
WINDOW_HEIGTH = 1060

FRAMES_PER_SECOND = 30
TITLE = 'WIZARD-RUN'
BackGround = map

#3 Initialize the world  
pygame.init
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()
transparent_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGTH), pygame.SRCALPHA)

#4 Load assests, images and sounds, etc


#5 - Initialize Variables 
window.blit(BackGround,(0,0))
Player1 = Player(window, WINDOW_WIDTH, WINDOW_HEIGTH)
startGame = True
LastState = None
# 6 Loop forever 
while startGame:

    #7 Check for and handle events
    for event in pygame.event.get():
        key = pygame.key.get_pressed()  
        if Player1.GetState() != LastState:
            LastState = Player1.GetState()
        
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            continue
    if key[pygame.K_LEFT]:
        Player1.SetStates('left')
        Player1.BoardCollision(LastState)
    elif key[pygame.K_RIGHT]:
        Player1.SetStates('right')
        Player1.BoardCollision(LastState)
    elif key[pygame.K_UP]:
        Player1.SetStates('up')
        Player1.BoardCollision(LastState)
    elif key[pygame.K_DOWN]:
        Player1.SetStates('down')
        Player1.BoardCollision(LastState)
    elif key[pygame.K_b]:
        print("B PRESSED")
        if showObstacles == True:
            showObstacles = False
        elif showObstacles == False:
            showObstacles = True
    
    
    
    #8 Do any "Per Frame" actions 
    
    #for obstacle in obstacle_List:
    
    #9 - Clear the window   
    
    window.blit(BackGround,(0,0))
    if showObstacles == True:
        window.blit(transparent_surface, (0,0))

    Player1.update()

    #10 Draw all the window elements
    Player1.draw()
   
    for obstacle in obstacle_List:
        pygame.draw.rect(transparent_surface, translucent_color, obstacle)
    




    #11 Update the display window
    pygame.display.update()
    


    #12 Slows thing down a bit
    clock.tick(FRAMES_PER_SECOND)
