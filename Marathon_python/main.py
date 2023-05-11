import pygame 
import random
from pygame.constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

main_surface = pygame.display.set_mode(screen)


ball = pygame.Surface((20, 20))
ball.fill((155, 155 ,155)) 
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.bottom >= heigth or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball.fill((random.randint(10,200),random.randint(10,200),random.randint(10,200)))
           
    if ball_rect.left <= 0 or ball_rect.right >= width:
        ball_speed[0] = -ball_speed[0]
        ball.fill((random.randint(10,200),random.randint(10,200),random.randint(10,200)))

    main_surface.fill((0, 0, 0))
    main_surface.blit(ball, ball_rect)

    # print(ball_rect)

    # main_surface.fill((155, 155, 155))
    pygame.display.flip()
