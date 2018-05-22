#coding=utf-8
import pygame
from sys import exit
import bullet
import enemy

pygame.init()
screen = pygame.display.set_mode((450, 600), 0, 32)
pygame.display.set_caption("Auther:陈勇臻")
background = pygame.image.load('../img/back.jpg').convert()
plane=pygame.image.load('../img/plane.png').convert_alpha()
#创建子弹list
bullets=[]
#向list添加5发子弹
for b in range(5):
    bullets.append(bullet.Bullet())
#子弹总数
count_b=len(bullets)
#即将激活的子弹序号
index_b=0
#发送子弹间隔
interval_b=0
enemys = []
for e in range(5):
    enemys.append(enemy.Enemy())

def checkHit(enemy, bullet):
	if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
	    enemy.restart()
	    bullet.active = False
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
        bullets[index_b].restart()
        interval_b=100
        index_b=(index_b+1) % count_b

    for b in bullets:
        if b.active:
            b.move()
            screen.blit(b.image, (b.x, b.y))

    for e in enemys:
        e.move()
        screen.blit(e.image, (e.x, e.y))

    for b in bullets:
        if b.active:
            for e in enemys:
                checkHit(e, b)
    #绘制飞机
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseX -= plane.get_width() / 2
    mouseY -= plane.get_height() / 2
    screen.blit(plane, (mouseX, mouseY))

    # 刷新一下画面
    pygame.display.update()

