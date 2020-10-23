import random

from .BaseEven import BaseEven, BaseAttachedEven
from .AirStrike import AirStrike
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight


class GenerateEvents(object):
    def __init__(self, player, win, settings):
        self.settings = settings
        self.events = []
        self.player = player
        self.win = win
        self.enemys = []

    def generate(self):
        pass

    def add_event(self, events):
        for event in events:
            self.events.append(event)

    def action(self, enemys):
        self.enemys = enemys
        self.move()

    def draw(self):
        for event in self.events:
            event.draw(self.win)

    def move(self):
        for event in self.events:
            if not isinstance(event, BaseEven):
                event.move(self.enemys, self.player)
            if not event.visible:
                if isinstance(event, BaseAttachedEven):
                    self.add_event([event.get_event()])
                try:
                    self.events.pop(self.events.index(event))
                except:
                    pass
