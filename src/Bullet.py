#coding=utf-8
import pygame
class Bullet:
    def __init__(self):
        # 初始化成员变量，x，y，image
        self.bullet_x=0
        self.bullet_y=-1
        self.image = pygame.image.load('../img/bullet.png').convert_alpha()
        #默认不激活子弹
        self.active=False

    def move(self):
        #如果激活，向上移动
        if self.active:
            self.bullet_y -=3

        #如果超出屏幕则设置为不激活
        if self.bullet_y<0:
            self.active=False

    def restart(self):
        #重置子弹位置
        mouseX, mouseY = pygame.mouse.get_pos()
        self.bullet_x = mouseX - self.image.get_width() / 2
        self.bullet_y = mouseY - self.image.get_height() / 2
        self.active=True


