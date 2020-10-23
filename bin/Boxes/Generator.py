import random
from .BaseBox import BaseEventBox
from .HealthBox import HealthBox
from .ShieldBox import ShieldBox
from .AirStrikeBox import AirStrileBox
#from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight


class GenerateBoxes(object):
    def __init__(self, player, win, settings):
        self.settings = settings
        self.boxes = []
        self.player = player
        self.win = win
        self.events = []

    def generate(self):
        if random.randint(0, 300) == 0:
            what_y = random.randint(0, self.settings['ScreenWidth'] - 30)
            boxes = []
            boxes.append(ShieldBox(what_y, -30, 30, 30, self.settings))
            boxes.append(HealthBox(what_y, -30, 30, 30, self.settings))
            boxes.append(AirStrileBox(what_y, -30, 30, 30, self.settings))
            box = random.choice(boxes)
            self.boxes.append(box)

    def action(self):
        self.generate()
        self.move()

    def draw(self):
        for box in self.boxes:
            box.draw(self.win)

    def move(self):
        events = []
        for box in self.boxes:
            box.move()
            box.take(self.player)
            if not box.visible:
                if isinstance(box, BaseEventBox) and box.take_box:
                    temp_event = box.get_event()
                    if isinstance(temp_event, list):
                        events += temp_event
                    else:
                        events.append(temp_event)
                try:
                    self.boxes.pop(self.boxes.index(box))
                except:
                    pass
        self.events = events
