import pygame
import random

SCREE_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("飞机大战/images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    """游戏背景设置"""
    def update(self, *args):
        # 父类update的调用
        super().update()
        # 判断是否移出屏幕， 如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREE_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 1.指定敌机图片
        super().__init__("飞机大战/images/enemy1.png")
        # 2.敌机飞行的随机速度
        self.speed = random.randint(5, 10)
        # 3.敌机随机的水平出现位置
        max_x = SCREE_RECT.width-self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0

    def update(self):
        # 1.调动父类方法
        super().update()
        # 2.如果飞出屏幕，将相关的敌机从敌机精灵组中删除
        if self.rect.y > SCREE_RECT.height:
            # print("敌机飞出屏幕")
            # kill 方法可以将飞出屏幕的精灵从所有组中删除
            self.kill()

    # def __del__(self):
    #     print("%s 挂了" %self)


class Hero(GameSprite):
    def __init__(self):
        # 设置我方飞机的图片
        super().__init__("飞机大战/images/me1.png")
        # 设置我方飞机的位置
        self.rect.centerx = SCREE_RECT.centerx
        self.rect.bottom = SCREE_RECT.bottom - 120
        self.speed = 0

        # 创建子弹的精灵组
        self.bullet_group = pygame.sprite.Group()


    def update(self):
        self.rect.x += self.speed
        max_x = SCREE_RECT.width - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > max_x:
            self.rect.x = max_x

    def fire(self):
        print("发射子弹！")

        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 调整子弹精灵的位置
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            # 3. 将创建好的子弹精灵添加到子弹精灵组
            self.bullet_group.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("飞机大战/images/bullet1.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
