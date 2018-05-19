import pygame
from pygame.locals import *
import random


class alienware(pygame.sprite.Sprite):
    def __init__(self, img):
        super(alienware, self).__init__()
        self.img = pygame.image.load(img)
        self.alienx = random.randint(1, 700)
        self.alieny = random.randint(0, 100)
