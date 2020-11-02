import random

import pygame
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight, font, bg, bulletSound, hitSound, win, clock
from Player import Player
from Projectlite import Projectile
from bin.Enemys.Generator import GenerateEnemys
from bin.Boxes.Generator import GenerateBoxes
from bin.Events.Generator import GenerateEvents
from bin.Enemys.BaseEnemys import BaseShotEnemy
import pyautogui
import ctypes

pygame.init()


class gameWindow(object):
    def __init__(self):
        self.settings = {
            'ScreenWidth': 1100,
            'ScreenHeight': 700,
            'playZoneYCoordinates': 550,
            'bg': pygame.image.load('resources/images/bg.jpg'),
            'font': pygame.font.SysFont("comicsans", 30, True),
            'bulletSound': pygame.mixer.Sound('resources/audio/bullet.wav'),
            'hitSound': pygame.mixer.Sound('resources/audio/hit.wav'),
            'music': pygame.mixer.music.load('resources/audio/music.wav')
        }
        self.win = pygame.display.set_mode((self.settings['ScreenWidth'], self.settings['ScreenHeight']))
        self.isWorldChange = False
        self.keys = list()
        self.events = list()
        self.player = Player(self.win, self.settings)
        self.enemys_generator = GenerateEnemys(self.player, self.win, self.settings)
        self.box_generator = GenerateBoxes(self.player, self.win, self.settings)
        self.events_generator = GenerateEvents(self.player, self.win, self.settings)
        pygame.display.set_caption("When will it all end?")
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.pause = False

    def draw(self):
        self.changeBg()
        self.drawMovingObjects()
        self.drawHealthBar()
        self.drawScoreBar()
        pygame.display.update()

    def drawScoreBar(self):
        text = self.settings['font'].render("Score: " + str(self.player.score), 1,
                                            (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        self.win.blit(text, (self.settings['ScreenWidth'] - 150, 10))

    def drawHealthBar(self):
        health_width = 50
        for _ in range(self.player.health):
            self.win.blit(
                pygame.transform.scale(pygame.image.load('resources/images/health.png'), (20, 20)),
                (health_width, 10))
            health_width += 20

    def drawMovingObjects(self):
        self.enemys_generator.draw()
        self.box_generator.draw()
        self.player.draw()
        self.events_generator.draw()

    def changeWinBgOnScreenshot(self):
        pygame.display.set_mode((1, 1))
        pygame.display.update()
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'screen_db.png')
        self.settings['bg'] = pygame.image.load('screen_db.png')

    def changeWinResolution(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.settings['ScreenWidth'] = screensize[0]
        self.settings['ScreenHeight'] = screensize[1]
        self.settings['playZoneYCoordinates'] = self.settings['ScreenHeight'] - 110
        pygame.display.set_mode((self.settings['ScreenWidth'], self.settings['ScreenHeight']), pygame.FULLSCREEN)

    def changePlayerSettingsToNewWin(self):
        self.player.settings = self.settings
        self.player.defaultState()
        self.player.vel += 1
        self.player.max_bullets = 10

    def changeEnemysSettingsToNewWin(self):
        self.enemys_generator.settings = self.settings
        self.enemys_generator.max_enemys = 10
        self.enemys_generator.enemys = []

    def changeEventSettingsToNewWin(self):
        self.events_generator.settings = self.settings

    def changeBoxSettingsToNewWin(self):
        self.events_generator.settings = self.settings

    def changeBg(self):
        if self.player.score > 1 and not self.isWorldChange:
            self.changeWinBgOnScreenshot()
            self.changeWinResolution()
            self.changePlayerSettingsToNewWin()
            self.changeEnemysSettingsToNewWin()
            self.changeEventSettingsToNewWin()
            self.changeBoxSettingsToNewWin()
            self.isWorldChange = True
        self.win.blit(self.settings['bg'], (0, 0))

    def start(self):
        run = True
        while run:
            clock.tick(30)
            self.keys = pygame.key.get_pressed()
            self.events = pygame.event.get()
            self.gamePause()
            run = self.isWindowClose()
            if not self.pause:
                self.enemys_generator.action()
                self.box_generator.action()
                self.events_generator.action(self.enemys_generator.enemys)
                self.events_generator.add_event(self.box_generator.events)
                self.player.action(self.keys, self.enemys_generator.enemys)
                self.draw()
            else:
                self.pauseMenu()

        pygame.quit()

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

    def gamePause(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if self.keys[pygame.K_ESCAPE] and not self.pause:
                    self.pause = True
                elif self.keys[pygame.K_ESCAPE] and self.pause:
                    self.pause = False

    def pauseMenu(self):
        text = self.settings['font'].render("PAUSE", 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        self.win.blit(text, (self.settings['ScreenWidth'] // 2, self.settings['ScreenHeight'] // 2))
        pygame.display.update()

    def isWindowClose(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return False
        return True


game_window = gameWindow()
game_window.start()
