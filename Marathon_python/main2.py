import pygame
import random
from os import listdir
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()
FPS = pygame.time.Clock()
screen = width, heigth = 800, 600
main_surface = pygame.display.set_mode(screen)

GRAY = 155, 155, 155
RED = 255, 0, 0
BLUE = 50, 74, 178
IMAGES_PATH = 'goose'

font = pygame.font.SysFont("Verdana", 20)

# ball = pygame.Surface((20, 20))
# ball.fill(GRAY)
# ball = pygame.transform.scale(pygame.image.load('player.png').convert_alpha(), (60, 40))
ball_images = [pygame.image.load(IMAGES_PATH + '/' + file).convert_alpha() for file in listdir(IMAGES_PATH)]
ball = ball_images[0]
ball_rect = ball.get_rect()
# ball_speed = [1, 1]
ball_speed = 5




def create_enemy():
    # enemy = pygame.Surface((20, 20))
    # enemy.fill(RED)
    enemy = pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(),(50, 18))
    enemy_rect = pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
    enemy_speed = random.randint(4, 8)
    return [enemy, enemy_rect, enemy_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2500)


def create_bonus():
    # bonus = pygame.Surface((20, 20))
    # bonus.fill(BLUE)
    bonus = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(), (45, 78))
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

# bg = pygame.image.load('background.png').convert()
bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bg_X =0
bg_X2 = bg.get_width()
bg_speed = 3

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3500)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 125)

img_index = 0
scores = 0
enemies = []
bonuses = []
is_working = True

while is_working:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            img_index += 1
            if img_index == len(ball_images):
                img_index = 0
            ball = ball_images[img_index]
            


    pressed_key = pygame.key.get_pressed()

    # main_surface.fill((0, 0, 0))
    # main_surface.blit(bg,(0, 0))
    bg_X -= bg_speed
    bg_X2 -= bg_speed

    if bg_X < -bg.get_width():
        bg_X = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_surface.blit(bg,(bg_X, 0))
    main_surface.blit(bg,(bg_X2, 0))

    main_surface.blit(ball, ball_rect)
    main_surface.blit(font.render(str(scores), True, RED), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if ball_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom > heigth:
            bonuses.pop(bonuses.index(bonus))

        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1

    if pressed_key[K_DOWN] and not ball_rect.bottom >= heigth:
        ball_rect = ball_rect.move((0, ball_speed))

    if pressed_key[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move((0, -ball_speed))

    if pressed_key[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move((-ball_speed, 0))

    if pressed_key[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move((ball_speed, 0))

    # print(ball_rect)
    # print('bobus', len(bonuses))
    # print('enemy', len(enemies))
    # main_surface.fill((155, 155, 155))
    pygame.display.flip()
