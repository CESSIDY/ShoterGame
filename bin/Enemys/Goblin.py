from .BaseEnemys import BaseFightEnemy
import pygame
#from Settings import hitSound, ScreenWidth


class Goblin(BaseFightEnemy):
    def __init__(self, x, y, width, height, settings):
        super(Goblin, self).__init__(x, y, width, height, settings)
        self.walkRight = [pygame.image.load('resources/images/R1E.png').convert_alpha(),
                          pygame.image.load('resources/images/R2E.png').convert_alpha(),
                          pygame.image.load('resources/images/R3E.png').convert_alpha(),
                          pygame.image.load('resources/images/R4E.png').convert_alpha(),
                          pygame.image.load('resources/images/R5E.png').convert_alpha(),
                          pygame.image.load('resources/images/R6E.png').convert_alpha(),
                          pygame.image.load('resources/images/R7E.png').convert_alpha(),
                          pygame.image.load('resources/images/R8E.png').convert_alpha(),
                          pygame.image.load('resources/images/R9E.png').convert_alpha(),
                          pygame.image.load('resources/images/R10E.png').convert_alpha(),
                          pygame.image.load('resources/images/R11E.png').convert_alpha()]
        self.walkLeft = [pygame.image.load('resources/images/L1E.png').convert_alpha(),
                         pygame.image.load('resources/images/L2E.png').convert_alpha(),
                         pygame.image.load('resources/images/L3E.png').convert_alpha(),
                         pygame.image.load('resources/images/L4E.png').convert_alpha(),
                         pygame.image.load('resources/images/L5E.png').convert_alpha(),
                         pygame.image.load('resources/images/L6E.png').convert_alpha(),
                         pygame.image.load('resources/images/L7E.png').convert_alpha(),
                         pygame.image.load('resources/images/L8E.png').convert_alpha(),
                         pygame.image.load('resources/images/L9E.png').convert_alpha(),
                         pygame.image.load('resources/images/L10E.png').convert_alpha(),
                         pygame.image.load('resources/images/L11E.png').convert_alpha()]

    def draw(self, win):
        super(Goblin, self).draw(win)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # Draws the hit box around the enemy

    def move(self):
        super(Goblin, self).move()

    def fight(self, player, win):
        super(Goblin, self).fight(player, win)
        # This will go at the top of or main loop.

    def hit(self):  # This will display when the enemy is hit
        return super(Goblin, self).hit()
    
    def die(self):  # This will display when the enemy is hit
        super(Goblin, self).die()
