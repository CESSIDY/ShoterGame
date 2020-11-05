import random
import pygame
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight, font, bg, bulletSound, hitSound, win, clock
from .BaseWorld import BaseWorld
import pyautogui
import ctypes


class StandardWorld(BaseWorld):
    def __init__(self, setting, player, win, enemys_generator, box_generator, events_generator):
        super().__init__(setting, player, win, enemys_generator, box_generator, events_generator)

    def __str__(self):
        return "Standart World"

    def uploadAccessData(self, player):
        super(StandardWorld, self).uploadAccessData(player)

    def isAccessWorld(self):
        return self.player.score < 1

    def isCloseWorld(self):
        return self.player.score > 1

    def generate(self):
        self.changeWinBgOnScreenshot()
        self.changeWinResolution()
        self.changePlayerSettingsToNewWin()
        self.changeEnemysSettingsToNewWin()
        self.changeEventSettingsToNewWin()
        self.changeBoxSettingsToNewWin()

    def draw(self):
        self.win.blit(self.settings['bg'], (0, 0))
        self.drawMovingObjects()
        self.drawHealthBar()
        self.drawScoreBar()
        pygame.display.update()

    def drawScoreBar(self):
        super(StandardWorld, self).drawScoreBar()

    def drawHealthBar(self):
        super(StandardWorld, self).drawHealthBar()

    def drawMovingObjects(self):
        self.enemys_generator.draw()
        self.box_generator.draw()
        self.player.draw()
        self.events_generator.draw()

    def changeWinBgOnScreenshot(self):
        self.settings['bg'] = pygame.image.load('resources/images/bg.jpg')
        self.win.blit(self.settings['bg'], (0, 0))

    def changeWinResolution(self):
        self.settings['ScreenWidth'] = 1100
        self.settings['ScreenHeight'] = 700
        pygame.display.set_mode((self.settings['ScreenWidth'], self.settings['ScreenHeight']))
        pygame.display.update()

    def changePlayerSettingsToNewWin(self):
        self.settings['playZoneYCoordinates'] = 550
        self.player.settings = self.settings
        self.player.defaultState()
        self.player.vel = 5
        self.player.max_bullets = 5

    def changeEnemysSettingsToNewWin(self):
        self.enemys_generator.settings = self.settings
        self.enemys_generator.max_enemys = 5
        self.enemys_generator.enemys = []

    def changeEventSettingsToNewWin(self):
        self.events_generator.settings = self.settings

    def changeBoxSettingsToNewWin(self):
        self.events_generator.settings = self.settings

    def start(self, keys, events):
        super(StandardWorld, self).start(keys, events)

    def drawLineToObjects(self):
        super(StandardWorld, self).drawLineToObjects()
