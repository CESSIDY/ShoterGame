import pygame

pygame.init()
ScreenWidth = 1100
ScreenHeight = 700
playZoneYCoordinates = 550
flags = pygame.OPENGL | pygame.FULLSCREEN

pygame.display.set_caption("First Game")
bg = pygame.image.load('resources/images/bg.jpg')
font = pygame.font.SysFont("comicsans", 30, True)

bulletSound = pygame.mixer.Sound('resources/audio/bullet.wav')
hitSound = pygame.mixer.Sound('resources/audio/hit.wav')

music = pygame.mixer.music.load('resources/audio/music.wav')

win = pygame.display.set_mode((ScreenWidth, ScreenHeight))

pygame.mixer.music.play(-1)

clock = pygame.time.Clock()