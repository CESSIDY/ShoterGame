from .BaseEnemys import BaseShotEnemy
import pygame
import random
from Settings import hitSound, ScreenWidth
from Projectlite import Projectile


class Cowboy(BaseShotEnemy):
    def __init__(self, x, y, width, height):
        super(Cowboy, self).__init__(x, y, width, height)
        self.walkRight = [pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_0.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_1.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_2.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_3.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_4.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_5.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_6.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_7.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_8.png'), (55, 60)),
                          pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_R_9.png'), (55, 60))]
        self.walkLeft = [pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_0.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_1.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_2.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_3.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_4.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_5.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_6.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_7.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_8.png'), (55, 60)),
                         pygame.transform.scale(pygame.image.load('resources/images/cowboy/Run_L_9.png'), (55, 60))]

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 30:  # Since we have 11 images for each animtion our upper bound is 33.
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
        self.shot(player)

        # This will go at the top of or main loop.

    def shot(self, player):
        for bullet in self.bullets:
            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:  # Checks x coords
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:  # Checks y coords
                    player.hit()  # calls enemy hit method
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

        if self.direction:
            facing = 1
        else:
            facing = -1
        if len(self.bullets) < 5 and random.randint(0, 200) == 0:
            self.bullets.append(
                Projectile(round(self.x + self.width // 2), round(self.y + self.height // 2), 5, (255, 0, 0), facing))

    def hit(self):  # This will display when the enemy is hit
        hitSound.play()
        if self.health > 0:
            self.health -= 1
            return True
        else:
            self.visible = False
            return False

    def drawBullets(self, win):
        for bullet in self.bullets:
            bullet.draw(win)
