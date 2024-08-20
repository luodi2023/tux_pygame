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

tux_play.animation_surface()
tux_play.thread_bitmap()

while running:
    for _event in pygame.event.get():
        if _event.type == pygame.QUIT:
            running = False
            tux_play.thread1_loop = False
            tux_play.thread2_loop = False

    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        tux_play.play_attack()


    tux_play.play_rotate()
    tux_play.play_key_move(dt)

    screen.display()
    screen.update_blit_sequence(1, tux_play.get_surface())

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
