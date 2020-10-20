from abc import ABC, abstractmethod
import random
import pygame
from Settings import hitSound, ScreenWidth, ScreenHeight
from Projectlite import Projectile


class BaseBox(ABC):
    @abstractmethod
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - 5, self.y - 5, 40, 40)
        self.visible = True

    @abstractmethod
    def draw(self, win):
        win.blit(self.box, (self.x, self.y))
        self.hitbox = (self.x - 5, self.y - 5, 40, 40)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # Draws the hit box around the enemy

    @abstractmethod
    def move(self):
        if ScreenHeight > self.y:
            self.y += self.vel
        else:
            self.visible = False

    @abstractmethod
    def take(self, player):  # This will display when the enemy is hit
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[
                2]:
                if player.health < 4:
                    player.health += 1
                self.visible = False