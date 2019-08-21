import pygame

pygame.init()

# 绘制游戏背景
screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("飞机大战/images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update() 注意：去掉此处的update 同样可以完成图像的渲染

# 绘制英雄图片
hero = pygame.image.load("飞机大战/images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()