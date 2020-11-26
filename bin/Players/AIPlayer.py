import pygame, sys
# from Settings import ScreenHeight, ScreenWidth, bulletSound, playZoneYCoordinates
from Projectlite import Projectile
from datetime import timedelta, datetime
from bin.Players.BasePlayer import BasePlayer
from bin.Enemys.BaseEnemys import BaseShotEnemy


class AIPlayer(BasePlayer):
    def __init__(self, win, settings):
        super().__init__(win, settings)

    def defaultState(self):
        super(AIPlayer, self).defaultState()

    def action(self, keys, enemys):
        super(AIPlayer, self).action(keys, enemys)

    def RestartWalkCountIfAnimationEnd(self):
        super(AIPlayer, self).RestartWalkCountIfAnimationEnd()

    def DrawShield(self):
        super(AIPlayer, self).DrawShield()

    def DrawWalk(self):
        super(AIPlayer, self).DrawWalk()

    def DrawStanding(self):
        super(AIPlayer, self).DrawStanding()

    def updateHitBox(self):
        super(AIPlayer, self).updateHitBox()

    def draw(self):
        super(AIPlayer, self).draw()

    def isMoveLeft(self, keys):
        return keys[0] > 0 and self.x > self.vel

    def MoveLeft(self):
        super(AIPlayer, self).MoveLeft()

    def isMoveRight(self, keys):
        return keys[1] > 0 and self.x + self.width + self.vel < self.settings['ScreenWidth']

    def MoveRight(self):
        super(AIPlayer, self).MoveRight()

    def Standing(self):
        super(AIPlayer, self).Standing()

    def Jump(self, keys):
        if keys[2] > 0:
            self.isJump = True
            self.right = False
            self.left = False
            self.walkCount = 0

    def isInAirAfterJump(self):
        return super(AIPlayer, self).isInAirAfterJump()

    def JumpAction(self):
        super(AIPlayer, self).JumpAction()

    def JumpStop(self):
        super(AIPlayer, self).JumpStop()

    def move(self, keys):
        super(AIPlayer, self).move(keys)

    def isProtected(self):
        return super(AIPlayer, self).isProtected()

    def hit(self):
        if not self.isProtected():
            self.defaultState()
            self.health -= 1
            self.score -= 2

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

        if keys[3] > 0 and self.shootLoop == 0:
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

    def isJumpedSomething(self, enemys):
        object_count = 0
        if not self.isProtected():
            player_center_x = self.x + self.width // 2
            player_down_y = self.y + self.height
            for e_key, enemy in enumerate(enemys):
                enemy_center_x = enemy.x + enemy.width // 2
                if isinstance(enemy, BaseShotEnemy):
                    for key, bullet in enumerate(enemy.bullets):
                        # 8 is the speed at which a bullet flies in one cycles
                        # (self.jumpCount ** 2) * 0.5 * neg - the player jumps and falls according to this formula
                        # if the player is less than 146 (4 cycles) on the bullet then he will fall on it and die.
                        if bullet.x <= player_center_x <= bullet.x + 8:  # on right side
                            if bullet.facing == 1 and bullet.x - 8 <= player_center_x - 8 <= bullet.x:
                                pass
                            elif player_down_y + 138 <= bullet.y + enemy.height//2:
                                object_count += 1
                        elif bullet.x - 8 <= player_center_x <= bullet.x:  # on left side
                            if bullet.facing == -1 and bullet.x + 8 >= player_center_x + 8 >= bullet.x:
                                pass
                            elif player_down_y + 138 <= bullet.y + enemy.height//2:
                                object_count += 1
        return object_count

    def drawBullets(self):
        super(AIPlayer, self).drawBullets()
