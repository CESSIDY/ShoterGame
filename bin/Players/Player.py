import pygame, sys
# from Settings import ScreenHeight, ScreenWidth, bulletSound, playZoneYCoordinates
from Projectlite import Projectile
from datetime import timedelta, datetime
from bin.Players.BasePlayer import BasePlayer


class Player(BasePlayer):
    def __init__(self, win, settings):
        super().__init__(win, settings)

    def defaultState(self):
        super(Player, self).defaultState()

    def action(self, keys, enemys):
        super(Player, self).action(keys, enemys)

    def RestartWalkCountIfAnimationEnd(self):
        super(Player, self).RestartWalkCountIfAnimationEnd()

    def DrawShield(self):
        super(Player, self).DrawShield()

    def DrawWalk(self):
        super(Player, self).DrawWalk()

    def DrawStanding(self):
        super(Player, self).DrawStanding()

    def updateHitBox(self):
        super(Player, self).updateHitBox()

    def draw(self):
        super(Player, self).draw()

    def isMoveLeft(self, keys):
        return super(Player, self).isMoveLeft(keys)

    def MoveLeft(self):
        super(Player, self).MoveLeft()

    def isMoveRight(self, keys):
        return super(Player, self).isMoveRight(keys)

    def MoveRight(self):
        super(Player, self).MoveRight()

    def Standing(self):
        super(Player, self).Standing()

    def Jump(self, keys):
        super(Player, self).Jump(keys)

    def isInAirAfterJump(self):
        return super(Player, self).isInAirAfterJump()

    def JumpAction(self):
        super(Player, self).JumpAction()

    def JumpStop(self):
        super(Player, self).JumpStop()

    def move(self, keys):
        super(Player, self).move(keys)

    def isProtected(self):
        return super(Player, self).isProtected()

    def hit(self):
        super(Player, self).hit()

    def shot(self, keys, enemys):
        super(Player, self).shot(keys, enemys)

    def drawBullets(self):
        super(Player, self).drawBullets()
