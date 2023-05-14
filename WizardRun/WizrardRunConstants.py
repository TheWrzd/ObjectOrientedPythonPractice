import pygame
import math

playerSpeed = 7
CPU_Speed = 3
CPU_Distance_Trigger = 80
playerClearance = 10
MinWidth = 62  
MaxWidth = 1018

MinHeight = 58
MaxHeight = 1022


translucent_color = (50, 205, 50, 128)
white = (255,255,255)
red = (255,0,0)
window = pygame.display.set_mode((1080, 1080))

borderTop = pygame.Rect(40,40,998,19) 
borderLeft = pygame.Rect(40,40,21,1001)
borderRight = pygame.Rect(1021, 40, 22, 1001)
borderBottom = pygame.Rect(40,1019,998,20)

obstacle1 = pygame.Rect(120,119,139,39)
obstacle2 = pygame.Rect(320,119,143,39)
obstacle3 = pygame.Rect(521,60,38,97)
obstacle4 = pygame.Rect(615,119,146,39)
obstacle5 = pygame.Rect(819,119,144,39)

obstacle6 = pygame.Rect(120,217,139,41)
obstacle7 = pygame.Rect(320,217,42,242) 
obstacle8 = pygame.Rect(421,217,236,39)
obstacle9 = pygame.Rect(718,217,43,242)
obstacle10 = pygame.Rect(819,217,144,41)

obstacle11 = pygame.Rect(63, 317,198,139)
obstacle12 = pygame.Rect(362,315,99,45)
obstacle34 = pygame.Rect(521,259,39,101)
obstacle13 = pygame.Rect(619,315,99,45)
obstacle14 = pygame.Rect(819,317,222,141)

obstacle15 = pygame.Rect(422,419,240,144)
"""""
obstacle15 = pygame.Rect(422,419,98,16)
obstacle35 = pygame.Rect(561,417,101,16)
obstacle36 = pygame.Rect(420,540,236,16)           #Middle
obstacle37 = pygame.Rect(422,419,19,140)
obstacle38 = pygame.Rect(640,417,19,140)
"""

obstacle16 = pygame.Rect(42,519,222,141)
obstacle17 = pygame.Rect(320,519,44,141)
obstacle18 = pygame.Rect(422,616,236,43)
obstacle19 = pygame.Rect(718,519,43,141)
obstacle20 = pygame.Rect(819,519,220,141)

obstacle21 = pygame.Rect(120,718,344,43)
obstacle22 = pygame.Rect(521,659,39,101)
obstacle23 = pygame.Rect(619,718,344,43)

obstacle24 = pygame.Rect(221,761,40,100)
obstacle25 = pygame.Rect(819,761,42,100)

obstacle26 = pygame.Rect(61,818,102,43)
obstacle27 = pygame.Rect(319,819,44,98)
obstacle28 = pygame.Rect(422,818,236,43)
obstacle29 = pygame.Rect(717,818,44,99)
obstacle30 = pygame.Rect(918,818,101,43)

obstacle31  = pygame.Rect(120,919,344,45)
obstacle32  = pygame.Rect(521,861,39,101)
obstacle33 = pygame.Rect(619,919,344,45)


obstacle_List = [ borderTop, borderBottom, borderLeft, borderRight, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5,
                 obstacle6, obstacle7, obstacle8, obstacle9, obstacle10,
                 obstacle11, obstacle12, obstacle13, obstacle14, obstacle15,
                 obstacle16, obstacle17,obstacle18, obstacle19, obstacle20,
                 obstacle21, obstacle22, obstacle23, obstacle24, obstacle25,
                 obstacle26, obstacle27, obstacle28, obstacle29, obstacle30,
                 obstacle31, obstacle32, obstacle33,obstacle34] 
                 

def distance(x1, y1, x2, y2):
    distance =  abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    print("Distance :", distance)
    return abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
