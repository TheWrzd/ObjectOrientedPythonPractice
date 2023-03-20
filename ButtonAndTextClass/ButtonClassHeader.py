#Simple Button Class

import pygame
from pygame.locals import *

class SimpleButton():
    #Used to Track the state of the button
    STATE_IDLE = 'idle' #Button is up, mouse not over botton
    STATE_ARMED = 'armed' #Button is down, mouse over button
    STATE_DISARMED = 'disarmed' #Clicked down on button, rolled off


    def __init__(self,window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        #Get the rect of the button(used to see if the mouse is over the button)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE
    
    def handleEvent(self, eventObj):
        #The method will return true if user clicks the button
        #Normally returns False

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            #the button only cares about mouse related events
            return False
        
        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if(eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            
        elif self.state == SimpleButton.STATE_ARMED:
            if(eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True #Clicked
        
            if(eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED
            
        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE
            
        return False
    

    def draw(self):
        #Draw the button's current appearance to the window
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        
        else: #IDLE or Disarmed
            self.window.blit(self.surfaceUp, self.loc)




        