import pygame
from woidow import Window
from play import TuxPlay

pygame.init()
# 窗口对象
screen = Window()

# 玩家对象
tux_play = TuxPlay((screen.size[0] / 2, screen.size[1] / 2))

# tux_play 加入显示队列
screen.add_blit_sequence(tux_play.get_init_surface())

running = True
dt = 0
clock = pygame.time.Clock()

tux_play.set_surface()

while running:
    for _event in pygame.event.get():
        if _event.type == pygame.QUIT:
            running = False
            tux_play.thread_loop = False
        if _event.type == pygame.KEYDOWN:
            tux_play.is_run = True
        tux_play.is_run = False

    print(tux_play.is_run)







    tux_play.play_rotate()
    tux_play.play_key_move(dt)

    screen.display()
    screen.update_blit_sequence(1, tux_play.get_surface())

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
