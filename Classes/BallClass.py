import pygame
import Eric_Dumb_Module as edm

GREEN = (0, 255, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        # Set Image
        self.image = pygame.Surface((WIDTH / 90, WIDTH / 90))
        self.image.fill(GREEN)
        # Set Rect Values
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2, HEIGHT / 2))
        # Class Vars
        self.vel = edm.Vector(2, -2)
        self.screenWidth = WIDTH
        self.screenHeight = HEIGHT
        self.alive = True

    def update(self):
        # Move ball based on x and y vels
        self.rect.centerx += self.vel.x
        self.rect.centery += self.vel.y

        # Check for collision on walls and if hit bottom
        if (self.rect.left < 0 or self.rect.right > self.screenWidth):
            self.vel.x *= -1
        if (self.rect.top < 0):
            self.vel.y *= -1
        if (self.rect.top > self.screenHeight):
            self.alive = False
            self.kill()
