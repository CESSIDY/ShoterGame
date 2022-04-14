import random
import pygame
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight, font, bg, bulletSound, hitSound, win, clock
from .BaseWorld import BaseWorld
import pyautogui
import ctypes
from ..Players.AIPlayer import AIPlayer


class ScreenshotWorld(BaseWorld):
    def __init__(self, setting, player, win, enemys_generator, box_generator, events_generator):
        super().__init__(setting, player, win, enemys_generator, box_generator, events_generator)

    def __str__(self):
        return "Screenshot World"

    def uploadAccessData(self, player):
        super(ScreenshotWorld, self).uploadAccessData(player)

    def isAccessWorld(self):
        return self.player.score > 1

    def isCloseWorld(self):
        return self.player.score > 5

    def generate(self):
        self.changeWinBg()
        self.changeWinResolution()
        self.changePlayerSettings()
        self.changeEnemysSettings()
        self.changeEventSettings()
        self.changeBoxSettings()

    def draw(self):
        self.win.blit(self.settings['bg'], (0, 0))
        self.drawMovingObjects()
        self.drawHealthBar()
        self.drawScoreBar()
        pygame.display.update()

    def drawScoreBar(self):
        super(ScreenshotWorld, self).drawScoreBar()

    def drawHealthBar(self):
        super(ScreenshotWorld, self).drawHealthBar()

    def drawMovingObjects(self):
        self.enemys_generator.draw()
        self.box_generator.draw()
        self.player.draw()
        self.events_generator.draw()

    def changeWinBg(self):
        pygame.display.set_mode((1, 1))
        pygame.display.update()
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'screen_db.png')
        self.settings['bg'] = pygame.image.load('screen_db.png').convert()
        self.win.blit(self.settings['bg'], (0, 0))

    def changeWinResolution(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.settings['ScreenWidth'] = screensize[0]
        self.settings['ScreenHeight'] = screensize[1]
        self.settings['playZoneYCoordinates'] = self.settings['ScreenHeight'] - 110
        pygame.display.set_mode((self.settings['ScreenWidth'], self.settings['ScreenHeight']), pygame.FULLSCREEN)

    def changePlayerSettings(self):
        self.player.settings = self.settings
        self.player.defaultState()
        self.player.vel = 6
        self.player.max_bullets = 10

    def changeEnemysSettings(self):
        self.enemys_generator.settings = self.settings
        self.enemys_generator.max_enemys = 10
        self.enemys_generator.enemys = []

    def changeEventSettings(self):
        self.events_generator.settings = self.settings

    def changeBoxSettings(self):
        self.events_generator.settings = self.settings

    def start(self, keys, events):
        super(ScreenshotWorld, self).start(keys, events)

    def drawLineToObjects(self):
        super(ScreenshotWorld, self).drawLineToObjects()
