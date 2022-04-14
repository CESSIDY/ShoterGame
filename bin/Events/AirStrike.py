import os
import pygame
import random
from .BaseEven import BaseEven, BaseAttachedEven
from Projectlite import Projectile


class AirStrike(BaseAttachedEven):
    def __init__(self, x, y, width, height, settings):
        super(AirStrike, self).__init__()
        self.settings = settings
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fallCount = 0
        self.vel = 4
        self.hitbox = (self.x - 5, self.y - 5, width + 10, height + 10)
        self.visible = True

        path = 'resources/images/explosion/'
        self.fireball_imgs = [
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_0.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_1.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_2.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_3.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_4.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_5.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_6.png')).convert_alpha(), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'fireball_7.png')).convert_alpha(), (width, height))]

    def draw(self, win):
        if self.fallCount + 1 >= 21:
            self.fallCount = 0
        win.blit(self.fireball_imgs[self.fallCount // 3], (self.x, self.y))
        self.fallCount += 1
        self.hitbox = (self.x - 5, self.y - 5, self.width + 10, self.height + 10)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # Draws the hit box around the enemy

    def move(self, enemys, player):
        if self.settings['playZoneYCoordinates'] > self.y:
            self.y += self.vel
        else:
            for enemy in enemys:
                if enemy.hitbox[1] < self.hitbox[1] + self.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > \
                        self.hitbox[1]:
                    if enemy.hitbox[0] + enemy.hitbox[2] > self.hitbox[0] and enemy.hitbox[0] < self.hitbox[0] + \
                            self.hitbox[
                                2]:
                        enemy.die()
                        enemys.pop(enemys.index(enemy))  # removes bullet from bullet list
                        player.score += 1
            self.visible = False

    def get_event(self):
        return Explosion(self.x, self.y, self.settings)



class Explosion(BaseEven):
    def __init__(self, x, y, settings):
        super(Explosion, self).__init__()
        path = 'resources/images/explosion/'
        self.x = x
        self.y = y
        self.Count = 0
        self.visible = True
        base_width = 40
        base_height = 40
        self.explosion_imgs = [
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_00.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_01.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_02.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_03.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_04.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_05.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_06.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_07.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_08.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_09.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_10.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_11.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_12.png')).convert_alpha(),
                                   (base_width, base_height)),
            pygame.transform.scale(pygame.image.load(os.path.join(path, 'boom_13.png')).convert_alpha(),
                                   (base_width, base_height)), ]

    def draw(self, win):
        if self.Count + 1 >= 26:
            self.visible = False
        else:
            win.blit(self.explosion_imgs[self.Count // 2], (self.x, self.y))
            self.Count += 1
