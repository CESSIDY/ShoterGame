from abc import ABC, abstractmethod
import pygame
from Settings import hitSound, ScreenWidth


class BaseFightEnemy(ABC):
    @abstractmethod
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        # True = from left, False = from right
        if x <= ScreenWidth//2:
            self.direction = True
        else:
            self.direction = False

    @abstractmethod
    def draw(self, win):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fight(self, player, win):
        pass

    @abstractmethod
    def hit(self):  # This will display when the enemy is hit
        pass


class BaseShotEnemy(ABC):
    @abstractmethod
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.bullets = []
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        # True = from left, False = from right
        if x <= ScreenWidth//2:
            self.direction = True
        else:
            self.direction = False

    @abstractmethod
    def draw(self, win):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fight(self, player, win):
        pass

    @abstractmethod
    def shot(self, player):
        pass

    @abstractmethod
    def hit(self):  # This will display when the enemy is hit
        pass

    def drawBullets(self, win):
        pass
