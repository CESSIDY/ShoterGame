from .ScreenshotWorld import ScreenshotWorld
from .StandardWorld import StandardWorld
import pygame
from itertools import chain
from bin.Enemys.BaseEnemys import BaseShotEnemy
from bin.Enemys.Generator import GenerateEnemys
from bin.Events.Generator import GenerateEvents
from bin.Boxes.Generator import GenerateBoxes
from bin.Boxes.AirStrikeBox import AirStrileBox
from bin.Boxes.ShieldBox import ShieldBox
from bin.Enemys.Cowboy import Cowboy
from bin.Enemys.Goblin import Goblin
import numpy


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

    def action(self, keys, event, ai_mode=False):
        if self.activeWorld.isCloseWorld() or not self.activeWorld.isAccessWorld():
            for world in self.worlds:
                if world.isAccessWorld() and not world.isCloseWorld():
                    self.activeWorld = world
                    self.activeWorld.generate()
                    break

        self.activeWorld.start(keys, event)
        if ai_mode:
            self.drawLineToObjects()
            #self.getWorldInfo()

    def getWorldInfo(self):
        # will track the coordinates of only the first 10 boxes | [0] = type, [1] = x, [2] = y
        box_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        box_val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # will track the coordinates of only the first 20 bullets | [0] = direction (-1,1), [1] = x, [2] = y
        bullets_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        bullets_val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # will track the coordinates of 10 enemys | [0] = type, [1] = x, [2] = y, [3] = HP
        enemys_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        enemys_val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # will track the player | [0] = x, [1] = y, [2] = y, [3] = HP, [4] = SCORE
        player_array = [(self.player.x + self.player.width // 2), (self.player.y + self.player.height // 2), self.player.health, self.player.score, self.player.isProtected()]
        player_val = [(self.player.x + self.player.width // 2)]

        for key, box in enumerate(self.box_generator.boxes):
            try:
                if isinstance(box, AirStrileBox):
                    box_array[key][0] = 1
                    box_val[key] = (10_000 + (box.y + box.height // 2))
                elif isinstance(box, ShieldBox):
                    box_array[key][0] = 2
                    box_val[key] = (20_000 + (box.y + box.height // 2))
                else:
                    box_array[key][0] = 3
                    box_val[key] = (30_000 + (box.y + box.height // 2))
                box_array[key][1] = (box.x + box.width // 2)
                box_array[key][2] = (box.y + box.height // 2)
            except IndexError:
                break
            except ZeroDivisionError:
                continue

        for key, enemy in enumerate(self.enemys_generator.enemys):
            try:
                if isinstance(enemy, Cowboy):
                    enemys_array[key][0] = 1
                    enemys_val[key] = (((enemy.x + enemy.width // 2) * -1) + (enemy.health * 10000))
                else:
                    enemys_array[key][0] = 2
                    enemys_val[key] = (((enemy.x + enemy.width // 2) * 1) + (enemy.health * 10000))
                enemys_array[key][1] = (enemy.x + enemy.width // 2)
                enemys_array[key][2] = (enemy.y + enemy.height // 2)
                enemys_array[key][3] = (enemy.health)
            except IndexError:
                break
            except ZeroDivisionError:
                continue
            if isinstance(enemy, BaseShotEnemy):
                for b_key, bullet in enumerate(enemy.bullets):
                    try:
                        bullets_array[b_key][0] = bullet.facing
                        bullets_array[b_key][1] = bullet.x
                        bullets_array[b_key][2] = bullet.y
                        box_val[key] = (bullet.x * bullet.facing)
                    except IndexError:
                        break
                    except ZeroDivisionError:
                        continue
        result = player_array + list(chain(*box_array)) + list(chain(*enemys_array)) + list(chain(*bullets_array))
        return list(map(self.divisionOnNumberInList, result))
        #return player_val + box_val + enemys_val + bullets_val

    @staticmethod
    def divisionOnNumberInList(x):
        try:
            return 1 / x
        except ZeroDivisionError:
            return 0

    def drawLineToObjects(self):
        boxes = []
        bullets = []
        enemys = []
        player_center_cordiats = {'x': self.player.x + self.player.width // 2,
                                  'y': self.player.y + self.player.height // 2}
        for box in self.box_generator.boxes:
            pygame.draw.line(self.win, (0, 235, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                             [box.x + box.width // 2, box.y + box.height // 2], 1)
        for enemy in self.enemys_generator.enemys:
            pygame.draw.line(self.win, (183, 0, 70), (player_center_cordiats['x'], player_center_cordiats['y']),
                             (enemy.x + enemy.width // 2, enemy.y + enemy.height // 2), 1)
            if isinstance(enemy, BaseShotEnemy):
                for bullet in enemy.bullets:
                    pygame.draw.line(self.win, (183, 235, 0),
                                     [player_center_cordiats['x'], player_center_cordiats['y']],
                                     [bullet.x, bullet.y], 1)
        pygame.display.flip()
