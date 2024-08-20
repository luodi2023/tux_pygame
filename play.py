import math
import threading
import time

import pygame.time
from pygame import image, transform, Vector2
from pygame.sprite import Sprite


class TuxPlay(Sprite):
    def __init__(self, pos, *groups: Sprite):
        super().__init__(*groups)

        self.play_bitmap = 0

        self.init_play_image = image.load(f'./data/tux{self.play_bitmap}.png')
        self.init_play_image.set_colorkey((0, 0, 248))
        self.init_play_pos = Vector2(pos)
        self.angle = 0
        self.speed = 200
        self.thread1_loop = True
        self.thread2_loop = True

        self.is_run = False
        self.attack_state = False

        self.play_image = None
        self.play_pos = Vector2()

    def play_key_move(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.init_play_pos.y -= dt * self.speed
            self.is_run = True
        elif key[pygame.K_DOWN]:
            self.init_play_pos.y += dt * self.speed
            self.is_run = True
        elif key[pygame.K_LEFT]:
            self.init_play_pos.x -= dt * self.speed
            self.is_run = True
        elif key[pygame.K_RIGHT]:
            self.init_play_pos.x += dt * self.speed
            self.is_run = True
        else:
            self.is_run = False

    def play_rotate(self):
        self.play_image = transform.rotate(self.init_play_image, self.angle)
        self.play_pos = self.play_image.get_rect(center=self.init_play_pos)

        mousePos = pygame.mouse.get_pos()

        x = mousePos[0] - self.get_pos_x()
        y = mousePos[1] - self.get_pos_y()

        angle = math.degrees(math.atan2(-x, -y))
        self.set_angle(angle)

    def exchange_image(self, *args):
        while self.thread1_loop:
            if self.is_run:
                self.init_play_image = image.load(f'./data/tux{self.play_bitmap}red.png')
                self.init_play_image.set_colorkey((0, 0, 248))
            else:
                self.init_play_image = image.load(f'./data/tux{self.play_bitmap}.png')
                self.init_play_image.set_colorkey((0, 0, 248))

    def animation_surface(self):
        threading.Thread(target=self.exchange_image, args=()).start()

    def fun_set_bitmap(self, *args):
        while self.thread2_loop:
            time.sleep(1)
            if self.play_bitmap == 0:
                self.attack_state = False

            self.play_bitmap += 1
            if self.play_bitmap == 5:
                self.play_bitmap = 0

    def thread_bitmap(self):
        threading.Thread(target=self.fun_set_bitmap, args=()).start()

    def play_attack(self):

        if self.play_bitmap == 0:
            self.play_no_state()
        elif 0 < self.play_bitmap:
            self.attack_state = True

    def play_no_state(self):
        def fun():
            self.init_play_pos.x += 0.5
            self.init_play_pos.y += 0.5

            time.sleep(0.1)
            self.init_play_pos.x -= 0.5
            self.init_play_pos.y -= 0.5

        threading.Thread(target=fun, args=()).start()

    def set_angle(self, angle):
        self.angle = angle

    def get_init_surface(self):
        return self.init_play_image, self.init_play_pos

    def get_surface(self):
        return self.play_image, self.play_pos

    def get_pos_x(self):
        return self.play_pos.x

    def get_pos_y(self):
        return self.play_pos.y
