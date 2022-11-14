import pygame
import random

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space War")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Space.jpg")

# player variables
img_player = pygame.image.load("battleship.png")
player_x = 368
player_y = 500
player_x_change = 0

# enemy variables
img_enemy = pygame.image.load("aircraft.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 0.2
enemy_y_change = 50


# Player function
def player(x, y):
    screen.blit(img_player, (x, y))


# Enemy function
def enemy(x, y):
    screen.blit(img_enemy, (x, y))


# Game loop
is_running = True
while is_running:
    # Background image
    screen.blit(background, (0,0))

    # Events Interation
    for event in pygame.event.get():
        # Closing event
        if event.type == pygame.QUIT:
            is_running = False

        # Press arrow key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3

        # Release key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modify player location
    player_x += player_x_change

    # Keep player in screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Modify enemy location
    enemy_x += enemy_x_change

    # Keep enemy in screen
    if enemy_x <= 0:
        enemy_x_change = 0.2
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.2
        enemy_y += enemy_y_change


    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    # Update
    pygame.display.update()
