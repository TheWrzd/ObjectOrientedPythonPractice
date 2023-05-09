import pygame

obstacle1 = pygame.Rect(189, 121, 111, 36)

class board:

    def __init__(self,window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.obstacle = pygame.polygone