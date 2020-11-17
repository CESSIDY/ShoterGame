from .ScreenshotWorld import ScreenshotWorld
from .StandardWorld import StandardWorld
import pygame
from bin.Enemys.BaseEnemys import BaseShotEnemy
from bin.Enemys.Generator import GenerateEnemys
from bin.Events.Generator import GenerateEvents
from bin.Boxes.Generator import GenerateBoxes


class GenerateWorlds(object):
    def __init__(self, setting, win, player):
        self.settings = setting
        self.win = win
        self.player = player
        self.enemys_generator = GenerateEnemys(self.player, self.win, self.settings)
        self.box_generator = GenerateBoxes(self.player, self.win, self.settings)
        self.events_generator = GenerateEvents(self.player, self.win, self.settings)
        self.worlds = list()
        self.activeWorld = StandardWorld(self.settings, self.player, self.win, self.enemys_generator,
                                         self.box_generator,
                                         self.events_generator)
        self.generate()

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
                if world.isAccessWorld() and not world.isCloseWorld():
                    self.activeWorld = world
                    self.activeWorld.generate()
                    break

        self.activeWorld.start(keys, event)
        self.drawLineToObjects()

    def drawLineToObjects(self):
        player_center_cordiats = {'x': self.player.x + self.player.width // 2,
                                  'y': self.player.y + self.player.height // 2}
        for box in self.box_generator.boxes:
            pygame.draw.line(self.win, (0, 235, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                             [box.x + box.width // 2, box.y + box.height // 2], 1)
        for enemy in self.enemys_generator.enemys:
            pygame.draw.line(self.win, (183, 0, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                             [enemy.x + enemy.width // 2, enemy.y + enemy.height // 2], 1)
            if isinstance(enemy, BaseShotEnemy):
                for bullet in enemy.bullets:
                    pygame.draw.line(self.win, (183, 235, 0),
                                     [player_center_cordiats['x'], player_center_cordiats['y']],
                                     [bullet.x, bullet.y], 1)
