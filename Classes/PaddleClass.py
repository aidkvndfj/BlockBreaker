import pygame
import math

WHITE = (255, 255, 255)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        # Set Image
        self.image = pygame.Surface((math.floor(WIDTH / 7), math.floor(HEIGHT / 33)))
        self.image.fill(WHITE)
        # Set Rect Values
        self.rect = self.image.get_rect()
        self.rect.centerx = math.floor(WIDTH / 2)
        self.rect.centery = math.floor(HEIGHT - 40)
        # Class Vars
        self.vel = 6
        self.screenWidth = WIDTH

    def update(self):
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_LEFT]):
            self.rect.centerx -= self.vel
        if (pressed[pygame.K_RIGHT]):
            self.rect.centerx += self.vel

        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > self.screenWidth):
            self.rect.right = self.screenWidth
