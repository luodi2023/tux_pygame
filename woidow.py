import pygame
from pygame import display, image



class Window:
    def __init__(self):
        self.bg_image = image.load('./data/background.jpg')
        self.size = (self.bg_image.get_size())
        self.sc = display.set_mode(self.size)

        self.blit_sequence = [(self.bg_image, (0, 0))]

    def display(self):
        self.sc.blits(self.blit_sequence)

    def add_blit_sequence(self, Surface):
        self.blit_sequence.append(Surface)

    def update_blit_sequence(self, index, surfaceData):
        self.blit_sequence[index] = surfaceData
