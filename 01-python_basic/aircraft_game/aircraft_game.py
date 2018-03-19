# -*- coding:utf-8 -*-

import pygame
import time
from pygame.locals import *

def main():

    # 1. create a window
    screen = pygame.display.set_mode((480,852),0,32)

    # 2. create a background fit the window
    background = pygame.image.load("./aircraft_img/background.png")

    # 2. create the image of the aircraft
    aircraft = pygame.image.load("./aircraft_img/hero1.png")

    # axis x, y
    x = 180
    y = 700
    # 3. display the background on the window
    while True:

        # setup the display of the background
        screen.blit(background,(0,0))

        # setup the display of the aircraft
        screen.blit(aircraft,(x,y))
        # update the display of content
        pygame.display.update()

        for event in pygame.event.get():
            #
            if event.type == QUIT:
                print("exit")
                exit()
            # 
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    x -= 5

                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    x += 5
                
                elif event.key == K_SPACE:
                    print("space")


        time.sleep(0.01)

if __name__ == "__main__":
    main()
