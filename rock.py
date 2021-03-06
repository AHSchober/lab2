#!/usr/bin/python

import pygame
from colors import *

G = 20 # Remains positive because of the inverted coordinate system

class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.rock = (0,0,0,0)
        
    def move(self, time):
        self.x += self.vx*time # Move in x direction
        if(self.vy !=0):
            self.vy += G*time # Update the y velocity for g
        self.y += self.vy*time # Move in y direction
    
    def isMoving(self):
        if (self.vx == 0) and (self.vy == 0):
            return False
        else:
            return True

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def getRect(self):
        return self.rock
    
    def draw(self, surf):

        self.rock = pygame.Rect((0,0,10,10))
        self.rock.center=(self.x,self.y)
        pygame.draw.rect(surf,(ROCK_COLOR),self.rock)
        
        
    
