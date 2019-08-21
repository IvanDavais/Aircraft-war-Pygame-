#! /usr/bin/python3
import pygame
from wf_12_plane_sprites import *


class PlaneGame(object):
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREE_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 掉用私有方法, 精灵和精灵组的创建
        self.__create_sprites()
        print("游戏初始化！")
        # 使用定时器创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("开始游戏！")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2.事件监听
            self.__eventhandler()

            # 3.碰撞检测
            self.__checkcollide()

            # 4.更新精灵组
            self.__updatesprites()

            # 5.更新屏幕显示
            pygame.display.update()

    def __eventhandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__gameover()
            # 利用事件监听，来检测是否出现创建敌机
            elif event.type == CREATE_ENEMY_EVENT:
                # print("创建敌机！")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 方法一：使用pygame.key.get_pressed()返回所有按键元组
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")

        # 方法二： 通过键盘常量，判断元组中某一个键是否被按下，如果被按下，对应的值为1
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            # print("持续向右移动.")
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __checkcollide(self):
        # 子弹撞击敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 英雄撞击敌机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 杀死英雄
            self.hero.kill()
            # 关闭游戏
            PlaneGame.__gameover()

    def __updatesprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 更新子弹精灵组
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)



    @staticmethod
    def __gameover():
        print("游戏结束！")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()