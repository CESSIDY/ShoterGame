from .BaseEnemys import BaseShotEnemy
import pygame
import random
from Settings import hitSound, ScreenWidth
from Projectlite import Projectile


class Cowboy(BaseShotEnemy):
    def __init__(self, x, y, width, height):
        super(Cowboy, self).__init__(x, y, width, height)
        self.walkRight = [pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_0.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_1.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_2.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_3.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_4.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_5.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_6.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_7.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_8.png'), (50, 61)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_9.png'), (50, 61))]
        self.walkLeft = [pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_0.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_1.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_2.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_3.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_4.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_5.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_6.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_7.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_8.png'), (50, 61)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_9.png'), (50, 61))]

    def draw(self, win):
        super(Cowboy, self).draw(win)

    def move(self):
        super(Cowboy, self).move()

    def fight(self, player, win):
        super(Cowboy, self).fight(player, win)
        # This will go at the top of or main loop.

    def shot(self, player):
        super(Cowboy, self).shot(player)

    def hit(self):  # This will display when the enemy is hit
        return super(Cowboy, self).hit()

    def drawBullets(self, win):
        super(Cowboy, self).drawBullets(win)
