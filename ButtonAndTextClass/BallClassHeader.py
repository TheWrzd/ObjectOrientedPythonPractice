import pygame
from pygame.locals import *
import random 

#Ball class
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windoWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('ButtonAndTextClass/images/ball.png')
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        #Pick Random starting postion
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)
         
        #Choose a rando speed between -4 and 4, but not zero
        speedsList = [-4,-3,-2,-1,0,1,2,3,4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        #Check for hitting wall, if so change direction
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if(self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
        
        #Update the ball's s and y using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed
    
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


        