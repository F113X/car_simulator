import pygame
pygame.init()

screen_width = 840
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('Assets/road1.png').convert_alpha()
player = pygame.image.load('Assets/car.png').convert_alpha()

player.blit(player, (0,0))

pygame.display.set_caption("Player Test")

running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(player, (100,100))
    pygame.display.flip()