import pygame
import time
import math
import alien
import missilecode
import random
import ghost
import space
from pygame.locals import *
import missilecode
import os
pygame.init()


def mov(img, x, y):
    gameDisplay.blit(img, (x, y))
width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
crashed = False
black = (0, 0, 0)
white = (255, 255, 255)
f = 0
x = (400)
y = (575)
start = time.time()
smallmisobj = 10
largemisobj = 10
alienobj = alien.alienware('alien.png')
shipobj = space.spaceship('ship3.png')
missofar = []
font = pygame.font.Font(None, 36)
score = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
#        moving spaceship
        if event.type == KEYDOWN:
            if event.key == 97:
                if x-100 >= 0:
                    x -= 100
            elif event.key == 100:
                if x+100 <= 700:
                    x += 100
            elif event.key == K_SPACE:
                smallmisobj = missilecode.smallmis('smallmis.png')
                smallmisobj.x = x+30
                missofar.append(smallmisobj)
            elif event.key == K_s:
                largemisobj = missilecode.largemis('largemis.png')
                largemisobj.x = x+30
                missofar.append(largemisobj)
            elif event.key == K_q:
                crashed = True
    for i in missofar:
        # delete ghost
        if i.__class__.__name__ == 'ghost':
            if time.time()-i.start >= 5:
                missofar.remove(i)
            else:
                mov(ghostobj.img, ghostobj.x, ghostobj.y)
#       delete alien
        elif i.__class__.__name__ == 'largemis' or i.__class__.__name__ == 'smallmis':
            if time.time()-i.start > 15:
                missofar.remove(i)
            elif f == 0:
                if abs(i.x-alienobj.alienx) < 70 and abs(i.y-alienobj.alieny) <= 50:
                    score += 1
                    if i.movement == 4:
                        ghostobj = ghost.ghost('ghost.png', alienobj.alienx, alienobj.alieny)
                        del alienobj
                        f = 1
                        mov(ghostobj.img, ghostobj.x, ghostobj.y)
                        missofar.append(ghostobj)
                    else:
                        del alienobj
                        f = 1
                    missofar.remove(i)
            i.y -= i.movement
            mov(i. img, i.x, i.y)
#   self destruct alien
    if time.time()-start >= 8 and f == 0:
        del alienobj
        f = 1
#   create new alien
    if time.time()-start >= 10:
        start = time.time()
        alienobj = alien.alienware('alien.png')
        f = 0
    if f == 0:
        mov(alienobj.img, alienobj.alienx, alienobj.alieny)
    mov(shipobj.img, x, y)
    text = font.render("Score: "+str(score), True, white)
    gameDisplay.blit(text, [10, 690])
    pygame.display.update()
    gameDisplay.fill(black)
    clock.tick(60)
