import pygame
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight, font, bg, bulletSound, hitSound, win, clock
from Player import Player
from Projectlite import Projectile
from bin.Enemys.Generator import GenerateEnemys
from bin.Enemys.BaseEnemys import BaseShotEnemy


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for enemy in enemys:
        enemy.draw(win)
        if isinstance(enemy, BaseShotEnemy):
            enemy.drawBullets(win)
    text = font.render("Score: " + str(man.score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
    health = font.render("{}/4".format(man.health), 1, (0, 255, 0))  # Arguments are: text, anti-aliasing, color
    win.blit(text, (ScreenWidth - 150, 10))
    win.blit(health, (100, 10))
    man.drawBullets(win)
    pygame.display.update()


def isWindowClose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# mainloop
man = Player(ScreenWidth//2, playZoneYCoordinates, 64, 64)
enemys = []
run = True
while run:
    enemys = GenerateEnemys().generate(enemys, shot=True)
    clock.tick(30)
    run = isWindowClose()
    keys = pygame.key.get_pressed()
    man.move(keys)
    man.shot(keys, enemys)
    for enemy in enemys:
        enemy.fight(man, win)
    redrawGameWindow()

pygame.quit()
