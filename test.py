import pygame
import sys

pygame.init()

screenWidth = 500
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
white = (255,255,255)
red = (255,0,0)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            sys.exit()

    screen.fill((red))
    pygame.display.update()

