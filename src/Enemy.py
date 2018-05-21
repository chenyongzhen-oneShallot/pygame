#coding=utf-8
import random

import pygame
class Enemy:
    def restart(self):

        self.enemy_x = random.randint(50, 400)

        self.enemy_y = random.randint(-200, -50)

        self.enemy_speed = random.random() + 0.1


    def __init__(self):
        self.restart()

        self.image = pygame.image.load('../img/enemy.png').convert_alpha()



    def move(self):

        if self.enemy_y < 800:

            self.enemy_y += self.enemy_speed

        else:

            self.restart()

