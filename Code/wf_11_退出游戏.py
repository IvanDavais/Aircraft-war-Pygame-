import pygame

pygame.init()

# 绘制游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制游戏背景
bg = pygame.image.load("飞机大战/images/background.png")
screen.blit(bg,(0, 0))

# 绘制英雄
hero = pygame.image.load("飞机大战/images/me1.png")
screen.blit(hero, (200, 500))

pygame.display.update()


clock = pygame.time.Clock()
hero_reac = pygame.Rect(200, 500, 102, 126)

while True:
    clock.tick(60)
    hero_reac.y -= 1

    # 事件监听方法 pygame.even.get() 方法能捕获用户在此期间的一系列活动， 并返回一个list
    even_list = pygame.event.get()
    # if len(even_list) > 0:
    #    print(even_list)

    # 每次调用update()方法之前，需要把所有的游戏图像都重新绘制一遍，而且应该最新重新绘制背景图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_reac)
    pygame.display.update()

    # 退出游戏代码
    for event in even_list:

        # 记住： 此处是event.type 而不是event
        if event.type == pygame.QUIT:
            print("退出游戏！ ")

            # 卸载所有模块
            pygame.quit()

            # 直接终止当前所有程序
            exit()
