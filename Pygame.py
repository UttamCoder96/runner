import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) #for user interface window (weidth, height)
pygame.display.set_caption('Cathcer')
clock = pygame.time.Clock()  #for frame rate

# test_surface = pygame.Surface((100, 200)) #tocreate a block
# test_surface.fill('Purple') #for block colour
test_surface = pygame.image.load('green.jpg')
ball_surface = pygame.image.load('background.jpg')
ball_position_X= 0
ball_position_Y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit window
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0)) #to set the block position
    #screen.blit(ball_surface,(ball_position_X,100))
    #ball_position_X += 1
    screen.blit('LOVE',(ball_position_X,0))
    pygame.display.update()
    clock.tick(150)
