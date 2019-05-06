##############################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~ Created By: Eric ~~~~~#
#~~~~~~~~ May 3 2019 ~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##############################

#~~~~~~~~~~~ Setup ~~~~~~~~~~#
# Needed Imports
import pygame
import random
import sys
sys.path.insert(0, 'Classes')
from PaddleClass import *
from BallClass import *

# Constants
WIDTH = 960 # Width of screen
HEIGHT = 540 # Height of screen
FPS = 60 # frames per second

# Define The Colors
BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)

# Global Variables

# Other Variables
SpacePressed = False

# Initalize Pygame
pygame.init()
pygame.font.init()

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Create a screen that is WIDTH wide and HEIGHT tall
pygame.display.set_caption("Breakout Remake") # Name the window 'PySnake'

# Clock Setup For FPS
clock = pygame.time.Clock()

# Font/Text Setup
scoreFont = pygame.font.SysFont("Halvetica", 20)
scoreText = scoreFont.render("Score: {0}".format(0), False, (WHITE))

#~~~~~~~ Sprites Init ~~~~~~~#
# Sprite Groups
allSprites = pygame.sprite.Group()

# Sprites
paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT)

allSprites.add(paddle, ball)

#~~~~~~~~ Functions ~~~~~~~~~#

#~~~~~~ Main Game Loop ~~~~~~#
running = True
while (running):
    # print(spawnFood)
    clock.tick(FPS) # Set the Frames Per

    # Checks for ball, if not game over
    if (ball.alive == False):
        running = False

    # If space not pressed follow paddle
    if (SpacePressed == False):
        ball.FollowPaddle(paddle.rect.centerx, paddle.rect.y)

    # Sprite Collisions
    if (pygame.sprite.collide_rect(paddle, ball)):
        hitLocation = ball.rect.centerx - paddle.rect.x
        ball.HitPaddle(hitLocation, paddle.rect.width)

    # Check events whenever some input is given
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): # If the 'X' in the corner is clicked exit
            running = False
        if (event.type == pygame.KEYDOWN):
            key = pygame.key.get_pressed()
            if (key[pygame.K_SPACE]):
                SpacePressed = True

    # Updates the head
    allSprites.update()

    # Draw Frame
    screen.fill(BACKGROUND) # Gets rid of everything on the screen
    allSprites.draw(screen) # Draws the head

    # Show Frame
    pygame.display.flip() # Flips the display to show new frame

# Quit out of pygame
pygame.quit()
pygame.font.quit()
