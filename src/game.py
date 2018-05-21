#coding=utf-8

import Bullet
import Enemy

import pygame

#向sys模块借一个exit函数用来退出程序
from sys import exit

#初始化pygame,为使用硬件做准备

pygame.init()

#创建了一个窗口,窗口大小和背景图片大小一样
screen = pygame.display.set_mode((450, 800), 0, 32)

#设置窗口标题
pygame.display.set_caption("Auther:陈勇臻")

#加载并转换图像
background = pygame.image.load('../img/back.jpg').convert()
plane=pygame.image.load('../img/plane.png').convert_alpha()

#创建子弹list
bullets=[]
#向list添加5发子弹
for i in range(5):
    bullets.append(Bullet())

#子弹总数
count_b=len(bullets)

#即将激活的子弹序号
index_b=0

#发送子弹间隔
interval_b=0

#创建一个bullet的对象
bullet=Bullet.Bullet()
enemy=Enemy.Enemy()
#游戏主循环
while True:
    for event in pygame.event.get():
        # 接收到退出事件后退出程序
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))


    #子弹发送间隔递减
    interval_b -=1


    #当间隔小于0时，激活一发子弹
    if interval_b<0:
        bullet[index_b].restart()
        interval_b=100
        index_b=(index_b+1)%count_b

    for b in bullets:
        b.move()
        screen.blit(b.image,(b.x,b.y))


    #绘制飞机
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseX -= plane.get_width() / 2
    mouseY -= plane.get_height() / 2
    screen.blit(plane, (mouseX, mouseY))

    #绘制敌机
    enemy.move()
    screen.blit(enemy.image, (enemy.enemy_x, enemy.enemy_y))

    # 刷新一下画面
    pygame.display.update()

