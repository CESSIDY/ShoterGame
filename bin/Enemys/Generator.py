import random

from .BaseEnemys import BaseShotEnemy
from .Goblin import Goblin
from .Cowboy import Cowboy
#from Settings import ScreenWidth, playZoneYCoordinates


class GenerateEnemys(object):
    def __init__(self, player, win, settings):
        self.settings = settings
        self.max_enemys = 5
        self.enemys = []
        self.player = player
        self.win = win

    def generate(self, fight=True, shot=False, fly=False):
        if len(self.enemys) < self.max_enemys:
            for _ in range(self.max_enemys - len(self.enemys)):
                what_x = [random.randint(self.settings['ScreenWidth'], self.settings['ScreenWidth'] + 200), random.randint(-200, 0)]
                x = random.choice(what_x)
                enemys_type = []
                if fight:
                    enemys_type.append(Goblin(x, self.settings['playZoneYCoordinates'], 64, 64, self.settings))
                if shot:
                    enemys_type.append(Cowboy(x, self.settings['playZoneYCoordinates'], 64, 64, self.settings))
                enemy = random.choice(enemys_type)
                self.enemys.append(enemy)

    def action(self):
        self.generate(shot=True)
        self.fight()

    def fight(self):
        for enemy in self.enemys:
            enemy.fight(self.player, self.win)

    def draw(self):
        for enemy in self.enemys:
            enemy.draw(self.win)
            # Draw Enemys Bullets
            if isinstance(enemy, BaseShotEnemy):
                enemy.drawBullets(self.win)
