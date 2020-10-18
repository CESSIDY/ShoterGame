import random

from .BaseEnemys import BaseShotEnemy
from .Goblin import Goblin
from .Cowboy import Cowboy
from Settings import ScreenWidth, playZoneYCoordinates


class GenerateEnemys(object):
    def __init__(self, player, win):
        self.enemys = []
        self.player = player
        self.win = win

    def generate(self, fight=True, shot=False, fly=False):
        if len(self.enemys) < 5:
            for i in range(5 - len(self.enemys)):
                what_x = [random.randint(ScreenWidth, ScreenWidth + 200), random.randint(-200, 0)]
                x = random.choice(what_x)
                enemys_type = []
                if fight:
                    enemys_type.append(Goblin(x, playZoneYCoordinates, 64, 64))
                if shot:
                    enemys_type.append(Cowboy(x, playZoneYCoordinates, 64, 64))
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
