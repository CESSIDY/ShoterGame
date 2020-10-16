from .BaseEnemys import BaseFightEnemy
import pygame
from Settings import hitSound, ScreenWidth


class Goblin(BaseFightEnemy):
    def __init__(self, x, y, width, height):
        super(Goblin, self).__init__(x, y, width, height)
        self.walkRight = [pygame.image.load('resources/images/R1E.png'), pygame.image.load('resources/images/R2E.png'),
                          pygame.image.load('resources/images/R3E.png'),
                          pygame.image.load('resources/images/R4E.png'), pygame.image.load('resources/images/R5E.png'),
                          pygame.image.load('resources/images/R6E.png'),
                          pygame.image.load('resources/images/R7E.png'), pygame.image.load('resources/images/R8E.png'),
                          pygame.image.load('resources/images/R9E.png'),
                          pygame.image.load('resources/images/R10E.png'),
                          pygame.image.load('resources/images/R11E.png')]
        self.walkLeft = [pygame.image.load('resources/images/L1E.png'), pygame.image.load('resources/images/L2E.png'),
                         pygame.image.load('resources/images/L3E.png'),
                         pygame.image.load('resources/images/L4E.png'), pygame.image.load('resources/images/L5E.png'),
                         pygame.image.load('resources/images/L6E.png'),
                         pygame.image.load('resources/images/L7E.png'), pygame.image.load('resources/images/L8E.png'),
                         pygame.image.load('resources/images/L9E.png'),
                         pygame.image.load('resources/images/L10E.png'), pygame.image.load('resources/images/L11E.png')]

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:  # Since we have 11 images for each animtion our upper bound is 33.
            # We will show each image for 3 frames. 3 x 11 = 33.
            self.walkCount = 0
        if self.direction:  # If we are moving to the right we will display our walkRight images
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:  # Otherwise we will display the walkLeft images
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # Draws the hit box around the enemy

    def move(self):
        if self.direction:  # If we are moving right
            if self.x >= ScreenWidth:  # If we have not reached the furthest right point on our path.
                self.direction = False
                self.walkCount = 0
            else:
                self.x += self.vel
        else:  # If we are moving left
            if self.x + self.width <= 0:
                self.direction = True
                self.walkCount = 0
            else:
                self.x -= self.vel


    def fight(self, player, win):
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[
                2]:
                player.hit()
        # This will go at the top of or main loop.

    def hit(self):  # This will display when the enemy is hit
        hitSound.play()
        if self.health > 0:
            self.health -= 1
            return True
        else:
            self.visible = False
            return False
