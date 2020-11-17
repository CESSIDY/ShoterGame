import pygame, sys
# from Settings import ScreenHeight, ScreenWidth, bulletSound, playZoneYCoordinates
from Projectlite import Projectile
from datetime import timedelta, datetime


class BasePlayer(object):
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
    bullet_img_left = pygame.transform.scale(pygame.image.load('resources/images/bullets/bullet4_left.png'), (10, 10))
    bullet_img_right = pygame.transform.scale(pygame.image.load('resources/images/bullets/bullet4_right.png'), (10, 10))
    shield_width = 50
    shield_height = 50
    shield = pygame.transform.scale(pygame.image.load('resources/images/baff/shield.png'),
                                    (shield_width, shield_height))

    def __init__(self, win, settings):
        self.x = int(settings['ScreenWidth'] // 2)
        self.y = int(settings['playZoneYCoordinates'])
        self.width = 64
        self.height = 64
        self.win = win
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.shootLoop = 0
        self.max_bullets = 5
        self.bullets = []
        self.hitbox = (
            self.x + 20, self.y, 28, 60)  # The elements in the hitbox are (top left x, top left y, width, height)
        self.score = 0
        self.health = 4
        self.settings = settings
        self.restart_date_time = datetime.now() + timedelta(seconds=4)

    def defaultState(self):
        self.jumpCount = 10
        self.isJump = False
        self.x = self.settings['ScreenWidth'] // 2
        self.y = self.settings['playZoneYCoordinates']
        self.walkCount = 0
        self.shootLoop = 0
        self.restart_date_time = datetime.now() + timedelta(seconds=4)

    def action(self, keys, enemys):
        self.move(keys)
        self.shot(keys, enemys)

    def RestartWalkCountIfAnimationEnd(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

    def DrawShield(self):
        if self.restart_date_time >= datetime.now():
            shield_x = self.x + ((self.width - self.shield_width) / 2)
            shield_y = self.y + ((self.height - self.shield_height) / 2)
            self.win.blit(self.shield, (shield_x, shield_y))

    def DrawWalk(self):
        if self.left:
            self.win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            self.win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def DrawStanding(self):
        if self.right:
            self.win.blit(self.walkRight[0], (self.x, self.y))
        else:
            self.win.blit(self.walkLeft[0], (self.x, self.y))

    def updateHitBox(self):
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self):
        self.drawBullets()
        self.RestartWalkCountIfAnimationEnd()
        self.DrawShield()
        if not self.standing:
            self.DrawWalk()
        else:
            self.DrawStanding()
        self.updateHitBox()

    def isMoveLeft(self, keys):
        return keys[pygame.K_LEFT] and self.x > self.vel

    def MoveLeft(self):
        self.x -= int(self.vel)
        self.left = True
        self.right = False
        self.standing = False

    def isMoveRight(self, keys):
        return keys[pygame.K_RIGHT] and self.x + self.width + self.vel < self.settings['ScreenWidth']

    def MoveRight(self):
        self.x += int(self.vel)
        self.left = False
        self.right = True
        self.standing = False

    def Standing(self):
        self.standing = True
        self.walkCount = 0

    def Jump(self, keys):
        if keys[pygame.K_UP]:
            self.isJump = True
            self.right = False
            self.left = False
            self.walkCount = 0

    def isInAirAfterJump(self):
        return self.jumpCount >= -10

    def JumpAction(self):
        neg = 1
        if self.jumpCount < 0:
            neg = -1
        self.y -= int((self.jumpCount ** 2) * 0.5 * neg)
        self.jumpCount -= 1

    def JumpStop(self):
        self.isJump = False
        self.jumpCount = 10

    def move(self, keys):
        if self.isMoveLeft(keys):
            self.MoveLeft()
        elif self.isMoveRight(keys):
            self.MoveRight()
        else:
            self.Standing()
        if not self.isJump:
            self.Jump(keys)
        else:
            if self.isInAirAfterJump():
                self.JumpAction()
            else:
                self.JumpStop()

    def isProtected(self):
        return self.restart_date_time >= datetime.now()

    def hit(self):
        if not self.isProtected():
            self.defaultState()
            self.health -= 1
            self.score -= 2
            if self.health <= 0:
                print(self.score)
                pygame.quit()
                sys.exit()

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
            if self.settings['ScreenWidth'] > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                try:
                    self.bullets.pop(self.bullets.index(bullet))
                except:
                    pass

        if keys[pygame.K_SPACE] and self.shootLoop == 0:
            if self.left:
                facing = -1
            else:
                facing = 1
            if len(self.bullets) < self.max_bullets:
                self.settings['bulletSound'].play()
                if facing == -1:
                    byll_img = self.bullet_img_left
                else:
                    byll_img = self.bullet_img_right
                self.bullets.append(
                    Projectile(round(self.x + self.width // 2), round(self.y + self.height // 2), 6, (0, 0, 0), facing,
                               win=self.win, image=byll_img))
            self.shootLoop = 1

    def drawBullets(self):
        for bullet in self.bullets:
            bullet.draw(self.win)
