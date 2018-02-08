#!/usr/bin/python

import pygame
from colors import *

G = 10 # Remains positive because of the inverted coordinate system

class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        
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
    
    def draw(self, surf):

        rock = pygame.Rect((0,0,10,10))
        rock.center=(self.x,self.y)
        pygame.draw.rect(surf,(ROCK_COLOR),rock)
        
    
