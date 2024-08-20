import pygame

pygame.init()

clock = pygame.time.Clock()

image = pygame.image.load('./data/tux0.png')

win = pygame.display.set_mode((800, 600))
play_s = pygame.Surface(image.get_size())
play_s.blit(image,(0,0))
angle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    _key = pygame.key.get_pressed()

    if _key[pygame.K_DOWN]:
        angle += 1
        print('hello')

    pygame.display.flip()

    play_s1 = pygame.transform.rotate(play_s, angle)
    win.blit(play_s1, play_s1.get_rect(center=(100, 100)))

    dt = clock.tick(60) / 1000

pygame.quit()
