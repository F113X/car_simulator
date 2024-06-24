import pygame
import random

# Initialize the game
pygame.init()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # Highlight the button when the mouse hovers over it
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, self.rect)
        return action

# Set up the game window
screen_width = 840
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)



speed = 0

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Load game assets
background = pygame.image.load('Assets/road1.png').convert_alpha()

# Set up the start button
start_text = font.render("Start", True, white)
start_button = Button(420 - start_text.get_rect().width/2, 400, start_text, 1)

# Set up the title text
title_text = font.render("Car Game", True, white)
title_text_size = title_text.get_rect().width

def roadMove(roadSpeed):
    screen.blit(background, (0, roadSpeed))
    screen.blit(background, (0, roadSpeed - 650))

def game_over():
    game_over_text = font.render("Game Over. Press 'space' to restart", True, white)
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
    pygame.display.update()

    pygame.quit()
    quit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(title_text, (420 - title_text_size / 2, 100))

    if start_button.draw(screen):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            # Render the game
            screen.blit(background, (0, 0))
            roadMove(speed)
            pygame.display.flip()

    pygame.display.flip()

pygame.quit()
quit()