import pygame
from pygame import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, MOUSEBUTTONDOWN
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)

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
#pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, MOUSEBUTTONDOWN])

music = pygame.mixer.music.load('resources/audio/music.wav')

flags = DOUBLEBUF
win = pygame.display.set_mode((ScreenWidth, ScreenHeight), flags, 16)

pygame.mixer.music.play(-1)

clock = pygame.time.Clock()