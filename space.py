import pygame
from pygame.locals import *


class spaceship(pygame.sprite.Sprite):
    def __init__(self, img):
        super(spaceship, self).__init__()
        self.img = pygame.image.load(img)
