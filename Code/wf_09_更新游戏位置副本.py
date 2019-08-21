import pygame
pygame.init()
# 绘制游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制游戏背景
bg = pygame.image.load("飞机大战/images/background.png")
screen.blit(bg, (0, 0))

# 绘制游戏英雄
hero = pygame.image.load("飞机大战/images/me1.png")
screen.blit(hero, (200, 500))

pygame.display.update()

# 建立时钟
# 建立英雄坐标
clock = pygame.time.Clock()
hero_reac = pygame.Rect(200, 500, 102, 126)

# 游戏循环
while True:
    clock.tick(60)
    hero_reac.y -= 1
    if hero_reac.y <= -hero_reac.height:
        hero_reac.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_reac)
    pygame.display.update()

pygame.quit()