import random

from .HealthBox import HealthBox
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight


class GenerateBoxes(object):
    def __init__(self, player, win):
        self.boxes = []
        self.player = player
        self.win = win

    def generate(self):
        if random.randint(0, 300) == 0:
            what_y = random.randint(0, ScreenWidth - 30)
            box = HealthBox(what_y, -30, 30, 30)
            self.boxes.append(box)

    def action(self):
        self.generate()
        self.move()

    def draw(self):
        for box in self.boxes:
            box.draw(self.win)

    def move(self):
        for box in self.boxes:
            box.move()
            box.take(self.player)
            if not box.visible:
                try:
                    self.boxes.pop(self.boxes.index(box))
                except:
                    pass
