from .BaseBox import BaseEventBox
import pygame
import random
#from Settings import hitSound, ScreenWidth, ScreenHeight
from Projectlite import Projectile
from datetime import timedelta, datetime

from ..Events.AirStrike import AirStrike


class AirStrileBox(BaseEventBox):
    def __init__(self, x, y, width, height, settings):
        super(AirStrileBox, self).__init__(x, y, width, height, settings)
        self.box = pygame.transform.scale(pygame.image.load('resources/images/boxes/air_strike_box.png').convert(), (30, 30))

    def __str__(self):
        return 'air strike'

    def draw(self, win):
        super(AirStrileBox, self).draw(win)

    def move(self):
        super(AirStrileBox, self).move()

    def take(self, player):  # This will display when the enemy is hit
        super(AirStrileBox, self).take(player)

    def get_event(self):
        events = []
        for i in range(random.randrange(1, 21)):
            what_y = random.randint(0, self.settings['ScreenWidth'] - 30)
            what_x = random.randint(-200, 0)
            events.append(AirStrike(what_y, what_x, 30, 30, self.settings))
        return events
