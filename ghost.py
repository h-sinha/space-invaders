import pygame
from pygame.locals import *
import time


class ghost(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(ghost, self).__init__()
        self.img = pygame.image.load(img)
        self.start = time.time()
        self.x = x
        self.y = y
