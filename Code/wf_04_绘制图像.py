import pygame

pygame.init()

# 注意： 1 图片加载时，要使用完整的路径名
#       2 绘制函数位blit

screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("飞机大战/images/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()

while True:
    pass

pygame.quit()