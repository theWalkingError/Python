import pygame
import sys


size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
color = 255, 155, 245
margin = 10

block_width = block_height = 30


while True:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
    for col in range (10):
        x = col * block_height + (col + 1) * margin
        pygame.draw.rect(screen, color, (x, 0, block_width, block_height))
    pygame.display.flip()
        