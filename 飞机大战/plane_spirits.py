# -*- coding: utf-8 -*-
"""
libo 2020/6/21 11:13
"""
import  random
import pygame
SCREEN_RECT=pygame.Rect(0,0,480,700)
FRAME_PER_SECOND=60
# 敌机定时器ID
CREAT_ENEMY_EVENT=pygame.USEREVENT
# 发射子弹事件ID
HERO_FIRE_EVENT=pygame.USEREVENT+1
# 继承游戏精灵
class GameSpirit(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向移动,更新坐标
        self.rect.y += self.speed
# 游戏背景精灵
class Background(GameSpirit):
    def __init__(self, is_alt=False):
        # 调用父类方法生产背景图像，默认位置
        super().__init__("./images/background.png")
        # 如果是第二种图像，需要更改初始位置
        if is_alt:
             self.rect.y = -self.rect.height
    def update(self):
        #1. 调用父类方法
        super().update()
        #2. 如果移除屏幕，将背景图设置到顶部
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
# 游戏敌机精灵
class Enemy(GameSpirit):
    def __init__(self):
        speed = random.randint(1, 3)
        #1. 创建敌机,指定初始随机速度
        super().__init__("./images/enemy1.png",speed)

         #3. 指定初始随机位置,x 坐标是窗口随机，敌机图像底边的y坐标是0
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)
    def update(self):
        # 1. 保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是就删除
        if self.rect.y >SCREEN_RECT.height :
            self.kill()
class Hero(GameSpirit):
    def __init__(self):
        super().__init__("./images/me1.png", speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120
        # 创建子弹精灵族作为英雄的属性，这样才能调用
        # 子弹的位置是随着英雄而变

        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <0 :
            self.rect.x=0
        elif self.rect.right> SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 子弹的位置是英雄的正上方，在子弹类无法指定
        for i in range(3):
            bullet = Bullet()
            bullet.rect.bottom= self.rect.top-20*i
            bullet.rect.centerx= self.rect.centerx
            print("发射子弹",bullet.rect.bottom)
            self.bullet_group.add(bullet)


class Bullet(GameSpirit):
    def __init__(self):
        speed = -3
        # 1. 创建敌机,指定初始随机速度
        super().__init__("./images/bullet1.png", speed)

    def update(self):
        # 1. 保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是就删除
        if self.rect.bottom <0 :
            self.kill()

