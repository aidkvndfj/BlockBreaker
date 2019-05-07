import pygame
import Eric_Dumb_Module as edm
import math

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
        self.vel = 4
        self.speed = edm.Vector(0, -7)
        self.screenWidth = WIDTH
        self.screenHeight = HEIGHT
        self.alive = True

    def update(self):
        # Check for collision on walls and if hit bottom
        # Hit Top
        if (self.rect.y <= 0):
            # self.rect.y += self.vel
            self.speed.y = abs(self.speed.y)

        # Hit Left
        if (self.rect.x <= 0):
            # self.rect.x += self.vel
            self.speed.x = abs(self.speed.x)

        # Hit Right
        if (self.rect.x + self.rect.width > self.screenWidth):
            # self.rect.x -= self.vel
            self.speed.x = -abs(self.speed.x)

        # Hit Bottom
        if (self.rect.y > self.screenHeight):
            # print("y pos: {0}, screen height: {1}".format(self.rect.y, self.screenHeight))
            self.alive = False
            self.kill()

        # Move ball based on x and y speeds
        self.rect.centerx += self.speed.x
        self.rect.centery += self.speed.y

    def HitPaddle(self, location, paddleWidth):
        # self.rect.y -= self.vel
        angleDeg = edm.map(location, -1, paddleWidth, 5, 175) # Degrees
        angleRad = angleDeg * math.pi / 180
        self.speed.x = -self.vel * math.cos(angleRad)
        # print("X Speed: {0}".format(self.speed.x))
        self.speed.y = -abs(1 * (self.vel * math.sin(angleRad)))
        # print("Y Speed: {0}".format(self.speed.y))
        # print("Angle: {0}".format(angleDeg))
        # print("Vel: {0}\n".format(math.sqrt(pow(self.speed.x, 2) + pow(self.speed.y, 2))))

    def FollowPaddle(self, paddleX, paddleY):
        self.rect.centerx = paddleX
        self.rect.centery = paddleY

    def bottomBounce(self):
        self.speed.y = abs(self.speed.y)
