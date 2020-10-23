from .BaseBox import BaseBox
import pygame
import random
#from Settings import hitSound, ScreenWidth, ScreenHeight
from Projectlite import Projectile
from datetime import timedelta, datetime


class ShieldBox(BaseBox):
    def __init__(self, x, y, width, height, settings):
        super(ShieldBox, self).__init__(x, y, width, height, settings)
        self.box = pygame.transform.scale(pygame.image.load('resources/images/boxes/shield_box.png'), (30, 30))

    def draw(self, win):
        super(ShieldBox, self).draw(win)

    def move(self):
        super(ShieldBox, self).move()

    def take(self, player):  # This will display when the enemy is hit
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[
                2]:
                player.restart_date_time = datetime.now() + timedelta(seconds=5)
                self.visible = False
