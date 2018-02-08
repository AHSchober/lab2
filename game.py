#!/usr/bin/python

import pygame, sys, time, random
from pygame.locals import *

import launchR, colors, rock, target

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TARGET_WIDTH = 40
FPS = 30

def main():
        pygame.init()
        fpsClock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Launchr 1.0')
        launcher = launchR.launcher(0,SCREEN_HEIGHT-20)
        the_rock = rock.Rock(0,SCREEN_HEIGHT-20)
        the_target = target.Target(random.random()*SCREEN_WIDTH + 100, SCREEN_HEIGHT - 20, TARGET_WIDTH)
        while True:
                
                #1 Process events
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        launcher.changeAngle(0.1)
                                elif event.key == pygame.K_DOWN:
                                        launcher.changeAngle(-0.1)
                                elif event.key == pygame.K_LEFT:
                                        launcher.changeMagnitude(-5)
                                elif event.key == pygame.K_RIGHT:
                                        launcher.changeMagnitude(5)
                                elif (event.key == pygame.K_SPACE) and (not the_rock.isMoving()):
                                        print("FIRE")
                                        launcher.fire(the_rock)
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                #2 ... update game logic ...
                the_rock.move(1.0/FPS)
                                                                        
                #3 draw everything
                draw_world(screen)
                launcher.draw(screen)
                the_rock.draw(screen)
                the_target.draw(screen)
		pygame.display.update()
                # run at the right speed
                fpsClock.tick(FPS)
                
def draw_world(surf):
        #1 Draw the sky with a fill
        surf.fill(colors.SKY_BLUE)
        #2 Add the ground
        ground = pygame.Rect(0,SCREEN_HEIGHT-20,SCREEN_WIDTH,20) #ground object
        pygame.draw.rect(surf,(colors.GRASS_GREEN),ground)
        #3 Add the game title
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('LaunchR 1.0', True, colors.BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SCREEN_WIDTH/2,25)

        surf.blit(textSurfaceObj, textRectObj)

main()        