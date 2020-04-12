#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/10 --
import pygame
from plane_sprite import *

class PlaneGame:
    """ 飞机大战练习"""
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

        # 4.设置定时时间 - 创建敌机 1s，CREATE_ENEMY_EVENT创建敌机频率，HERO_FIRE_EVENT发射子弹频率
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def start(self):
        while True:
            # 设置刷新频率
            self.clock.tick(60)
            # 监听事件
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 绘制图像
            self.__update_sprites()
            # 刷新显示
            pygame.display.update()

    def __create_sprites(self):
        # 创建背景精灵和精灵组，调用plane_sprites的Background()类
        bg1 = Background()
        bg2 = Background(True)
        self.back_ground = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否点×退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                # 1.创建敌机精灵
                enemy = EnemyPlane()
                # 2.将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 使用键盘提供的方法获取键盘按键
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中对应的按键索引值 1
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 3
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -3
            else:
                self.hero.speed = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机，子弹和敌机都销毁
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2.敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 3.判断列表是否有内容，有内容英雄飞机摧毁
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 背景精灵组更新
        self.back_ground.update()
        self.back_ground.draw(self.screen)

        # 敌机精灵组更新
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)


        # 英雄精灵组更新
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹精灵组更新
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    @staticmethod
    def __game_over():
        print("游戏结束...")

        pygame.quit()
        exit()




if __name__ == '__main__':
    game = PlaneGame()
    game.start()






print("飞机大战")
