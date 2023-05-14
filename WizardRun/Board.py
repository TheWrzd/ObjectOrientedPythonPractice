import pygame
from WizrardRunConstants import *
from pygame.locals import *
import random

obstacle1 = pygame.Rect(189, 121, 111, 36)
blinky_Img = pygame.image.load("WizardRun/images/blinky.png")    

class CPU:

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windoWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = blinky_Img
        self.CPURect = self.image.get_rect()

        self.width = self.CPURect.width
        self.height = self.CPURect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        self.LastX = 61
        self.LastY = 61
        
        self.up = False
        self.down = True
        self.left = False
        self.right = False

     #Player Starting Postion
        self.x = 61
        self.y = 61
        self.xVel = 0
        self.yVel = 0
        self.speed = CPU_Speed
    
        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
    
    def update(self,Last_dir):
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
        elif self.collision() == True:
            self.GenMove(Last_dir)
    
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

    def GenMove(self, Last_dir):
        move = random.randint(1,4)

        if move == 1 and Last_dir != 'left':
            self.SetStates('left')
        elif move == 2 and Last_dir != 'right': 
            self.SetStates('right')
        elif move == 3 and Last_dir != 'up':
            self.SetStates('up')
        elif move == 4 and Last_dir != 'down':
            self.SetStates('down')
        else:
            self.GenMove(Last_dir)
    
    
    def SetStates(self, dir):
        print("CPU DIRECTION:", dir)
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
        else:
            return None

        
    def collision(self):
        state = self.GetState()
        NewPlayerRect = self.GetNewPlayerRect()
        for obstacle in obstacle_List:
            
            if state == 'up' and NewPlayerRect.colliderect(borderTop) == True:
                print('CPU COLLISION',self.x, ' ', self.y)
                self.LastX = self.x
                self.LastY = self.y
                return True
            elif state == 'down' and NewPlayerRect.colliderect(borderBottom) == True:
                print('CPU COLLISION',self.x, ' ', self.y)
                return True
            elif state == 'left' and NewPlayerRect.colliderect(borderLeft) == True:
                print('CPU COLLISION',self.x, ' ', self.y)
                self.LastX = self.x
                self.LastY = self.y
                return True
            elif state == 'right' and NewPlayerRect.colliderect(borderRight) == True:
                print('CPU COLLISION',self.x, ' ', self.y)
                self.LastX = self.x
                self.LastY = self.y
                return True
            elif state == 'down' and NewPlayerRect.colliderect(obstacle):
                print('CPU COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                self.LastX = self.x
                self.LastY = self.y
                return True
            elif state == 'up' and NewPlayerRect.colliderect(obstacle):
                print('CPU COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                self.LastX = self.x
                self.LastY = self.y
                return True
            elif state == 'right' and NewPlayerRect.colliderect(obstacle):
                print('CPU COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                self.LastX = self.x
                self.LastY = self.y
                return True
            elif state == 'left' and NewPlayerRect.colliderect(obstacle):
                print('CPU COLLISION',self.x, ' ', self.y, 'OBSTACLE: ', obstacle)
                self.LastX = self.x
                self.LastY = self.y
                return True
            
        return False
    
    def OpenDir(self):
        state = self.GetState()
        NewPlayerRect = None
      


    def GetNewPlayerRect(self):
        state = self.GetState()
        NewPlayerRect = None

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
    
    def DistanceTrigger(self):
        print('TRIGGEREDs', self.LastX, self.LastY, self.x, self.y)
        if distance(self.x, self.y, self.LastX, self.LastY) <= CPU_Distance_Trigger:
            return False
        elif distance(self.x, self.y, self.LastX, self.LastY) >= CPU_Distance_Trigger:
            print('_________DISTANCE TRIGGERED_______')
            self.LastX = self.x
            self.LastY = self.y
            return True
        print("       ")
    
    