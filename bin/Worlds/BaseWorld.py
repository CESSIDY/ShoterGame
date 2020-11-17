from abc import ABC, abstractmethod
import pygame
from bin.Enemys.BaseEnemys import BaseShotEnemy



class BaseWorld(ABC):
    def __init__(self, setting, player, win, enemys_generator, box_generator, events_generator):
        self.settings = setting
        self.win = win
        self.isWorldChange = False
        self.player = player
        self.enemys_generator = enemys_generator
        self.box_generator = box_generator
        self.events_generator = events_generator

    @abstractmethod
    def uploadAccessData(self, player):
        self.player = player

    def isAccessWorld(self):
        pass

    def isCloseWorld(self):
        pass

    def worldClose(self):
        pass

    def generate(self):
        pass

    def draw(self):
        pass

    @abstractmethod
    def start(self, keys, events):
        self.keys = keys
        self.events = events
        self.enemys_generator.action()
        self.box_generator.action()
        self.events_generator.action(self.enemys_generator.enemys)
        self.events_generator.add_event(self.box_generator.events)
        self.player.action(self.keys, self.enemys_generator.enemys)
        self.draw()

    @abstractmethod
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

    @abstractmethod
    def drawScoreBar(self):
        text = self.settings['font'].render("Score: " + str(self.player.score), 1,
                                            (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        self.win.blit(text, (self.settings['ScreenWidth'] - 150, 10))

    @abstractmethod
    def drawHealthBar(self):
        health_width = 50
        for _ in range(self.player.health):
            self.win.blit(
                pygame.transform.scale(pygame.image.load('resources/images/health.png'), (20, 20)),
                (health_width, 10))
            health_width += 20
