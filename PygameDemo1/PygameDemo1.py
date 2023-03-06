#pygame widow template

#Import packages
import pygame
from pygame.locals import *
import sys
import random

#Define Constants
BLACK = (0,0,0)
WINDOW_WIDTH = 1200
WINDOW_HEIGTH = 1000 
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3


#3 Initialize the world  
pygame.init
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()

#4 Load assests, images and sounds, etc

ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.png')

squishSound = pygame.mixer.Sound('sounds/squish.wav')
pygame.mixer.music.load('sounds/backGroundMusic.mp3')
pygame.mixer.music.play(-1, 0.0)

#5 - Initialize Variables 
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGTH - ballRect.height
ballX = random.randrange(MAX_HEIGHT)
ballY = random.randrange(MAX_WIDTH)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME


# 6 Loop forever 
while True:
        
        #7 Check for and handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        
        #See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
              ballX = random.randrange(MAX_WIDTH)
              ballY = random.randrange(MAX_HEIGHT)
              ballRect = pygame.Rect(ballX,ballY, MAX_WIDTH, MAX_HEIGHT)

        #8 Do any "Per Frame" actions 
        keyPressedTuple = pygame.key.get_pressed()

        if keyPressedTuple[pygame.K_LEFT]:
               ballX -= N_PIXELS_PER_FRAME

        if keyPressedTuple[pygame.K_RIGHT]:
               ballX += N_PIXELS_PER_FRAME

        if keyPressedTuple[pygame.K_UP]:
               ballY -= N_PIXELS_PER_FRAME

        if keyPressedTuple[pygame.K_DOWN]:
               ballY += N_PIXELS_PER_FRAME

        if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
            xSpeed = -xSpeed #reverse the x direction
            squishSound.play()

        if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGTH):
            ySpeed = -ySpeed #reverse Y direction
            squishSound.play()

        #Update the ball's rectangle usering the speed in two directions
        ballRect.left = ballRect.left + xSpeed
        ballRect.top = ballRect.top + ySpeed                    

        #9 - Clear the window   
        window.fill(BLACK)

        #10 Draw all the window elements
        window.blit(ballImage,ballRect)
    

        #11 Update the display window
        pygame.display.update()


        #12 Slows thing down a bit
        clock.tick(FRAMES_PER_SECOND)
