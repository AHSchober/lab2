import pygame
import colors
import rock

class Target:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.target = pygame.Rect((0,0,width,10))
        self.target.center = (self.x, self.y)

    def hitBy(self, obj):
        return self.target.colliderect(obj.getRect())
        
    def draw(self, surf):
        
        pygame.draw.rect(surf,(colors.TARGET_COLOR),self.target)
        
