import pygame
import random
# Initialize the game
pygame.init()

# Set up the game window
screen_width = 840
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")
background = pygame.image.load('Assets/road1.png').convert_alpha()

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the player
player_width = 50
player_height = 110
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10
player = pygame.image.load('Assets/car.png').convert_alpha()

# Set up the obstacles

truck1 = pygame.image.load('Assets/truck1.png').convert_alpha()
truck2 = pygame.image.load('Assets/truck2.png').convert_alpha()
truck3 = pygame.image.load('Assets/truck3.png').convert_alpha()
truck4 = pygame.image.load('Assets/truck4.png').convert_alpha()
truck5 = pygame.image.load('Assets/truck5.png').convert_alpha()
bus = pygame.image.load('Assets/bus.png').convert_alpha()

obstacle_width = [50,45,50,55,60,55]
obstacle_height = 120
obstacle_x = random.randint(150, screen_width - obstacle_width-150)
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle = [truck1, truck2, truck3, truck4, truck5, bus]

# Set up coins
coin_width = 32
coin_height = 38
coin_x = random.randint(150, 680)
coin_y = -coin_height
coin = pygame.image.load('Assets/coin.png').convert_alpha()

speed = 0
chanceTop = 2500

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

def roadMove(roadSpeed):
    background.blit(background, (0,roadSpeed))
    background.blit(background, (0,roadSpeed - 650))

def show_score():
    #Displays the current score on the screen.

    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

def game_over():
    #Displays the game over message and quits the game.

    game_over_text = font.render("Game Over. Press 'space' to restart", True, white)
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
    pygame.display.update()

    pygame.quit()
    quit()

# Game loop
running = True
clock = pygame.time.Clock()

def shop():
    print('welcome to shop :)')

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x >= 150:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x <= 680:
        player_x += player_speed
    if keys[pygame.K_UP] and speed <= 20:
        speed += 0.3
    if keys[pygame.K_DOWN] or keys[pygame.K_SPACE] and speed >= 0:
       speed -= 0.7
    if keys[pygame.K_UP] == False and speed >= 0:
        speed -= 0.1
    
    if speed <= 0.5:
        player_speed = 0
    if speed > 0.5 and speed <= 10:
        player_speed = 3
    if speed > 10:
        player_speed = 7

    # Update the obstacles
    obstacle_y += speed + obstacle_speed
    if obstacle_y > screen_height:
        obstacle_x = random.randint(150, 650)
        obstacle_y = -obstacle_height

    chance1 = random.randint(1,chanceTop)
    chance2 = random.randint(1,10)

    print(chance1,chance2,chance1 // chance2)

    coin_y += speed
    if coin_y > screen_height:
        if chance1 // chance2 == 1:
            coin_x = random.randint(150, 680)
            coin_y = -coin_height

    if player_x < coin_x + coin_width and player_x + player_width > coin_x and player_y < coin_y + coin_height and player_y + player_height > coin_y:
        coin_x = random.randint(150, 680)
        coin_y = -coin_height
        score += 1

    # Check for collision
    if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
        game_over()


    screen.blit(background, (0, 0))
    roadMove(speed)

    # Draw the player
    screen.blit(player, (player_x, player_y))

    # Draw the obstacles
    screen.blit(obstacle, (obstacle_x, obstacle_y))

    # Draw coins
    screen.blit(coin, (coin_x, coin_y))

    # Display the score
    show_score()

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
print(score)
quit()
