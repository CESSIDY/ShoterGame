from .BaseBox import BaseBox
import pygame
import random
#from Settings import hitSound, ScreenWidth, ScreenHeight
from Projectlite import Projectile


class HealthBox(BaseBox):
    def __init__(self, x, y, width, height, settings):
        super(HealthBox, self).__init__(x, y, width, height, settings)
        self.box = pygame.transform.scale(pygame.image.load('resources/images/boxes/health_box.png').convert(), (30, 30))

    def __str__(self):
        return 'health'

    def draw(self, win):
        super(HealthBox, self).draw(win)

    def move(self):
        super(HealthBox, self).move()

    def take(self, player):  # This will display when the enemy is hit
        super(HealthBox, self).take(player)
