import pygame
from WizrardRunConstants import *

from pygame.locals import *

playerIcon = pygame.image.load("WizardRun/images/Pac-man.png")
#Player Class

class Player():
    
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windoWidth = windowWidth
        self.windowHeight = windowHeight

        
        self.image = playerIcon
        self.PlayerRect = self.image.get_rect()
        
        self.width = self.PlayerRect.width
        self.height = self.PlayerRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        #Player Starting Postion
        self.x = 61
        self.y = 61
        self.xVel = 0
        self.yVel = 0
        self.speed = playerSpeed
        

        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
        

    def update(self):
        self.xVel = 0
        self.yVel = 0
        state = self.GetState()

        if state == 'left' and self.collision() == False:
            self.xVel = -self.speed  
        elif state == 'right' and self.collision() == False:
            self.xVel = self.speed
        elif state == 'up' and self.collision() == False:
            self.yVel = -self.speed  
        elif state == 'down' and self.collision() == False:
            self.yVel = self.speed
    
        self.x += self.xVel
        self.y += self.yVel
    
    def BoardCollision(self,LastState):
        state = self.GetState()
        NewPlayerRect = self.GetNewPlayerRect()
        
        for obstacle in obstacle_List:
            if state == 'left' and (NewPlayerRect.colliderect(obstacle) == True):
                self.SetStates(LastState)
            elif state == 'right' and (NewPlayerRect.colliderect(obstacle) == True):
                self.SetStates(LastState)
            elif state == 'up' and (NewPlayerRect.colliderect(obstacle) == True):
                self.SetStates(LastState)     
            elif state == 'down' and (NewPlayerRect.colliderect(obstacle) == True):
                self.SetStates(LastState)
        
    def SetStates(self, dir):
        print("DIRECTION:", dir)
        if dir == 'right':
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        elif dir == 'left':
            self.right = False
            self.left = True
            self.up = False
            self.down = False
        elif dir == 'down':
            self.right = False
            self.left = False
            self.up = False
            self.down = True
        elif dir == 'up':
            self.right = False
            self.left = False
            self.up = True
            self.down = False
        else:
            print('All FAlIED')

    def GetState(self):
        if self.left == True:
            return 'left'  
        elif self.right == True:
            return 'right'
        elif self.up == True:
            return 'up' 
        elif self.down == True:
            return 'down'
        
    def collision(self):
        state = self.GetState()
        NewPlayerRect = self.GetNewPlayerRect()
        dir_list = ['up', 'down', 'left', 'right']
        output = False
        for obstacle in obstacle_List:
            
            if state == 'up' and NewPlayerRect.colliderect(borderTop) == True:
                print('COLLISION',self.x, ' ', self.y)
                output = True
            elif state == 'down' and NewPlayerRect.colliderect(borderBottom) == True:
                print('COLLISION',self.x, ' ', self.y)
                output = True
            elif state == 'left' and NewPlayerRect.colliderect(borderLeft) == True:
                print('COLLISION',self.x, ' ', self.y)
                output = True
            elif state == 'right' and NewPlayerRect.colliderect(borderRight) == True:
                print('COLLISION',self.x, ' ', self.y)
                output = True
            elif state == 'down' and NewPlayerRect.colliderect(obstacle):
                print('COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                output = True
            elif state == 'up' and NewPlayerRect.colliderect(obstacle):
                print('COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                output = True
            elif state == 'right' and NewPlayerRect.colliderect(obstacle):
                print('COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                output = True
            elif state == 'left' and NewPlayerRect.colliderect(obstacle):
                print('COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                output = True
        
        return output
    
    def GetNewPlayerRect(self):
        state = self.GetState()
        
        if state == 'left':
            nextMove = self.x - playerClearance
            NewPlayerRect = pygame.Rect(nextMove, self.y, self.width, self.height)
        elif state == 'right':   
            nextMove = self.x + playerClearance
            NewPlayerRect = pygame.Rect(nextMove, self.y, self.width, self.height)
        elif state == 'up':   
            nextMove = self.y - playerClearance
            NewPlayerRect = pygame.Rect(self.x, nextMove, self.width, self.height)
        elif state == 'down':   
            nextMove = self.y + playerClearance
            NewPlayerRect = pygame.Rect(self.x, nextMove, self.width, self.height)
        
        return NewPlayerRect   
            
  
    
        

    
