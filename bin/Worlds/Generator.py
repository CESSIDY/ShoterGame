import random
from .ScreenshotWorld import ScreenshotWorld
from .StandardWorld import StandardWorld
from Player import Player
from bin.Enemys.Generator import GenerateEnemys
from bin.Events.Generator import GenerateEvents
from bin.Boxes.Generator import GenerateBoxes


class GenerateWorlds(object):
    def __init__(self, setting, win):
        self.settings = setting
        self.win = win
        self.player = Player(self.win, self.settings)
        self.enemys_generator = GenerateEnemys(self.player, self.win, self.settings)
        self.box_generator = GenerateBoxes(self.player, self.win, self.settings)
        self.events_generator = GenerateEvents(self.player, self.win, self.settings)
        self.worlds = list()
        self.activeWorld = StandardWorld(self.settings, self.player, self.win, self.enemys_generator,
                                         self.box_generator,
                                         self.events_generator)

    def generate(self):
        self.worlds.append(
            StandardWorld(self.settings, self.player, self.win, self.enemys_generator, self.box_generator,
                          self.events_generator))
        self.worlds.append(
            ScreenshotWorld(self.settings, self.player, self.win, self.enemys_generator, self.box_generator,
                            self.events_generator))

    def action(self, keys, event):
        if self.activeWorld.isCloseWorld() or not self.activeWorld.isAccessWorld():
            for world in self.worlds:
                print(world)
                if world.isAccessWorld() and not world.isCloseWorld():
                    self.activeWorld = world
                    self.activeWorld.generate()
                    break

        self.activeWorld.start(keys, event)
