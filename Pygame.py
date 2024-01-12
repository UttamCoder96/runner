import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) #for user interface window (weidth, height)
pygame.display.set_caption('Cathcer')
clock = pygame.time.Clock()  #for frame rate

test_surface = pygame.Surface((100, 200)) #tocreate a block
test_surface.fill('Purple') #for block colour

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit window
            pygame.quit()
    screen.blit(test_surface,(100,100)) #to set the block position
    pygame.display.update()
    clock.tick(60)
