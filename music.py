import pygame
from pygame.locals import *
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
pygame.mixer.music.load("Europe - The Final Countdown.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
print("play music")
