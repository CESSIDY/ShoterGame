import pygame
from Settings import ScreenHeight, ScreenWidth, bulletSound, playZoneYCoordinates
from Projectlite import Projectile
from datetime import timedelta, datetime


class Player(object):
    walkRight = [pygame.image.load('resources/images/R1.png'), pygame.image.load('resources/images/R2.png'),
                 pygame.image.load('resources/images/R3.png'), pygame.image.load('resources/images/R4.png'),
                 pygame.image.load('resources/images/R5.png'), pygame.image.load('resources/images/R6.png'),
                 pygame.image.load('resources/images/R7.png'), pygame.image.load('resources/images/R8.png'),
                 pygame.image.load('resources/images/R9.png')]
    walkLeft = [pygame.image.load('resources/images/L1.png'), pygame.image.load('resources/images/L2.png'),
                pygame.image.load('resources/images/L3.png'), pygame.image.load('resources/images/L4.png'),
                pygame.image.load('resources/images/L5.png'), pygame.image.load('resources/images/L6.png'),
                pygame.image.load('resources/images/L7.png'), pygame.image.load('resources/images/L8.png'),
                pygame.image.load('resources/images/L9.png')]
    char = pygame.image.load('resources/images/standing.png')
    shield_width = 50
    shield_height = 50
    shield = pygame.transform.scale(pygame.image.load('resources/images/baff/shield.png'), (shield_width, shield_height))

    def __init__(self, x, y, width, height, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = win
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.shootLoop = 0
        self.bullets = []
        self.hitbox = (
            self.x + 20, self.y, 28, 60)  # The elements in the hitbox are (top left x, top left y, width, height)
        self.score = 0
        self.health = 4
        self.restart_date_time = datetime.now() + timedelta(seconds=2)
        self.saveZoneYCoordinates = playZoneYCoordinates - 100
        self.saveZoneXCoordinates = ScreenWidth // 2
        self.playZoneYCoordinates = playZoneYCoordinates
        self.playZoneXCoordinates = ScreenWidth // 2

    def action(self, keys, enemys):
        self.move(keys)
        self.shot(keys, enemys)

    def draw(self):
        self.drawBullets()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.restart_date_time >= datetime.now():
            shield_x = self.x + ((self.width - self.shield_width) / 2)
            shield_y = self.y + ((self.height - self.shield_height) / 2)
            self.win.blit(self.shield, (shield_x, shield_y))
        if not self.standing:
            if self.left:
                self.win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                self.win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                self.win.blit(self.walkRight[0], (self.x, self.y))
            else:
                self.win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.vel:
            if self.y == self.saveZoneYCoordinates:
                self.y = self.playZoneYCoordinates
            self.x -= int(self.vel)
            self.left = True
            self.right = False
            self.standing = False
        elif keys[pygame.K_RIGHT] and self.x + self.width + self.vel < ScreenWidth:
            if self.y == self.saveZoneYCoordinates:
                self.y = self.playZoneYCoordinates
            self.x += int(self.vel)
            self.left = False
            self.right = True
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0
        if not self.isJump:
            if keys[pygame.K_UP]:
                if self.y == self.saveZoneYCoordinates:
                    self.y = self.playZoneYCoordinates
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= int((self.jumpCount ** 2) * 0.5 * neg)
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def hit(self):
        print("RESTART TIME {}:".format(self.restart_date_time))
        if self.restart_date_time <= datetime.now():
            self.jumpCount = 10
            self.isJump = False
            self.x = self.playZoneXCoordinates
            self.y = self.playZoneYCoordinates
            self.walkCount = 0
            self.health -= 1
            self.restart_date_time = datetime.now() + timedelta(seconds=5)
            self.score -= 2
            if self.health <= 0:
                pygame.quit()
            # i = 0
            # while i < 300:
            #     pygame.time.delay(10)
            #     i += 1
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             i = 301
            #             pygame.quit()

    def shot(self, keys, enemys):
        if self.shootLoop > 0:
            self.shootLoop += 1
        if self.shootLoop > 3:
            self.shootLoop = 0
        for bullet in self.bullets:
            for enemy in enemys:
                if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > \
                        enemy.hitbox[1]:  # Checks x coords
                    if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + \
                            enemy.hitbox[2]:  # Checks y coords
                        enemy_alive = enemy.hit()  # calls enemy hit method
                        if not enemy_alive:
                            self.score += 1
                            enemys.pop(enemys.index(enemy))  # removes bullet from bullet list
                        try:
                            self.bullets.pop(self.bullets.index(bullet))  # removes bullet from bullet list
                        except:
                            pass
            if ScreenWidth > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                try:
                    self.bullets.pop(self.bullets.index(bullet))
                except:
                    pass

        if keys[pygame.K_SPACE] and self.shootLoop == 0:
            bulletSound.play()
            if self.left:
                facing = -1
            else:
                facing = 1
            if len(self.bullets) < 5:
                self.bullets.append(
                    Projectile(round(self.x + self.width // 2), round(self.y + self.height // 2), 6, (0, 0, 0), facing))
            self.shootLoop = 1

    def drawBullets(self):
        for bullet in self.bullets:
            bullet.draw(self.win)
