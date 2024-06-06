import pygame
import time

line = 0

size = (840, 650)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Road Move')

background = pygame.image.load("Assets/road1.png").convert()
pygame.init()

def roadMove(line):
    window.blit(background, (0,line))
    window.blit(background, (0,line-650))
    pygame.display.flip()
    
    if line >= 650:
        line = 0
    time.sleep(0.01)


while True:
    roadMove(line)
    line += 10
    
    
