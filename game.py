import random

import pygame
from Settings import ScreenWidth, playZoneYCoordinates, ScreenHeight, font, bg, bulletSound, hitSound, win, clock
from Player import Player
from Projectlite import Projectile
from bin.Enemys.Generator import GenerateEnemys
from bin.Boxes.Generator import GenerateBoxes
from bin.Events.Generator import GenerateEvents
from bin.Enemys.BaseEnemys import BaseShotEnemy


def redrawGameWindow():
    # Draw BackGround
    win.blit(bg, (0, 0))
    # Draw Staff
    enemys_generator.draw()
    box_generator.draw()
    player.draw()
    events_generator.draw()
    # Draw Health point
    health_width = 50
    for i in range(player.health):
        win.blit(pygame.transform.scale(pygame.image.load('resources/images/health.png'), (20, 20)),
                 (health_width, 10))
        health_width += 20
    # Draw Score Bar
    text = font.render("Score: " + str(player.score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
    win.blit(text, (ScreenWidth - 150, 10))
    # Draw Bullets
    # Update display
    #draw_line_to_objects()
    pygame.display.update()

def draw_line_to_objects():
    player_center_cordiats = {'x': player.x + player.width // 2, 'y': player.y + player.height // 2}
    for box in box_generator.boxes:
        pygame.draw.line(win, (0, 235, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                         [box.x + box.width // 2, box.y + box.height // 2], 1)
    for enemy in enemys_generator.enemys:
        pygame.draw.line(win, (183, 0, 70), [player_center_cordiats['x'], player_center_cordiats['y']],
                         [enemy.x + enemy.width // 2, enemy.y + enemy.height // 2], 1)
        if isinstance(enemy, BaseShotEnemy):
            for bullet in enemy.bullets:
                pygame.draw.line(win, (183, 235, 0), [player_center_cordiats['x'], player_center_cordiats['y']],
                                 [bullet.x, bullet.y], 1)

def isWindowClose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# mainloop
player = Player(ScreenWidth // 2, playZoneYCoordinates, 64, 64, win)
box_generator = GenerateBoxes(player, win)
enemys_generator = GenerateEnemys(player, win)
events_generator = GenerateEvents(player, win)
run = True
while run:
    clock.tick(30)
    keys = pygame.key.get_pressed()
    run = isWindowClose()
    # Enemys
    enemys_generator.action()
    # Boxes
    box_generator.action()
    # Events
    events_generator.action(enemys_generator.enemys)
    events_generator.add_event(box_generator.events)
    # Player
    player.action(keys, enemys_generator.enemys)
    # Draw all staff
    redrawGameWindow()

pygame.quit()
