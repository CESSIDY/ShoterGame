import pygame

pygame.init()
ScreenWidth = 1100
ScreenHeight = 700
playZoneYCoordinates = 550

pygame.display.set_caption("First Game")
bg = pygame.image.load('resources/images/bg.jpg')

win = pygame.display.set_mode((ScreenWidth, ScreenHeight))

clock = pygame.time.Clock()

while True:
    pygame.display.set_mode((ScreenWidth, ScreenHeight))
    pygame.display.update()
    ScreenWidth += 1
    ScreenHeight += 1