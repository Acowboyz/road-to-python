# -*- coding:utf-8 -*-

import pygame
import time
import random
from pygame.locals import *

class BaseAircraft(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image  = pygame.image.load(image_name)
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        # use temp list to append the bullet object which is cross the boundary
        # it may not fully remove the bullet wihich is cross the boundary, when you remove the object in the loop of its own list. 
        temp_bullet_list = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

            if bullet.judge():
                temp_bullet_list.append(bullet)

        for temp_bullet in temp_bullet_list:
            self.bullet_list.remove(temp_bullet)


class Aircraft(BaseAircraft):
    def __init__(self, screen_temp):
        super(Aircraft, self).__init__( screen_temp, 210, 700, "./aircraft_img/hero1.png")
        
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyAircraft(BaseAircraft):
    def __init__(self, screen_temp):
        super(EnemyAircraft, self).__init__( screen_temp, 0, 0, "./aircraft_img/enemy0.png")
        self.direction = "right"
 
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num ==80:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(object):
    def __init__(self, screen_temp, x, y, image_name):        
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image  = pygame.image.load(image_name)
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y): 
        super(Bullet, self).__init__(screen_temp, x + 40, y -20, "./aircraft_img/bullet.png") 

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):        
        super(EnemyBullet, self).__init__(screen_temp, x + 25, y +40, "./aircraft_img/bullet1.png") 

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

def key_control(aircraft_temp):
    
    for event in pygame.event.get():
        #
        if event.type == QUIT:
            print("exit")
            exit()
        # 
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                aircraft_temp.move_left()

            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                aircraft_temp.move_right()
            
            elif event.key == K_SPACE:
                print("space")
                aircraft_temp.fire()

def main():

    # 1. create a window
    screen = pygame.display.set_mode((480,852),0,32)

    # 2. create a background fit the window
    background = pygame.image.load("./aircraft_img/background.png")

    # 2. create the object of the aircraft
    aircraft = Aircraft(screen)
    # 2. create the object of the enemy
    enemy    = EnemyAircraft(screen)
    # 3. display the background on the window
    while True:

        # setup the display of the background
        screen.blit(background,(0,0))

        # setup the display of the aircraft
        aircraft.display()
        # setup the display of the enemy
        enemy.display()

        enemy.move()

        enemy.fire()
        # update the display of content
        pygame.display.update()

        key_control(aircraft)



        time.sleep(0.01)

if __name__ == "__main__":
    main()
