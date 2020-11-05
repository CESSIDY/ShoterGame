import random
import pygame
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight, font, bg, bulletSound, hitSound, win, clock
from Player import Player
from Projectlite import Projectile
from bin.Enemys.Generator import GenerateEnemys
from bin.Boxes.Generator import GenerateBoxes
from bin.Events.Generator import GenerateEvents
from bin.Enemys.BaseEnemys import BaseShotEnemy
from bin.Worlds.Generator import GenerateWorlds
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
            'hitSound': pygame.mixer.Sound('resources/audio/hit.wav')
        }
        self.win = win
        self.worlds_generator = GenerateWorlds(self.settings, self.win)
        self.keys = list()
        self.events = list()
        pygame.display.set_caption("When will it all end?")
        pygame.mixer.music.load('resources/audio/music.wav')
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.pause = False

    def start(self):
        run = True
        self.worlds_generator.generate()
        while run:
            clock.tick(30)
            self.keys = pygame.key.get_pressed()
            self.events = pygame.event.get()
            self.gamePause()
            run = self.isWindowClose()
            if not self.pause:
                self.worlds_generator.action(self.keys, self.events)
            else:
                self.pauseMenu()

        pygame.quit()

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
