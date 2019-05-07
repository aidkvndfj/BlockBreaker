import pygame
import Eric_Dumb_Module as edm
import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 130, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, xPos, yPos, type):
        pygame.sprite.Sprite.__init__(self)
        # Set Image
        self.image = pygame.Surface((WIDTH / 20, HEIGHT / 35))
        self.image.fill(ORANGE)
        # Set Rect Values
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
        # Class Vars
        self.screenWidth = WIDTH
        self.screenHeight = HEIGHT
        self.alive = True
        self.type = type
