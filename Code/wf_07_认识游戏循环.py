import pygame

pygame.init()

# 绘制游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制游戏背景
bg = pygame.image.load("飞机大战/images/background.png")
screen.blit(bg,(0, 0))

# 绘制英雄
hero = pygame.image.load("飞机大战/images/me1.png")
screen.blit(hero,(200, 500))

pygame.display.update()

i = 0
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    print(i)
    i += 1


pygame.quit()