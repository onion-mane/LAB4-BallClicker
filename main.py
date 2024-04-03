import pygame
from pygame.draw import *
from random import *
from math import sqrt
from time import *
pygame.init()

FPS = 60
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

NUM_OF_BALLS = 6
balls_array = []

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
    Задает параметры для нового шара в виде массива.
    Параметры по индексам
    0, 1) - координаты x, y
    2) r - радиус
    3) color - цвет
    4) dx - скорость по x
    5) dy - скорость по y
    '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,100)
    dx, dy = randint(-4, 4), randint(-4, 4)
    color = choice(COLORS)
    return [x,y,r,color,dx,dy]




def draw_ball(ball):
    circle(screen, ball[3], (ball[0], ball[1]), ball[2])
    f1 = pygame.font.Font(None, 32)
    ball_text = f1.render(str(110 - ball[2]), 1, "Black")
    screen.blit(ball_text, (ball[0]-12, ball[1]-10))
    '''
    Отрисовывает шар (ball)
    '''

def move_ball(ball):
    ball[0] += ball[4]
    ball[1] += ball[5]
    if ball[0] - ball[2] < 0 or ball[0] + ball[2] > WIDTH:
        ball[4] = -ball[4]
    if ball[1] - ball[2] < 0 or ball[1] + ball[2] > HEIGHT:
        ball[5] = -ball[5]
    '''
    Двигает шар (ball)
    Отвечает за столкновение со стенами
    '''

def ball_is_clicked(event, ball):
    '''
    Проверяет попадание по шару
    :param clickPos: кортеж с координатами клика
    :param ballPos: кортеж с координатами шара
    :param radius: радиус шара
    :return: 1 - попадание, 0 - промах
    '''
    distance_vec = (event.pos[0] - ball[0],
                    event.pos[1] - ball[1])
    if sqrt(distance_vec[0]**2 + distance_vec[1]**2) <= ball[2]:

        return 1
    else:
        return 0



def score_tracker():
    '''
    Рендерит текст со счетом на экран.
    :return:
    '''
    f1 = pygame.font.Font(None, 64)
    text1 = f1.render("Счёт: " + str(SCORE), 1, "White")
    screen.blit(text1, (10, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
SCORE = 0

for _ in range(NUM_OF_BALLS):
    balls_array.append(new_ball())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls_array:
                if (ball_is_clicked(event,ball)):
                    SCORE += 110 - ball[2]
                    balls_array.remove(ball)
                    balls_array.append(new_ball())
                pygame.display.update()

    score_tracker()
    for ball in balls_array:
        draw_ball(ball)
        move_ball(ball)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
