# -*- coding: utf-8 -*-
"""
libo 2020/6/22 19:11
"""
import pygame
# 屏幕大小


from plane_spirits import *
class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        print("游戏初始化")
        # 游戏初始化
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵族的创建
        self.__creat_spirits()
        # 4. 设置定时器事件， 创建敌机
        pygame.time.set_timer(CREAT_ENEMY_EVENT,1000)
        # 5. 设置定时器事件， 发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT,200)

    # 创建精灵族
        self.__creat_spirits()

    def __creat_spirits(self):
        # 精灵
        bg1= Background()
        bg2= Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建空的敌机的精灵族，根据监听事件中的时钟频率精灵族是变化的
        self.enemy_group= pygame.sprite.Group()
        # 创建英雄精灵和精灵族
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    # 开始游戏
    def start_game(self):

        print("游戏开始")
        while True:
            #1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SECOND)
            #2. 事件监听
            self.__event_handler()
            #3. 碰撞检测
            self.__check_collide()
            #4. 更新、绘制精灵族
            self.__update_spirites()
            #5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        event_list = pygame.event.get()
        for event in event_list:
            # 退出游戏
            if event.type == pygame.QUIT:
                print("退出游戏")
                PlaneGame.__game_over()
            # 根据定时器来运行创建敌机并添加到精灵族
            elif event.type == CREAT_ENEMY_EVENT:
                enemy= Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 所有键盘按键是否按下的元组，按下为1
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            # print("向右 被按下")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else :
            self.hero.speed = 0

    def __check_collide(self):
        # 发生碰撞就自动销毁，子弹摧毁飞机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group,True,True)
        # 敌机撞毁英雄, 返回碰撞的敌机列表
        enemies= pygame.sprite.spritecollide(self.hero, self.enemy_group,True)
        if len(enemies) >0 :
            self.hero.kill()
            PlaneGame.__game_over()
    def  __update_spirites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game Over")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象，开始游戏
    game=PlaneGame()
    game.start_game()
