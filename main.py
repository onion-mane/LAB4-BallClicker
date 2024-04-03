import pygame
from pygame.draw import *
from random import randint
from math import sqrt
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global SCORE

def new_ball():
    '''
    Создает новый шар с координатами (x, y) и радиусом r.
    x, y, r - глобальные переменные
    '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def ball_is_clicked(clickPos, ballPos, radius):
    '''
    Проверяет попадание по шару
    :param clickPos: кортеж с координатами клика
    :param ballPos: кортеж с координатами шара
    :param radius: радиус шара
    :return: 1 - попадание, 0 - промах
    '''
    distance_vec = (clickPos[0] - ballPos[0],
                    clickPos[1] - ballPos[1])
    if sqrt(distance_vec[0]*distance_vec[0] + distance_vec[1]*distance_vec[1]) <= radius:
        return 1
    else:
        return 0


def score_tracker():
    '''
    Пополняет и выводит счет на экран.
    :return:
    '''
    f1 = pygame.font.Font(None, 64)
    text1 = f1.render("Счёт: " + str(SCORE), 1, "White")
    screen.blit(text1, (10, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
SCORE = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            if event.button == 1:
                if (ball_is_clicked(event.pos, (x, y), r)):
                    SCORE += 110 - r
                pygame.display.update()
    score_tracker()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
