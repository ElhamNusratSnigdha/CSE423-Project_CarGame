from circle import MidpointCircle
from line import MidpointLine
from digits import Digits
from rectangle import Reactangle
from menu import Menu


from rock import Rock

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


from random import randint
from threading import Thread
from time import sleep
from pynput.keyboard import Controller

import pygame

pygame.init()
pygame.mixer.music.load("music.mp3")
crash_sound = pygame.mixer.Sound("carCrash.mp3")
# Globals
colors = 0, 0, 0

SCORE = 0

X_MAX_GLOBAL = 700
X_MIN_GLOBAL = -700
Y_MAX_GLOBAL = 900
Y_MIN_GLOBAL = -900 
ROAD_LENGTH = 900

ROCKS = []
num_rocks = 7
for i in range(num_rocks):
    rock = Rock(randint(X_MIN_GLOBAL, X_MAX_GLOBAL), Y_MAX_GLOBAL,randint(10,15), randint(20,50))
    ROCKS.append(rock)

SPEED_MULTIPLIER = 4

MOVE_DISPLACEMENT = 50

auto_key_press = Controller()

line = MidpointLine()
circle = MidpointCircle()
menu = Menu()


CAR_X = 0
CAR_Y = - 600
CAR_WIDTH = 40

GAME_OVER = False

def update():
    global ROAD_LENGTH, colors, \
        CAR_Y, \
        CAR_X, \
        SPEED_MULTIPLIER, \
        GAME_OVER


    while True:
        SPEED_MULTIPLIER += 0.001
      
        auto_key_press.press(",")
        sleep(0.1)

        if GAME_OVER:
            break

        ROAD_LENGTH -= 20
        if ROAD_LENGTH <= -900:
            ROAD_LENGTH = 900

        colors = 1, 1, 0
        

        for i in range(num_rocks):
            ROCKS[i].y -= ROCKS[i].speed * SPEED_MULTIPLIER
            if ROCKS[i].y < Y_MIN_GLOBAL:
                ROCKS[i].y = 900
                ROCKS[i].x = randint(X_MIN_GLOBAL, X_MAX_GLOBAL)
        
        glutPostRedisplay()


def score_increment():
    global SCORE
    while True:
        sleep(1)
        glutPostRedisplay()
        SCORE += 1
        if GAME_OVER:
            break

class Race:
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0,
                 pixel_size=1):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.pixel_size = pixel_size


        self.player1_radius = 40
        self.player1_move_x = 0
        self.player1_move_y = 0
        self.score = 10

        self.player2_radius = 20
        self.player_move_x = 0
        self.player_move_y = 0



    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(b"Race Game")
        glClearColor(0, 0, 0, 0),
        glutDisplayFunc(self.show_screen)
        glutKeyboardFunc(self.buttons)

        animation_thread = Thread(target=update)
        animation_thread.start()

        global score_thread
        score_thread = Thread(target=score_increment)
        score_thread.start()

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -
                self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()
        pygame.mixer.music.play(-1)

    def buttons(self, key, x, y):
        global CAR_Y, \
            CAR_X, \
            CAR_WIDTH, \
            GAME_OVER, \
            SCORE

        if key == b"w" and CAR_Y < Y_MAX_GLOBAL:
            CAR_Y += MOVE_DISPLACEMENT
        if key == b"a" and CAR_X > X_MIN_GLOBAL:
            CAR_X -= MOVE_DISPLACEMENT
        if key == b"s" and CAR_Y > Y_MIN_GLOBAL:
            CAR_Y -= MOVE_DISPLACEMENT
        if key == b"d" and CAR_X < X_MAX_GLOBAL:
            CAR_X += MOVE_DISPLACEMENT

        if CAR_Y < - self.win_size_y:
            CAR_Y = self.win_size_y

        if CAR_X < - self.win_size_x:
            CAR_X = self.win_size_x

        if CAR_Y > self.win_size_y:
            CAR_Y = - self.win_size_y

        if CAR_X > self.win_size_x:
            CAR_X = - self.win_size_x


        for i in range(num_rocks):
            if CAR_Y - CAR_WIDTH <= ROCKS[i].y <= CAR_Y + CAR_WIDTH and CAR_X - CAR_WIDTH <= ROCKS[i].x <= CAR_X + CAR_WIDTH:
                GAME_OVER = True
        

        glutPostRedisplay()

  
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)

        self.road()
        menu.score_text(950, 200)

       
        glColor3f(1, 0, 0)
        glPointSize(1)
        
        for i in range(num_rocks):  self.create_rock(ROCKS[i])
        
        
        glColor3f(0,1,0)
        Reactangle(CAR_WIDTH*2,CAR_X,CAR_Y/2)

        glPointSize(1)

        score_text = Digits()
        digit_position = 900
        glColor3f(colors[0], colors[1], colors[2])

        for i in range(10, 50, 4):
            score_text.draw_digit(
                f"{SCORE}", offset_x=i, offset_y=i, digit_position_x=digit_position)

        glColor3f(colors[2], colors[1], colors[0])

        if GAME_OVER:
            glColor3f(0, 0, 1)
            glColor3f(1, 0, 0)
            menu.game_over_text(-650, 0)
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(crash_sound)

        glutSwapBuffers()
        glutMainLoop()

    def start(self):
        glutMainLoop()

    def road(self):
        left_x1, left_y1 = X_MIN_GLOBAL, Y_MIN_GLOBAL
        offset = -50

        line.midpoint(left_x1 + offset, left_y1, left_x1 + offset, Y_MAX_GLOBAL)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - offset, Y_MAX_GLOBAL)

        for i in range(3):
            line.midpoint(left_x1 + offset + i, left_y1,
                          left_x1 + offset + i , Y_MAX_GLOBAL)
            line.midpoint(-left_x1 - offset - i, left_y1, -
                          left_x1 - offset - i , Y_MAX_GLOBAL)

    def create_rock(self, rock):
        circle.midpoint_circle_algorithm(rock.radius, rock.x, rock.y)
        circle.filled_circle(rock.radius, rock.x, rock.y)


race = Race(win_size_x=1920, win_size_y=900, pixel_size=1)

race.initialize()
race.start()
