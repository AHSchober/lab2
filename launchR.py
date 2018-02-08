from math import *
import colors, pygame, sys, time
from pygame.locals import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = radians(90)
MIN_ANGLE = 0


class launcher:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.deltaM = 0
        self.deltaA = 0
        self.magnitude = 20
        self.angle = radians(45)
    
    def changeMagnitude(self, delta):
        
        if self.magnitude+delta > MAX_MAG:
            delta = 0
        elif self.magnitude+delta < MIN_MAG:
            delta = 0
        self.magnitude += delta
                
    def changeAngle(self, delta):

        if self.angle + delta > MAX_ANGLE:
            delta = 0
        elif self.angle + delta < MIN_ANGLE:
            delta = 0
        self.angle += delta
        
    def draw(self, surf):
        
        self.surf = surf
        Xf = self.x + self.magnitude*cos(self.angle)
        Yf = self.y - self.magnitude*sin(self.angle)
        pygame.draw.line(self.surf, colors.BLACK, [self.x, self.y],[Xf,Yf],3)
        pygame.display.update()

    def fire(self,rock):
        rock.vx = self.magnitude*cos(self.angle)
        rock.vy = -1*self.magnitude*sin(self.angle) # Negative for inverted coordinates
        
