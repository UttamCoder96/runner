import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) #for user interface window (weidth, height)
pygame.display.set_caption('Cathcer')
clock = pygame.time.Clock()  #for frame rate

# test_surface = pygame.Surface((100, 200)) #tocreate a block
# test_surface.fill('Purple') #for block colour
test_surface = pygame.image.load('background.jpg')
sun_surface = pygame.image.load('sun.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit window
            pygame.quit()
            exit()

    screen.blit(sun_surface,(-1500,-3000))
    screen.blit(test_surface,(0,100)) #to set the block position
    
    pygame.display.update()
    clock.tick(60)
