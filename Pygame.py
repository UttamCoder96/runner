'''try:'''
import pygame
from sys import exit
pygame.init()
weidth = 800
height = 400
count = 0
screen = pygame.display.set_mode((weidth, height)) #for user interface window (weidth, height)
pygame.display.set_caption('Cathcer')
clock = pygame.time.Clock()  #for frame rate
# test_surface = pygame.Surface((100, 200)) #tocreate a block
# test_surface.fill('Purple') #for block colour
test_surface = pygame.image.load('green.jpg')
ball_surface = pygame.image.load('DVD.jpg').convert_alpha()
Bal = pygame.transform.scale(ball_surface,(50,50))
ball_position_X= 0
ball_position_Y = 0
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit window
            pygame.quit()
            exit()
    screen.blit(test_surface,(0,0)) #to set the block position
    count += 1
    if count % 2 == 0:
        ball_position_Y += 2
        ball_position_X += 2
        screen.blit(Bal,(ball_position_X, ball_position_Y))
    if count % 2 != 0:
        ball_position_Y -= 1
        ball_position_X += 1
        screen.blit(Bal,(ball_position_X, ball_position_Y))
    pygame.display.update()
    clock.tick(150)


'''except Exception as e:
    print(f'Error Found !!!{chr(2)}')'''
