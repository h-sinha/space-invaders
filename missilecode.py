import pygame
from pygame.locals import *
import time
import alien


class missiles(pygame.sprite.Sprite):
    def __init__(self, img):
        super(missiles, self).__init__()
        self.img = pygame.image.load(img)
        self.start = time.time()
        self.y = 575
        self.x = 0


class smallmis(missiles):
    def __init__(self, img):
        super(smallmis, self).__init__(img)
        self.movement = 2


class largemis(missiles):
    def __init__(self, img):
        super(largemis, self).__init__(img)
        self.movement = 4
