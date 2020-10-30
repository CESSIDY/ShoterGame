import pygame


class Projectile(object):
    def __init__(self, x, y, radius, color, facing, win=None, image=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.image = image
        self.win = win
        self.vel = 8 * facing

    def draw(self, win):
        if self.image:
            self.win.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
