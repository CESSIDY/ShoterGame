import random

from .Goblin import Goblin
from .Cowboy import Cowboy


class GenerateEnemys(object):
    def __init__(self):
        pass

    def generate(self, enemys, fight=True, shot=False, fly=False):
        if len(enemys) < 5:
            for i in range(5 - len(enemys)):
                what_x = [random.randint(1000, 1100), random.randint(-100, 0)]
                x = random.choice(what_x)
                enemys_type = []
                if fight:
                    enemys_type.append(Goblin(x, 550, 64, 64))
                if shot:
                    enemys_type.append(Cowboy(x, 550, 64, 64))
                enemy = random.choice(enemys_type)
                enemys.append(enemy)

        return enemys
