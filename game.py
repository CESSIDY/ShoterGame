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


class RedrawGameWindows(object):
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
        self.keys = []
        self.player = Player(self.settings['ScreenWidth'] // 2, self.settings['playZoneYCoordinates'], 64, 64, self.win, self.settings)
        self.enemys_generator = GenerateEnemys(self.player, self.win, self.settings)
        self.box_generator = GenerateBoxes(self.player, self.win, self.settings)
        self.events_generator = GenerateEvents(self.player, self.win, self.settings)
        pygame.display.set_caption("First Game")
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()

    def draw(self):
        # Draw BackGround
        if self.player.score > 1 and not self.isWorldChange:
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            pygame.display.set_mode((1, 1))
            pygame.display.update()
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'screen_db.png')
            self.settings['bg'] = pygame.image.load('screen_db.png')
            self.settings['ScreenWidth'] = screensize[0]
            self.settings['ScreenHeight'] = screensize[1]
            self.settings['playZoneYCoordinates'] = screensize[1]-110
            self.player.settings = self.settings
            self.player.playZoneXCoordinates = screensize[0] // 2
            self.player.y = screensize[1]-110
            self.player.vel += 1
            self.player.max_bullets = 10
            self.enemys_generator.settings = self.settings
            self.enemys_generator.max_enemys = 10
            self.events_generator.settings = self.settings
            self.box_generator.settings = self.settings
            self.enemys_generator.enemys = []
            pygame.display.set_mode((screensize[0], screensize[1]), pygame.FULLSCREEN)
            self.isWorldChange = True
        self.win.blit(self.settings['bg'], (0, 0))
        # Draw Staff
        self.enemys_generator.draw()
        self.box_generator.draw()
        self.player.draw()
        self.events_generator.draw()
        # Draw Health point
        health_width = 50
        for _ in range(self.player.health):
            self.win.blit(
                pygame.transform.scale(pygame.image.load('resources/images/health.png'), (20, 20)),
                (health_width, 10))
            health_width += 20
        # Draw Score Bar
        text = self.settings['font'].render("Score: " + str(self.player.score), 1,
                           (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        self.win.blit(text, (self.settings['ScreenWidth'] - 150, 10))
        # Draw Bullets
        # Update display
        # draw_line_to_objects()
        pygame.display.update()

    def start(self):
        run = True
        while run:
            clock.tick(30)
            self.keys = pygame.key.get_pressed()
            run = self.isWindowClose()
            # Enemys
            self.enemys_generator.action()
            # Boxes
            self.box_generator.action()
            # Events
            self.events_generator.action(self.enemys_generator.enemys)
            self.events_generator.add_event(self.box_generator.events)
            # Player
            self.player.action(self.keys, self.enemys_generator.enemys)
            # Draw all staff
            # redrawGameWindow(base_bg, isWorldChange)
            self.draw()
        pygame.quit()

    def draw_line_to_objects(self):
        player_center_cordiats = {'x': self.player.x + self.player.width // 2, 'y': self.player.y + self.player.height // 2}
        for box in self.box_generator.boxes:
            pygame.draw.line(self.win, (0, 235, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                             [box.x + box.width // 2, box.y + box.height // 2], 1)
        for enemy in self.enemys_generator.enemys:
            pygame.draw.line(self.win, (183, 0, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                             [enemy.x + enemy.width // 2, enemy.y + enemy.height // 2], 1)
            if isinstance(enemy, BaseShotEnemy):
                for bullet in enemy.bullets:
                    pygame.draw.line(self.win, (183, 235, 0), [player_center_cordiats['x'], player_center_cordiats['y']],
                                     [bullet.x, bullet.y], 1)

    def isWindowClose(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if self.keys[pygame.K_ESCAPE]:
            return False
        return True

game_window = RedrawGameWindows()
game_window.start()

# def redrawGameWindow(base_bg, isWorldChange):
#     # Draw BackGround
#     if player.score > 2 and not isWorldChange:
#         myScreenshot = pyautogui.screenshot()
#         myScreenshot.save(r'screen_db.png')
#         base_bg = pygame.image.load('screen_db.png')
#         win.blit(base_bg, (0, 0))
#         print(isWorldChange)
#         isWorldChange = True
#         print(isWorldChange)
#     else:
#         win.blit(base_bg, (0, 0))
#     # Draw Staff
#     enemys_generator.draw()
#     box_generator.draw()
#     player.draw()
#     events_generator.draw()
#     # Draw Health point
#     health_width = 50
#     for _ in range(player.health):
#         win.blit(pygame.transform.scale(pygame.image.load('resources/images/health.png'), (20, 20)),
#                  (health_width, 10))
#         health_width += 20
#     # Draw Score Bar
#     text = font.render("Score: " + str(player.score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
#     win.blit(text, (ScreenWidth - 150, 10))
#     # Draw Bullets
#     # Update display
#     # draw_line_to_objects()
#     pygame.display.update()
#
#
# def draw_line_to_objects():
#     player_center_cordiats = {'x': player.x + player.width // 2, 'y': player.y + player.height // 2}
#     for box in box_generator.boxes:
#         pygame.draw.line(win, (0, 235, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
#                          [box.x + box.width // 2, box.y + box.height // 2], 1)
#     for enemy in enemys_generator.enemys:
#         pygame.draw.line(win, (183, 0, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
#                          [enemy.x + enemy.width // 2, enemy.y + enemy.height // 2], 1)
#         if isinstance(enemy, BaseShotEnemy):
#             for bullet in enemy.bullets:
#                 pygame.draw.line(win, (183, 235, 0), [player_center_cordiats['x'], player_center_cordiats['y']],
#                                  [bullet.x, bullet.y], 1)
#
#
# def isWindowClose():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             return False
#     if keys[pygame.K_ESCAPE]:
#         return False
#     return True
#
#
# # mainloop
# player = Player(ScreenWidth // 2, playZoneYCoordinates, 64, 64, win)
# box_generator = GenerateBoxes(player, win)
# isWorldChange = False
# base_bg = bg
# enemys_generator = GenerateEnemys(player, win)
# events_generator = GenerateEvents(player, win)
# run = True
# redraw_window = RedrawGameWindows(player=player, box_generator=box_generator, events_generator=events_generator,
#                                   enemys_generator=enemys_generator)
# while run:
#     clock.tick(30)
#     keys = pygame.key.get_pressed()
#     run = isWindowClose()
#     # Enemys
#     enemys_generator.action()
#     # Boxes
#     box_generator.action()
#     # Events
#     events_generator.action(enemys_generator.enemys)
#     events_generator.add_event(box_generator.events)
#     # Player
#     player.action(keys, enemys_generator.enemys)
#     # Draw all staff
#     # redrawGameWindow(base_bg, isWorldChange)
#     redraw_window.draw()
# pygame.quit()


