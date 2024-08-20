import math
import threading
import time

import pygame.time
from pygame import image, transform, Vector2
from pygame.sprite import Sprite


class TuxPlay(Sprite):
    def __init__(self, pos, *groups: Sprite):
        super().__init__(*groups)

        self.init_play_image = image.load('./data/tux0.png')
        self.init_play_image.set_colorkey((0, 0, 248))
        self.init_play_pos = Vector2(pos)
        self.angle = 0
        self.speed = 200
        self.thread_loop = True
        self.is_run = False

        self.play_image = None
        self.play_pos = Vector2()

    def play_key_move(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.init_play_pos.y -= dt * self.speed
        if key[pygame.K_DOWN]:
            self.init_play_pos.y += dt * self.speed
        if key[pygame.K_LEFT]:
            self.init_play_pos.x -= dt * self.speed
        if key[pygame.K_RIGHT]:
            self.init_play_pos.x += dt * self.speed

    def play_rotate(self):
        self.play_image = transform.rotate(self.init_play_image, self.angle)
        self.play_pos = self.play_image.get_rect(center=self.init_play_pos)

        mousePos = pygame.mouse.get_pos()

        x = mousePos[0] - self.get_pos_x()
        y = mousePos[1] - self.get_pos_y()

        angle = math.degrees(math.atan2(-x, -y))
        self.set_angle(angle)

    def set_angle(self, angle):
        self.angle = angle

    def get_init_surface(self):
        return self.init_play_image, self.init_play_pos

    def set_surface(self):
         threading.Thread(target=self.exchange_image, args=()).start()


    def get_surface(self):
        return self.play_image, self.play_pos

    def get_pos_x(self):
        return self.play_pos.x

    def get_pos_y(self):
        return self.play_pos.y

    def exchange_image(self, *args):
        i = 0
        while self.thread_loop:
            if self.is_run:
                self.init_play_image = image.load(f'./data/tux{i}red.png')
                self.init_play_image.set_colorkey((0, 0, 248))
            else:
                self.init_play_image = image.load(f'./data/tux{i}.png')
                self.init_play_image.set_colorkey((0, 0, 248))


            time.sleep(2)
            i += 1
            if i == 5:
                i = 0

